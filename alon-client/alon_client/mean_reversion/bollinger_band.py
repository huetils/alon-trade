import asyncio
import logging
from logging.handlers import RotatingFileHandler
from typing import Any, Coroutine, Dict, List, Protocol, Union

import ccxt.pro
import numpy as np
import talib
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

    def apply_strategy(self, symbol: str, close_prices: List[float]) -> None: ...


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

    def compute_bollinger_bands(self, close_prices: List[float]) -> Dict[str, float]:
        """
        Compute Bollinger Bands using TA-Lib.

        :param close_prices: List of close prices.
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

    def apply_strategy(self, symbol: str, close_prices: List[float]) -> None:
        """
        Apply the Bollinger Bands strategy to generate buy/sell signals.

        :param symbol: Trading pair (e.g., 'BTC/USDT').
        :param close_prices: List of close prices.
        """
        logging.info(f"Applying Bollinger Bands strategy to {symbol}")

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
    exchange: Any, symbol: str, timeframe: str
) -> Union[List[List[float]], Exception]:
    """
    Fetch OHLCV data for a symbol from an exchange.

    :param exchange: CCXT exchange instance.
    :param symbol: Trading pair (e.g., 'BTC/USDT').
    :param timeframe: Timeframe for OHLCV data (e.g., '1m').
    :return: Latest OHLCV data or an exception.
    """
    try:
        return await exchange.watch_ohlcv(symbol, timeframe)
    except Exception as e:
        return e


async def stream_ohlcv(
    exchange: Any, symbols: List[str], strategy: Strategy, timeframe: str = "1m"
) -> None:
    """
    Stream OHLCV data for the specified exchange and symbols.

    :param exchange: An instance of a CCXT exchange.
    :param symbols: List of trading pairs (e.g., ['BTC/USDT', 'ETH/USDT']).
    :param strategy: An instance of a class implementing the Strategy protocol.
    :param timeframe: Timeframe for OHLCV data (default is '1m').
    """
    # Store close prices for each symbol
    price_data: Dict[str, List[float]] = {symbol: [] for symbol in symbols}

    logging.info(f"Streaming OHLCV data for {exchange.id} {symbols}")

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
                    close_prices = price_data[symbol]
                    close_prices.append(result[-1][4])  # Append latest close price

                    if len(close_prices) > strategy.length:
                        close_prices.pop(0)

                    # Apply strategy
                    strategy.apply_strategy(symbol, close_prices)
                else:
                    strategy.logger.warning(
                        f"Unexpected OHLCV format for {symbol}: {result}"
                    )

    except Exception as e:
        strategy.logger.error(f"Error in {exchange.id}: {e}")

    finally:
        await exchange.close()


async def initialize_exchange(exchange_id: str) -> Any:
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

    # Define exchanges and their symbols
    exchanges: List[Dict[str, Any]] = [
        {"id": "okx", "symbols": ["BTC/USDT", "ETH/USDT"]},
        # {"id": "binance", "symbols": ["BTC/USDT", "ETH/USDT"]},
        # {"id": "kraken", "symbols": ["BTC/USD", "ETH/USD"]},
    ]

    tasks: List[Coroutine[Any, Any, None]] = []

    for exchange_info in exchanges:
        exchange = await initialize_exchange(exchange_info["id"])
        tasks.append(
            stream_ohlcv(exchange, exchange_info["symbols"], strategy, timeframe="1m")
        )

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
