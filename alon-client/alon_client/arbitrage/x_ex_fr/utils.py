import asyncio
from dataclasses import dataclass
from decimal import Decimal
from typing import Any

from ccxt.base.exchange import Exchange

from alon_client.arbitrage.x_ex_fr.config import configurations
from alon_client.arbitrage.x_ex_fr.logger import logger


@dataclass
class Position:
    symbol: str
    direction: str
    size: float
    funding_time: str


open_positions: dict[str, Position] = {}


async def fetch_balance(exchange: Any, currency: str) -> Decimal:
    """Fetches balance from the given exchange."""
    attempts = 0
    while attempts < configurations["FETCH_BALANCE_MAX_RETRIES"]:
        try:
            balance = await exchange.fetch_balance()  # type: ignore
            return Decimal(balance["free"].get(currency, 0))  # type: ignore
        except Exception as e:
            logger.error(f"[{exchange.id}] Error fetching balance: {e}")
            attempts += 1
            await asyncio.sleep(2**attempts)

    return Decimal(0)


async def close_position(exchange: Exchange, symbol: str) -> None:
    """
    Closes an open position with a market order.
    """
    if symbol not in open_positions:
        logger.info(f"[{symbol}] No open position to close.")
        return

    try:
        position = open_positions[symbol]
        side = "sell" if position.direction == "long" else "buy"

        await exchange.create_market_order(  # type: ignore
            symbol, side, position.size, params={"reduceOnly": True}
        )

        del open_positions[symbol]
        logger.info(f"[{symbol}] Position closed.")

    except Exception as e:
        logger.exception(f"[{symbol}] Error closing position: {e}")


async def transfer_funds(
    source_exchange: Exchange,
    dest_exchange: Exchange,
    currency: str,
    amount: Decimal,
) -> bool:
    """
    Transfers funds from one exchange to another.

    Args:
        source_exchange (Exchange): The exchange to withdraw from.
        dest_exchange (Exchange): The exchange to deposit to.
        currency (str): The currency to transfer.
        amount (Decimal): The amount to transfer.

    Returns:
        bool: True if transfer was initiated successfully, False otherwise.
    """
    try:
        logger.info(
            f"Initiating transfer of {amount} {currency} from {source_exchange.id} to {dest_exchange.id}"
        )

        # Fetch deposit address from destination exchange
        deposit_address_info: dict[str, Any] = dict(
            await dest_exchange.fetch_deposit_address(currency)  # type: ignore
        )

        deposit_address: str | None = deposit_address_info["address"]  # type: ignore
        tag = deposit_address_info.get(  # type: ignore
            "tag", None
        )  # Some currencies require a tag/memo

        if not deposit_address:
            logger.error(
                f"[{dest_exchange.id}] No deposit address found for {currency}"
            )
            return False

        logger.info(
            f"[{dest_exchange.id}] Deposit address for {currency}: {deposit_address} (Tag: {tag})"
        )

        # Withdraw funds from source exchange to the deposit address
        withdrawal_params: dict[str, float | str] = {
            "address": deposit_address,
            "amount": float(amount),
        }

        if tag:
            withdrawal_params["tag"] = tag

        withdrawal_tx = await source_exchange.withdraw(  # type: ignore
            currency, float(amount), deposit_address, tag
        )

        logger.info(f"[{source_exchange.id}] Withdrawal successful: {withdrawal_tx}")

        return True
    except Exception as e:
        logger.error(f"[{source_exchange.id}] Error transferring funds: {e}")
        return False
