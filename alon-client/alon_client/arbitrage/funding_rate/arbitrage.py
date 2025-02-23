import asyncio

from alon_client.arbitrage.funding_rate.config import configurations
from alon_client.arbitrage.funding_rate.exchange import initialize_exchange
from alon_client.arbitrage.funding_rate.logger import logger
from alon_client.arbitrage.funding_rate.strategies import (
    funding_rate_analyzer,
    funding_rate_collector,
    manage_positions,
)


async def funding_rate_arbitrage(
    exchange_id: str, api_key: str, api_secret: str, api_password: str
) -> None:
    exchange = await initialize_exchange(exchange_id, api_key, api_secret, api_password)

    try:
        await exchange.load_markets()  # type: ignore
        logger.info("Markets loaded successfully.")

        all_swap_markets = [
            m for m in exchange.markets if exchange.markets[m]["type"] == "swap"
        ]
        selected_markets = all_swap_markets[: configurations["TOP_OPPORTUNITIES"]]
        logger.info(f"Selected swap markets: {selected_markets}")

        collector_tasks: list[asyncio.Task[None]] = [
            asyncio.create_task(funding_rate_collector(exchange, m))
            for m in selected_markets
        ]
        analyzer_task = asyncio.create_task(funding_rate_analyzer(exchange))
        manage_task = asyncio.create_task(manage_positions(exchange))

        await asyncio.gather(*collector_tasks, analyzer_task, manage_task)

    except Exception as e:
        logger.exception("Critical error in funding_rate_arbitrage loop:", exc_info=e)
    finally:
        await exchange.session.close()
        logger.info("Exchange connection closed.")
