import asyncio
from datetime import datetime, timezone
from typing import Any

from ccxt.base.exchange import Exchange

from alon_client.arbitrage.funding_rate.config import configurations
from alon_client.arbitrage.funding_rate.logger import logger
from alon_client.arbitrage.funding_rate.utils import close_position, try_open_position

latest_funding_rates: dict[str, dict[str, Any]] = {}
open_positions: dict[str, dict[str, Any]] = {}


async def funding_rate_collector(exchange: Exchange, market: str) -> None:
    while True:
        try:
            fr_info = await exchange.watch_funding_rate(market)  # type: ignore
            symbol = str(fr_info["symbol"])  # type: ignore
            funding_rate = str(fr_info["fundingRate"])  # type: ignore

            latest_funding_rates[symbol] = {
                "symbol": symbol,
                "funding_rate": funding_rate,
                "timestamp": datetime.now(timezone.utc),
            }
        except Exception as e:
            logger.exception(f"[{market}] watch_funding_rate error: {e}")
        await asyncio.sleep(5)


async def funding_rate_analyzer(exchange: Exchange) -> None:
    while True:
        try:
            for symbol, data in latest_funding_rates.items():
                fr = data["funding_rate"]

                if symbol in open_positions:
                    current_pos = open_positions[symbol]
                    if (current_pos["direction"] == "long" and fr < 0) or (
                        current_pos["direction"] == "short" and fr > 0
                    ):
                        logger.info(
                            f"[ANALYZER] Funding rate flipped for {symbol}, closing position."
                        )
                        await close_position(exchange, symbol)
                        continue

                await try_open_position(exchange, symbol, "short" if fr > 0 else "long")

            await asyncio.sleep(configurations["CHECK_INTERVAL"])
        except Exception as e:
            logger.exception(f"[ANALYZER] Unexpected error: {e}")


async def manage_positions(exchange: Exchange) -> None:
    while True:
        try:
            for symbol in list(open_positions.keys()):
                if datetime.now(timezone.utc) >= open_positions[symbol].get(
                    "funding_time", datetime.now(timezone.utc)
                ):
                    await close_position(exchange, symbol)
        except Exception as e:
            logger.exception(f"[MANAGE_POSITIONS] Error managing positions: {e}")
        await asyncio.sleep(10)
