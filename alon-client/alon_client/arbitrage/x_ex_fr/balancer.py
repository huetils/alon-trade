import asyncio
from decimal import Decimal

import ccxt.async_support as ccxt
from alon_client.arbitrage.x_ex_fr.config import configurations
from alon_client.arbitrage.x_ex_fr.logger import logger
from ccxt.base.exchange import Exchange


async def fetch_balance(exchange: Exchange, currency: str) -> Decimal:
    """
    Fetch the free balance of the specified currency from the exchange.
    """
    try:
        balance = await exchange.fetch_balance()  # type: ignore
        return Decimal(balance["free"].get(currency, 0))  # type: ignore
    except Exception as e:
        logger.error(f"[{exchange.id}] Error fetching balance: {e}")
        return Decimal(0)


async def transfer_funds(
    source_exchange: Exchange,
    dest_exchange: Exchange,
    currency: str,
    amount: Decimal,
) -> bool:
    """
    Transfer funds from one exchange to another.
    """
    try:
        logger.info(
            f"Transferring {amount} {currency} from {source_exchange.id} to {dest_exchange.id}"
        )

        # Withdraw from source exchange
        withdrawal_tx = await source_exchange.withdraw(  # type: ignore
            currency, float(amount), dest_exchange.id
        )

        logger.info(f"[{source_exchange.id}] Withdrawal successful: {withdrawal_tx}")

        return True
    except Exception as e:
        logger.error(f"[{source_exchange.id}] Error transferring funds: {e}")
        return False


async def balance_monitor(exchanges: dict[str, Exchange]) -> None:
    """
    Monitor and balance funds across exchanges to prevent liquidation.
    """
    currency = configurations["CURRENCY"]
    min_balance = Decimal(configurations["MIN_BALANCE_THRESHOLD"])
    transfer_threshold = Decimal(configurations["TRANSFER_THRESHOLD"])

    while True:
        try:
            balances: dict[str, Decimal] = {}

            # Fetch balances for each exchange
            for ex_id, exchange in exchanges.items():
                balances[ex_id] = await fetch_balance(exchange, currency)
                logger.info(f"[{ex_id}] Balance: {balances[ex_id]} {currency}")

            # Identify exchanges with low and high balances
            low_balance_exchanges: dict[str, Decimal] = {
                ex: bal for ex, bal in balances.items() if bal < min_balance
            }
            high_balance_exchanges = {
                ex: bal for ex, bal in balances.items() if bal > transfer_threshold
            }

            for low_ex, low_bal in low_balance_exchanges.items():
                for high_ex, high_bal in high_balance_exchanges.items():
                    if high_ex != low_ex:
                        transfer_amount = min(
                            high_bal - transfer_threshold, min_balance - low_bal
                        )
                        if transfer_amount > 0:
                            success = await transfer_funds(
                                exchanges[high_ex],
                                exchanges[low_ex],
                                currency,
                                transfer_amount,
                            )
                            if success:
                                logger.info(
                                    f"Successfully transferred {transfer_amount} {currency} from {high_ex} to {low_ex}"
                                )

            await asyncio.sleep(configurations["BALANCE_CHECK_INTERVAL"])
        except Exception as e:
            logger.error(f"[BALANCE_MONITOR] Unexpected error: {e}")


async def start_balance_manager(exchanges_config: list[dict[str, str]]) -> None:
    """
    Initialize exchanges and start balance monitoring.
    """
    exchanges: dict[str, Exchange] = {}

    try:
        for ex in exchanges_config:
            exchange = getattr(ccxt, ex["id"])(
                {
                    "apiKey": ex["api_key"],
                    "secret": ex["api_secret"],
                    "password": ex.get("api_password", ""),
                    "enableRateLimit": True,
                }
            )

            exchanges[ex["id"]] = exchange

        await balance_monitor(exchanges)
    except Exception as e:
        logger.error(f"[BALANCE_MANAGER] Critical error: {e}")
    finally:
        for exchange in exchanges.values():
            await exchange.session.close()
        logger.info("All exchange connections closed.")


if __name__ == "__main__":
    asyncio.run(start_balance_manager(configurations["EXCHANGES"]))
