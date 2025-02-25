import asyncio
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal
from typing import Any

from ccxt.base.exchange import Exchange

from alon_client.arbitrage.x_ex_fr.config import configurations
from alon_client.arbitrage.x_ex_fr.logger import logger


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


class FundingRateManager:
    def __init__(self, check_interval: int) -> None:
        self.check_interval = check_interval
        self._latest_funding_rates: dict[tuple[str, str], FundingRate] = {}
        self._open_positions: dict[str, Position] = {}

    async def collect_funding_rate(self, exchange: Exchange, market: str) -> None:
        """Collects funding rates from a specific exchange."""
        while True:
            try:
                fr_info: dict[str, Any] = dict(
                    await exchange.fetch_funding_rate(market)
                )  # type: ignore
                symbol = str(fr_info["symbol"])
                funding_rate = Decimal(str(fr_info["fundingRate"]))

                self._latest_funding_rates[(exchange.id, symbol)] = FundingRate(
                    exchange=exchange.id,
                    symbol=symbol,
                    funding_rate=funding_rate,
                    timestamp=datetime.now(timezone.utc),
                )
            except Exception as e:
                logger.exception(
                    f"[{exchange.id}:{market}] watch_funding_rate error: {e}"
                )

            await asyncio.sleep(self.check_interval)

    async def analyze_funding_rates(self) -> None:
        """Analyzes funding rates to find arbitrage opportunities."""
        while True:
            try:
                symbols = self._get_unique_symbols()
                for symbol in symbols:
                    rates = self._get_sorted_funding_rates(symbol)
                    if len(rates) < 2:
                        continue  # Need at least 2 exchanges for arbitrage

                    long_exchange, long_fr, short_exchange, short_fr = (
                        self._get_arbitrage_exchanges(rates)
                    )
                    if (short_fr - long_fr) >= configurations[
                        "MIN_ARBITRAGE_THRESHOLD"
                    ]:
                        self._handle_arbitrage(
                            symbol, long_exchange, long_fr, short_exchange, short_fr
                        )

                await asyncio.sleep(self.check_interval)
            except Exception as e:
                logger.exception(f"[ANALYZER] Unexpected error: {e}")

    def _get_unique_symbols(self) -> list[str]:
        """Extracts unique symbols from latest funding rates."""
        return list({symbol for _, symbol in self._latest_funding_rates.keys()})

    def _get_sorted_funding_rates(self, symbol: str) -> list[tuple[str, Decimal]]:
        """Retrieves and sorts funding rates for a given symbol."""
        rates = [
            (ex, data.funding_rate)
            for (ex, sym), data in self._latest_funding_rates.items()
            if sym == symbol
        ]
        rates.sort(key=lambda x: x[1])
        return rates

    def _get_arbitrage_exchanges(
        self, rates: list[tuple[str, Decimal]]
    ) -> tuple[str, Decimal, str, Decimal]:
        """Determines exchanges for arbitrage opportunities."""
        long_exchange, long_fr = rates[0]  # Lowest funding rate (long)
        short_exchange, short_fr = rates[-1]  # Highest funding rate (short)
        return long_exchange, long_fr, short_exchange, short_fr

    def _handle_arbitrage(
        self,
        symbol: str,
        long_exchange: str,
        long_fr: Decimal,
        short_exchange: str,
        short_fr: Decimal,
    ) -> None:
        """Handles the arbitrage opportunity decision-making process."""
        if symbol in self._open_positions:
            current_pos = self._open_positions[symbol]
            if (
                current_pos.long_exchange == short_exchange
                and current_pos.short_exchange == long_exchange
            ):
                logger.info(
                    f"[ANALYZER] Funding rate flipped for {symbol}, closing position."
                )
                del self._open_positions[symbol]
                return

            logger.info(
                f"[ANALYZER] Arbitrage position already open for {symbol}, skipping."
            )
            return

        logger.info(
            f"[ANALYZER] Opening arbitrage position: LONG on {long_exchange} ({long_fr:.4%}), "
            f"SHORT on {short_exchange} ({short_fr:.4%}) for {symbol}."
        )

        self._open_positions[symbol] = Position(
            long_exchange=long_exchange,
            short_exchange=short_exchange,
            symbol=symbol,
            funding_time=datetime.now(timezone.utc),
        )
