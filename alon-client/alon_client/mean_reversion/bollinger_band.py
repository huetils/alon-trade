import asyncio
import logging
from logging.handlers import RotatingFileHandler
from typing import Any, Coroutine, Protocol, Union

import ccxt.pro
import numpy as np
import talib
from alon_client.candles import CandlestickChart
from ccxt.base.exchange import Exchange
from talib._ta_lib import MA_Type


class Logger:
    @staticmethod
    def setup_logger() -> logging.Logger:
        logger = logging.getLogger("OHLCVStreaming")
        logger.setLevel(logging.DEBUG)

        file_handler = RotatingFileHandler(
            "ohlcv_streaming.log", maxBytes=5 * 1024 * 1024, backupCount=5
        )
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        return logger


class Strategy(Protocol):
    @property
    def length(self) -> int: ...

    @property
    def logger(self) -> logging.Logger: ...

    def apply_strategy(self, symbol: str, close_prices: list[float]) -> None: ...


class BollingerBandsStrategy(Strategy):
    def __init__(self, length: int, multiplier: float, logger: logging.Logger):
        self._length = length
        self.multiplier = multiplier
        self._logger = logger

    @property
    def length(self) -> int:
        return self._length

    @property
    def logger(self) -> logging.Logger:
        return self._logger

    def compute_bollinger_bands(self, close_prices: list[float]) -> dict[str, float]:
        """
        Compute Bollinger Bands using TA-Lib.

        :param close_prices: list of close prices.
        :return: A dictionary containing the upper, middle, and lower bands.
        """
        upper, middle, lower = talib.BBANDS(
            np.array(close_prices),
            timeperiod=self.length,
            nbdevup=self.multiplier,
            nbdevdn=self.multiplier,
            matype=MA_Type.EMA,
        )
        return {"upper": upper[-1], "middle": middle[-1], "lower": lower[-1]}

    def apply_strategy(self, symbol: str, close_prices: list[float]) -> None:
        """
        Apply the Bollinger Bands strategy to generate buy/sell signals.

        :param symbol: Trading pair (e.g., 'BTC/USDT').
        :param close_prices: list of close prices.
        """
        self.logger.info(f"Applying Bollinger Bands strategy to {symbol}")

        if len(close_prices) >= self.length:
            bands = self.compute_bollinger_bands(close_prices)
            latest_close = close_prices[-1]
            if latest_close < bands["lower"]:
                self.logger.info(
                    f"{symbol}: Buy signal - close {latest_close} crossed below lower band {bands['lower']}"
                )
            elif latest_close > bands["upper"]:
                self.logger.info(
                    f"{symbol}: Sell signal - close {latest_close} crossed above upper band {bands['upper']}"
                )


async def fetch_ohlcv(
    exchange: Exchange, symbol: str, timeframe: str
) -> Union[list[list[float]], Exception]:
    """
    Fetch OHLCV data for a symbol from an exchange.

    :param exchange: CCXT exchange instance.
    :param symbol: Trading pair (e.g., 'BTC/USDT').
    :param timeframe: Timeframe for OHLCV data (e.g., '15m').
    :return: Latest OHLCV data or an exception.
    """
    try:
        return await exchange.watch_ohlcv(symbol, timeframe)  # type: ignore
    except Exception as e:
        return e


async def stream_ohlcv(
    exchange: Exchange,
    symbols: list[str],
    strategy: Strategy,
    chart: CandlestickChart,
    timeframe: str = "15m",
) -> None:
    """
    Stream OHLCV data for the specified exchange and symbols.

    :param exchange: An instance of a CCXT exchange.
    :param symbols: list of trading pairs (e.g., ['BTC/USDT', 'ETH/USDT']).
    :param strategy: An instance of a class implementing the Strategy protocol.
    :param chart: Instance of the RealTimeCandlestickChart to visualize the data.
    :param timeframe: Timeframe for OHLCV data (default is '15m').
    """
    price_data: dict[str, list[float]] = {symbol: [] for symbol in symbols}
    last_candle_timestamp: dict[str, float] = {}

    strategy.logger.info(f"Streaming OHLCV data for {exchange.id} {symbols}")

    try:
        while True:
            tasks = [fetch_ohlcv(exchange, symbol, timeframe) for symbol in symbols]
            results = await asyncio.gather(*tasks)

            for i, result in enumerate(results):
                symbol = symbols[i]

                if isinstance(result, Exception):
                    strategy.logger.error(
                        f"Error fetching OHLCV for {exchange.id} {symbol}: {result}"
                    )
                    continue

                if len(result) > 0 and len(result[-1]) >= 5:
                    current_candle = result[-1]
                    current_timestamp = current_candle[0]  # Candle timestamp

                    if (
                        symbol not in last_candle_timestamp
                        or current_timestamp != last_candle_timestamp[symbol]
                    ):
                        last_candle_timestamp[symbol] = current_timestamp

                        close_prices = price_data[symbol]
                        close_prices.append(current_candle[4])

                        if len(close_prices) > strategy.length:
                            close_prices.pop(0)

                        strategy.apply_strategy(symbol, close_prices)

                        # Update the real-time candlestick chart
                        chart.update_ohlcv(current_candle)
                else:
                    strategy.logger.warning(
                        f"Unexpected OHLCV format for {symbol}: {result}"
                    )

    except Exception as e:
        strategy.logger.error(f"Error in {exchange.id}: {e}")

    finally:
        await exchange.session.close()


async def initialize_exchange(exchange_id: str) -> Exchange:
    """
    Initialize and return a CCXT Pro exchange instance.

    :param exchange_id: The ID of the exchange (e.g., 'okx', 'binance').
    :return: An initialized CCXT Pro exchange instance.
    """
    try:
        exchange = getattr(ccxt.pro, exchange_id)()
        return exchange
    except AttributeError as e:
        raise ValueError(f"Exchange {exchange_id} is not supported.") from e


async def main() -> None:
    """
    Main function to stream OHLCV data and apply a generic strategy from multiple exchanges.
    """
    logger = Logger.setup_logger()
    strategy = BollingerBandsStrategy(length=20, multiplier=2.0, logger=logger)

    # Initialize the real-time candlestick chart
    chart = CandlestickChart(timeframe="15m", max_candles=20, refresh_rate=1.0)

    exchanges: list[dict[str, Any]] = [{"id": "okx", "symbols": ["BTC/USDT"]}]

    tasks: list[Coroutine[Any, Any, None]] = []

    for exchange_info in exchanges:
        exchange = await initialize_exchange(exchange_info["id"])
        tasks.append(
            stream_ohlcv(
                exchange, exchange_info["symbols"], strategy, chart, timeframe="15m"
            )
        )

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
