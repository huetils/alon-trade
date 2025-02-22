import asyncio
import logging
from logging.handlers import RotatingFileHandler
from typing import Any, Dict, List

import ccxt.pro


def setup_logger():
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


logger = setup_logger()


async def stream_ohlcv(
    exchange_id: str, symbols: List[str], timeframe: str = "1m"
) -> None:
    """
    Stream OHLCV data for the specified exchange and symbols.

    Args:
        exchange_id (str): ID of the exchange (e.g., 'okx', 'binance').
        symbols (List[str]): List of trading pairs (e.g., ['BTC/USDT', 'ETH/USDT']).
        timeframe (str, optional): Timeframe for OHLCV data (default is '1m').

    Returns:
        None
    """
    exchange: Any = getattr(ccxt.pro, exchange_id)()

    try:
        while True:
            tasks = [exchange.watch_ohlcv(symbol, timeframe) for symbol in symbols]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    logger.error(
                        f"Error fetching OHLCV for {exchange_id} {symbols[i]}: {result}"
                    )
                else:
                    logger.info(f"{exchange_id} {symbols[i]} {result}")

    except Exception as e:
        logger.error(f"Error in {exchange_id}: {e}")

    finally:
        await exchange.close()


async def main() -> None:
    """
    Main function to stream OHLCV data from multiple exchanges.
    """

    # Define exchanges and their symbols
    exchanges: List[Dict[str, Any]] = [
        {"id": "okx", "symbols": ["BTC/USDT", "ETH/USDT"]},
        # {"id": "binance", "symbols": ["BTC/USDT", "ETH/USDT"]},
        # {"id": "kraken", "symbols": ["BTC/USD", "ETH/USD"]},
    ]

    # Create tasks for each exchange
    tasks = [
        stream_ohlcv(exchange["id"], exchange["symbols"], timeframe="1m")
        for exchange in exchanges
    ]

    # Run all tasks concurrently
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
