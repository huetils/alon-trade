"""
This type stub file was generated by pyright.
"""

from typing import List

import ccxt.async_support
from ccxt.async_support.base.ws.client import Client
from ccxt.base.types import Balances, Int, Order, OrderBook, Str, Ticker, Trade

class okcoin(ccxt.async_support.okcoin):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    async def subscribe(self, channel, symbol, params=...): ...
    async def watch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://www.okcoin.com/docs-v5/en/#websocket-api-public-channel-trades-channel

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    async def watch_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        watches information on multiple orders made by the user

        https://www.okcoin.com/docs-v5/en/#websocket-api-private-channel-order-channel

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def handle_orders(self, client: Client, message, subscription=...):  # -> None:
        ...
    async def watch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://www.okcoin.com/docs-v5/en/#websocket-api-public-channel-tickers-channel

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def handle_trade(self, client: Client, message): ...
    def handle_ticker(self, client: Client, message): ...
    async def watch_ohlcv(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[list]:
        """
        watches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://www.okcoin.com/docs-v5/en/#websocket-api-public-channel-candlesticks-channel

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...

    def handle_ohlcv(self, client: Client, message):  # -> None:
        ...
    async def watch_order_book(
        self, symbol: str, limit: Int = ..., params=...
    ) -> OrderBook:
        """
        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://www.okcoin.com/docs-v5/en/#websocket-api-public-channel-order-book-channel

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def handle_delta(self, bookside, delta):  # -> None:
        ...
    def handle_deltas(self, bookside, deltas):  # -> None:
        ...
    def handle_order_book_message(self, client: Client, message, orderbook): ...
    def handle_order_book(self, client: Client, message): ...
    async def authenticate(self, params=...): ...
    async def watch_balance(self, params=...) -> Balances:
        """
        watch balance and get the amount of funds available for trading or funds locked in orders

        https://www.okcoin.com/docs-v5/en/#websocket-api-private-channel-account-channel

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    async def subscribe_to_user_account(self, negotiation, params=...): ...
    def handle_balance(self, client: Client, message):  # -> None:
        ...
    def handle_subscription_status(self, client: Client, message): ...
    def handle_authenticate(self, client: Client, message): ...
    def ping(self, client: Client):  # -> Literal['ping']:
        ...
    def handle_pong(self, client: Client, message): ...
    def handle_error_message(self, client: Client, message):  # -> Literal[False]:
        ...
    def handle_message(self, client: Client, message):  # -> None:
        ...
