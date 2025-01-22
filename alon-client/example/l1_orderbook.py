import asyncio
import logging
from multiprocessing import Manager, Process

import ccxt.pro as ccxt

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)

log = logging.getLogger(__name__)


class OrderBookManager:
    """Manages and displays the order book table."""

    HEADER = (
        f"{'Exchange':<10} {'Symbol':<20} {'Bid':<20} {'Ask':<20} {'Midprice':<20}\n"
    )
    SEPARATOR = "-" * 90 + "\n"

    def __init__(self, shared_orderbooks: dict[tuple[str, str], dict[str, float]]):
        self.orderbooks = shared_orderbooks

    def update(self, exchange: str, symbol: str, bid: float, ask: float):
        """Update the order book data."""
        self.orderbooks[(exchange, symbol)] = {"bid": bid, "ask": ask}
        self.display_table()

    def display_table(self):
        """Display the updated table with midprice calculation and mean row."""
        # Initialize sums and counts for calculating the averages
        bid_sum = 0.0
        ask_sum = 0.0
        midprice_sum = 0.0
        count = 0

        # Start with ANSI escape code to clear the screen
        table = "\033[H\033[J\n" + self.HEADER + self.SEPARATOR

        for (exchange, symbol), data in self.orderbooks.items():
            bid = data["bid"]
            ask = data["ask"]
            midprice = (bid + ask) / 2 if bid and ask else 0.0
            formatted_midprice = f"{midprice:.5f}"

            # Add to the table
            table += f"{exchange:<10} {symbol:<20} {bid:<20} {ask:<20} {formatted_midprice:<20}\n"

            # Accumulate values for mean calculation
            if bid and ask:
                bid_sum += bid
                ask_sum += ask
                midprice_sum += midprice
                count += 1

        # Calculate averages
        mean_bid = bid_sum / count if count > 0 else 0.0
        mean_ask = ask_sum / count if count > 0 else 0.0
        mean_midprice = midprice_sum / count if count > 0 else 0.0

        # Append the mean row
        table += self.SEPARATOR
        table += f"{'Mean':<10} {'-':<20} {f'{mean_bid:.5f}':<20} {f'{mean_ask:.5f}':<20} {f'{mean_midprice:.5f}':<20}\n"

        # Log the table
        log.info("\n" + table.strip())


async def stream_orderbook_l1(
    shared_orderbooks: dict[tuple[str, str], dict[str, float]],
    exchange_name: str,
    symbol: str,
):
    exchange = None
    manager = OrderBookManager(shared_orderbooks)

    try:
        exchange_class = getattr(ccxt, exchange_name)
        exchange = exchange_class(
            {
                "enableRateLimit": True,
            }
        )
        await exchange.load_markets()

        log.info("Streaming L1 order book for %s on %s...", symbol, exchange_name)

        while True:
            orderbook = await exchange.watch_order_book(symbol, limit=1)
            best_bid = orderbook["bids"][0][0] if len(orderbook["bids"]) > 0 else None
            best_ask = orderbook["asks"][0][0] if len(orderbook["asks"]) > 0 else None

            # Update the shared manager with the latest bid/ask
            manager.update(exchange_name, symbol, best_bid or 0.0, best_ask or 0.0)

    except Exception as e:
        log.error("Error with %s: %s", exchange_name, e)
    finally:
        if exchange is not None:
            await exchange.close()


def run_in_process(
    shared_orderbooks: dict[tuple[str, str], dict[str, float]],
    exchange_name: str,
    symbol: str,
):
    asyncio.run(stream_orderbook_l1(shared_orderbooks, exchange_name, symbol))


def main():
    exchanges = {
        "bybit": "ZEREBROUSDT",
        "bitget": "ZEREBROUSDT",
        "okx": "ZEREBRO-USDT-SWAP",
    }

    # Shared dictionary for inter-process communication
    with Manager() as manager:
        shared_orderbooks = manager.dict()

        processes: list[Process] = []

        for exchange, symbol in exchanges.items():
            process = Process(
                target=run_in_process, args=(shared_orderbooks, exchange, symbol)
            )
            process.start()
            processes.append(process)

        for process in processes:
            process.join()


if __name__ == "__main__":
    main()
