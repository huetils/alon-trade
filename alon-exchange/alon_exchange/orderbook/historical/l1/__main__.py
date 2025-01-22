import asyncio
import sqlite3
import threading
from datetime import datetime, timezone
from queue import Queue
from typing import Any, Coroutine, Dict, List, Tuple

import ccxt.pro

# Configure database
DB_NAME: str = "orderbook_data.db"
data_queue: Queue[Tuple[str, str, str, str, str, float, float]] = Queue()


def setup_database() -> None:
    conn: sqlite3.Connection = sqlite3.connect(DB_NAME)
    cursor: sqlite3.Cursor = conn.cursor()

    exchanges = ["bybit", "bitget", "okx", "deribit", "kraken"]
    levels = ["L1", "L2"]

    for exchange in exchanges:
        for level in levels:
            table_name = f"{exchange}_orderbook_{level.lower()}"
            cursor.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    symbol TEXT,
                    timestamp TEXT,
                    side TEXT,
                    price REAL,
                    amount REAL
                )
            """
            )
    conn.commit()
    conn.close()


# Database writer thread
def database_writer() -> None:
    conn: sqlite3.Connection = sqlite3.connect(DB_NAME)
    cursor: sqlite3.Cursor = conn.cursor()
    while True:
        data: List[Tuple[str, str, str, str, str, float, float]] = []
        while not data_queue.empty():
            data.append(data_queue.get())
        if data:
            for entry in data:
                exchange, symbol, timestamp, level, side, price, amount = entry
                table_name = f"{exchange}_orderbook_{level.lower()}"
                try:
                    cursor.execute(
                        f"""
                        INSERT INTO {table_name} (symbol, timestamp, side, price, amount)
                        VALUES (?, ?, ?, ?, ?)
                    """,
                        (symbol, timestamp, side, price, amount),
                    )
                except sqlite3.OperationalError as e:
                    print(f"Error writing to {table_name}: {e}")
            conn.commit()


def start_database_writer() -> None:
    threading.Thread(target=database_writer, daemon=True).start()


# Fetch L1 and L2 data asynchronously using websockets
async def fetch_order_book(exchange_id: str, symbols: List[str]) -> None:
    exchange: Any = getattr(ccxt.pro, exchange_id)()

    try:
        while True:
            tasks: List[asyncio.Future[Any]] = []
            for symbol in symbols:
                tasks.append(exchange.watch_order_book(symbol))

            # Gather all updates in parallel
            results: List[Any] = await asyncio.gather(*tasks, return_exceptions=True)
            timestamp: str = datetime.now(timezone.utc).isoformat()

            for idx, order_book in enumerate(results):
                if isinstance(order_book, Exception):
                    print(
                        f"Error fetching data for {exchange_id} {symbols[idx]}: {order_book}"
                    )
                    continue

                symbol: str = symbols[idx]
                data: List[Tuple[str, str, str, str, str, float, float]] = []

                # L1 Data
                if "bids" in order_book and len(order_book["bids"]) > 0:
                    best_bid: Tuple[float, float] = order_book["bids"][0]
                    data.append(
                        (
                            exchange_id,
                            symbol,
                            timestamp,
                            "L1",
                            "bid",
                            best_bid[0],
                            best_bid[1],
                        )
                    )

                if "asks" in order_book and len(order_book["asks"]) > 0:
                    best_ask: Tuple[float, float] = order_book["asks"][0]
                    data.append(
                        (
                            exchange_id,
                            symbol,
                            timestamp,
                            "L1",
                            "ask",
                            best_ask[0],
                            best_ask[1],
                        )
                    )

                # L2 Data
                for bid in order_book.get("bids", [])[:10]:  # Top 10 bids
                    data.append(
                        (exchange_id, symbol, timestamp, "L2", "bid", bid[0], bid[1])
                    )

                for ask in order_book.get("asks", [])[:10]:  # Top 10 asks
                    data.append(
                        (exchange_id, symbol, timestamp, "L2", "ask", ask[0], ask[1])
                    )

                for entry in data:
                    data_queue.put(entry)

    except Exception as e:
        print(f"Error in websocket for {exchange_id}: {e}")

    finally:
        await exchange.close()


# Main entry point
async def main() -> None:
    setup_database()
    start_database_writer()

    exchanges: List[Dict[str, Any]] = [
        {"id": "bybit", "symbols": ["BTC/USDT", "ETH/USDT"]},
        {"id": "bitget", "symbols": ["BTC/USDT", "ETH/USDT"]},
        {"id": "okx", "symbols": ["BTC/USDT", "ETH/USDT"]},
        {"id": "deribit", "symbols": ["BTC/USDT", "ETH/USDT"]},
        {"id": "kraken", "symbols": ["BTC/USD", "ETH/USD"]},
    ]

    tasks: List[Coroutine[Any, Any, None]] = []
    for exchange in exchanges:
        tasks.append(fetch_order_book(exchange["id"], exchange["symbols"]))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
