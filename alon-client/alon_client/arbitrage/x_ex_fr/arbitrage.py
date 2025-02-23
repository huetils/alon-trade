import asyncio
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Dict, List, Tuple

from alon_client.arbitrage.x_ex_fr.balancer import start_balance_manager
from alon_client.arbitrage.x_ex_fr.config import configurations
from alon_client.arbitrage.x_ex_fr.exchange import initialize_exchange
from alon_client.arbitrage.x_ex_fr.logger import logger
from ccxt.base.exchange import Exchange


@dataclass
class FundingRate:
    exchange: str
    symbol: str
    funding_rate: Decimal
    timestamp: datetime


@dataclass
class Position:
    long_exchange: str
    short_exchange: str
    symbol: str
    funding_time: datetime


# Dictionary to store the latest funding rates from all exchanges
latest_funding_rates: Dict[Tuple[str, str], FundingRate] = (
    {}
)  # {(exchange, symbol): FundingRate}
open_positions: Dict[str, Position] = {}  # {symbol: Position}


async def funding_rate_collector(exchange: Exchange, market: str) -> None:
    """
    Collects funding rates from a specific exchange and updates the latest_funding_rates dictionary.
    """
    while True:
        try:
            fr_info: Dict[str, Any] = dict(await exchange.fetch_funding_rate(market))  # type: ignore
            symbol = str(fr_info["symbol"])
            funding_rate = Decimal(str(fr_info["fundingRate"]))

            latest_funding_rates[(exchange.id, symbol)] = FundingRate(
                exchange=exchange.id,
                symbol=symbol,
                funding_rate=funding_rate,
                timestamp=datetime.now(timezone.utc),
            )

        except Exception as e:
            logger.exception(f"[{exchange.id}:{market}] watch_funding_rate error: {e}")

        await asyncio.sleep(configurations["CHECK_INTERVAL"])


async def funding_rate_analyzer() -> None:
    """
    Identifies arbitrage opportunities by comparing funding rates across exchanges.
    """
    while True:
        try:
            symbols = {symbol for _, symbol in latest_funding_rates.keys()}

            for symbol in symbols:
                rates = [
                    (ex, data.funding_rate)
                    for (ex, sym), data in latest_funding_rates.items()
                    if sym == symbol
                ]

                if len(rates) < 2:
                    continue  # Need at least 2 exchanges for arbitrage

                # Sort funding rates (ascending)
                rates.sort(key=lambda x: x[1])

                long_exchange, long_fr = rates[0]  # Lowest funding rate (long)
                short_exchange, short_fr = rates[-1]  # Highest funding rate (short)

                # Arbitrage condition: Funding rate difference must exceed the threshold
                if (short_fr - long_fr) >= configurations["MIN_ARBITRAGE_THRESHOLD"]:

                    # Avoid duplicate trades for the same symbol
                    if symbol in open_positions:
                        current_pos = open_positions[symbol]

                        # If the funding rates flipped, close the position
                        if (
                            current_pos.long_exchange == short_exchange
                            and current_pos.short_exchange == long_exchange
                        ):
                            logger.info(
                                f"[ANALYZER] Funding rate flipped for {symbol}, closing position."
                            )
                            # await close_position(current_pos.long_exchange, symbol)
                            # await close_position(current_pos.short_exchange, symbol)
                            del open_positions[symbol]
                            continue

                        logger.info(
                            f"[ANALYZER] Arbitrage position already open for {symbol}, skipping."
                        )
                        continue

                    # Open arbitrage position
                    logger.info(
                        f"[ANALYZER] Opening arbitrage position: LONG on {long_exchange} ({long_fr:.4%}), "
                        f"SHORT on {short_exchange} ({short_fr:.4%}) for {symbol}."
                    )

                    open_positions[symbol] = Position(
                        long_exchange=long_exchange,
                        short_exchange=short_exchange,
                        symbol=symbol,
                        funding_time=datetime.now(timezone.utc),
                    )

                    # await try_open_position(long_exchange, symbol, "long")
                    # await try_open_position(short_exchange, symbol, "short")

            await asyncio.sleep(configurations["CHECK_INTERVAL"])
        except Exception as e:
            logger.exception(f"[ANALYZER] Unexpected error: {e}")


async def funding_rate_arbitrage(exchanges_config: List[Dict[str, Any]]) -> None:
    """
    Initializes multiple exchanges, starts funding rate collectors, and runs arbitrage strategy.
    """
    exchanges: dict[str, Any] = {}

    try:
        # Initialize all exchanges
        for ex in exchanges_config:
            exchange = await initialize_exchange(
                exchange_id=ex["id"],
                api_key=ex["api_key"],
                api_secret=ex["api_secret"],
                api_password=ex.get("api_password", ""),
            )
            await exchange.load_markets()  # type: ignore
            exchanges[ex["id"]] = exchange

        logger.info(f"Initialized {len(exchanges)} exchanges.")

        # Start the balance manager alongside arbitrage monitoring
        balance_manager_task = asyncio.create_task(
            start_balance_manager(exchanges_config)
        )

        # Collect funding rates for each exchange's swap markets
        collector_tasks: list[asyncio.Task[None]] = []

        for ex in exchanges_config:
            exchange = exchanges[ex["id"]]
            swap_markets = [
                m for m in exchange.markets if exchange.markets[m]["type"] == "swap"
            ]
            selected_markets = swap_markets[: configurations["TOP_OPPORTUNITIES"]]

            logger.info(f"[{ex['id']}] Selected swap markets: {selected_markets}")

            for market in selected_markets:
                collector_tasks.append(
                    asyncio.create_task(funding_rate_collector(exchange, market))
                )

        # Run funding rate analyzer
        analyzer_task = asyncio.create_task(funding_rate_analyzer())

        await asyncio.gather(*collector_tasks, analyzer_task, balance_manager_task)

    except Exception as e:
        logger.exception("Critical error in funding_rate_arbitrage loop:", exc_info=e)

    finally:
        # Close all exchange sessions
        for exchange in exchanges.values():
            await exchange.session.close()
        logger.info("All exchange connections closed.")
