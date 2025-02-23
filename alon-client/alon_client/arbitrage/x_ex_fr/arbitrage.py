import asyncio
from typing import Any, Callable

from alon_client.arbitrage.x_ex_fr.logger import logger


class FundingRateArbitrage:
    def __init__(
        self,
        exchanges_config: list[dict[str, Any]],
        initialize_exchange: Callable[..., Any],
        start_balance_manager: Callable[..., Any],
        funding_rate_collector: Callable[..., Any],
        funding_rate_analyzer: Callable[..., Any],
        top_opportunities: int,
    ) -> None:
        """
        Initializes the FundingRateArbitrage class with dependencies injected.

        Args:
            exchanges_config: List of exchange configurations.
            initialize_exchange: Function to initialize an exchange.
            start_balance_manager: Function to start balance management.
            funding_rate_collector: Function to collect funding rates.
            funding_rate_analyzer: Function to analyze funding rates.
            top_opportunities: Number of top swap markets to monitor.
        """
        self.exchanges_config = exchanges_config
        self.initialize_exchange = initialize_exchange
        self.start_balance_manager = start_balance_manager
        self.funding_rate_collector = funding_rate_collector
        self.funding_rate_analyzer = funding_rate_analyzer
        self.top_opportunities = top_opportunities
        self.exchanges: dict[str, Any] = {}

    async def run(self) -> None:
        """
        Asynchronously orchestrates funding rate arbitrage across multiple exchanges.
        """
        try:
            await self._initialize_exchanges()
            balance_manager_task = asyncio.create_task(
                self.start_balance_manager(self.exchanges_config)
            )
            collector_tasks = await self._start_funding_rate_collectors()
            analyzer_task = asyncio.create_task(self.funding_rate_analyzer())
            await asyncio.gather(*collector_tasks, analyzer_task, balance_manager_task)
        except Exception as e:
            logger.exception(
                "Critical error in funding_rate_arbitrage loop:", exc_info=e
            )
        finally:
            await self._close_exchanges()

    async def _initialize_exchanges(self) -> None:
        """Initializes exchanges and loads markets."""
        for ex in self.exchanges_config:
            exchange = await self.initialize_exchange(
                exchange_id=ex["id"],
                api_key=ex["api_key"],
                api_secret=ex["api_secret"],
                api_password=ex.get("api_password", ""),
            )

            await exchange.load_markets()  # type: ignore

            self.exchanges[ex["id"]] = exchange

        logger.info(f"Initialized {len(self.exchanges)} exchanges.")

    async def _start_funding_rate_collectors(self) -> list[asyncio.Task[None]]:
        """Starts tasks for collecting funding rates."""
        collector_tasks: list[asyncio.Task[None]] = []

        for ex in self.exchanges_config:
            exchange = self.exchanges[ex["id"]]
            swap_markets = [
                m for m in exchange.markets if exchange.markets[m]["type"] == "swap"
            ]

            selected_markets = swap_markets[: self.top_opportunities]
            logger.info(f"[{ex['id']}] Selected swap markets: {selected_markets}")

            for market in selected_markets:
                collector_tasks.append(
                    asyncio.create_task(self.funding_rate_collector(exchange, market))
                )

        return collector_tasks

    async def _close_exchanges(self) -> None:
        """Closes all exchange sessions."""
        for exchange in self.exchanges.values():
            await exchange.session.close()

        logger.info("All exchange connections closed.")


# Smoke Test
if __name__ == "__main__":

    async def mock_initialize_exchange(
        exchange_id: str, api_key: str, api_secret: str, api_password: str = ""
    ):
        class MockExchange:
            markets = {"BTC/USDT": {"type": "swap"}, "ETH/USDT": {"type": "swap"}}

            class MockSession:
                async def close(self):
                    pass  # Simulate an async close method

            session = MockSession()

            async def load_markets(self):
                pass

        return MockExchange()

    async def mock_start_balance_manager(config: list[dict[str, str]]):
        pass

    async def mock_funding_rate_collector(exchange: Any, market: str):
        pass

    async def mock_funding_rate_analyzer():
        pass

    exchanges_config = [
        {
            "id": "mock",
            "api_key": "key",
            "api_secret": "secret",
            "api_password": "password",
        }
    ]

    arbitrage = FundingRateArbitrage(
        exchanges_config,
        mock_initialize_exchange,
        mock_start_balance_manager,
        mock_funding_rate_collector,
        mock_funding_rate_analyzer,
        top_opportunities=1,
    )

    asyncio.run(arbitrage.run())
