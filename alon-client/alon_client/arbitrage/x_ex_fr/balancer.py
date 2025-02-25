import asyncio
from decimal import Decimal
from typing import Any, Callable, Dict

import ccxt.async_support as ccxt
from ccxt.base.exchange import Exchange

from alon_client.arbitrage.x_ex_fr.logger import logger


class BalanceManager:
    def __init__(
        self,
        exchanges_config: list[dict[str, str]],
        fetch_balance: Callable[[Exchange, str], Any],
        transfer_funds: Callable[[Exchange, Exchange, str, Decimal], Any],
        config: Dict[str, Any],
    ) -> None:
        """
        Initializes the BalanceManager class.

        Args:
            exchanges_config: List of exchange configurations.
            fetch_balance: Function to fetch balance from an exchange.
            transfer_funds: Function to transfer funds between exchanges.
            config: Configuration settings.
        """
        self.exchanges_config = exchanges_config
        self.fetch_balance = fetch_balance
        self.transfer_funds = transfer_funds
        self.config = config
        self.exchanges: Dict[str, Exchange] = {}

    async def run(self) -> None:
        """Initialize exchanges and start balance monitoring."""
        try:
            await self._initialize_exchanges()
            await self._balance_monitor()
        except Exception as e:
            logger.error(f"[BALANCE_MANAGER] Critical error: {e}")
        finally:
            await self._close_exchanges()

    async def _initialize_exchanges(self) -> None:
        """Initializes exchanges with API credentials."""
        for ex in self.exchanges_config:
            exchange = getattr(ccxt, ex["id"])(
                {
                    "apiKey": ex["api_key"],
                    "secret": ex["api_secret"],
                    "password": ex.get("api_password", ""),
                    "enableRateLimit": True,
                }
            )
            self.exchanges[ex["id"]] = exchange

    async def _balance_monitor(self) -> None:
        """Monitor and balance funds across exchanges to prevent liquidation."""
        currency = self.config["QUOTE_CURRENCY"]
        min_balance = Decimal(self.config["MIN_BALANCE_THRESHOLD"])
        transfer_threshold = Decimal(self.config["TRANSFER_THRESHOLD"])

        while True:
            try:
                balances = await self._fetch_balances(currency)
                self._log_balances(balances, currency)
                await self._rebalance_funds(
                    balances, currency, min_balance, transfer_threshold
                )
                await asyncio.sleep(self.config["BALANCE_CHECK_INTERVAL"])
            except Exception as e:
                logger.error(f"[BALANCE_MONITOR] Unexpected error: {e}")

    async def _fetch_balances(self, currency: str) -> Dict[str, Decimal]:
        """Fetch balances from all exchanges."""
        return {
            ex_id: await self.fetch_balance(exchange, currency)
            for ex_id, exchange in self.exchanges.items()
        }

    def _log_balances(self, balances: Dict[str, Decimal], currency: str) -> None:
        """Logs balances in a structured format."""
        balance_info = ", ".join(
            [f"{ex}: {bal} {currency}" for ex, bal in balances.items()]
        )
        logger.info(f"Balances: {balance_info}")

    async def _rebalance_funds(
        self,
        balances: Dict[str, Decimal],
        currency: str,
        min_balance: Decimal,
        transfer_threshold: Decimal,
    ) -> None:
        """Rebalances funds between exchanges."""
        low_balance_exchanges = {
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
                        success = await self.transfer_funds(
                            self.exchanges[high_ex],
                            self.exchanges[low_ex],
                            currency,
                            transfer_amount,
                        )
                        if success:
                            logger.info(
                                f"Successfully transferred {transfer_amount} {currency} from {high_ex} to {low_ex}"
                            )

    async def _close_exchanges(self) -> None:
        """Closes all exchange sessions."""
        for exchange in self.exchanges.values():
            await exchange.session.close()
        logger.info("All exchange connections closed.")


# Smoke Test
if __name__ == "__main__":

    async def mock_fetch_balance(exchange: Exchange, currency: str) -> Decimal:
        return Decimal("100.0")

    async def mock_transfer_funds(
        source_exchange: Exchange,
        dest_exchange: Exchange,
        currency: str,
        amount: Decimal,
    ) -> bool:
        return True

    exchanges_config = [
        {
            "id": "mock",
            "api_key": "key",
            "api_secret": "secret",
            "api_password": "password",
        }
    ]

    config: dict[str, str | int] = {
        "QUOTE_CURRENCY": "USDT",
        "MIN_BALANCE_THRESHOLD": "50",
        "TRANSFER_THRESHOLD": "150",
        "BALANCE_CHECK_INTERVAL": 10,
    }

    balance_manager = BalanceManager(
        exchanges_config, mock_fetch_balance, mock_transfer_funds, config
    )
    asyncio.run(balance_manager.run())
