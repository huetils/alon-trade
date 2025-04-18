"""
This type stub file was generated by pyright.
"""

from typing import List

import ccxt.async_support
from ccxt.async_support.base.ws.client import Client
from ccxt.base.types import Int, Order, OrderBook, Str, Strings, Ticker, Tickers, Trade

class coinbaseexchange(ccxt.async_support.coinbaseexchange):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    def authenticate(self):  # -> dict[str, Any]:
        ...
    async def subscribe(self, name, symbol=..., messageHashStart=..., params=...): ...
    async def subscribe_multiple(
        self, name, symbols=..., messageHashStart=..., params=...
    ): ...
    async def watch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market
        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    async def watch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for all markets of a specific list
        :param str[] [symbols]: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.channel]: the channel to subscribe to, tickers by default. Can be tickers, sprd-tickers, index-tickers, block-tickers
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    async def watch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol
        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    async def watch_trades_for_symbols(
        self, symbols: List[str], since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol
        :param str[] symbols: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    async def watch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        watches information on multiple trades made by the user
        :param str symbol: unified market symbol of the market trades were made in
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trade structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    async def watch_my_trades_for_symbols(
        self, symbols: Strings = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        watches information on multiple trades made by the user
        :param str[] symbols: unified symbol of the market to fetch trades for
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trade structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    async def watch_orders_for_symbols(
        self, symbols: Strings = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        watches information on multiple orders made by the user
        :param str[] symbols: unified symbol of the market to fetch orders for
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of trade structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def watch_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        watches information on multiple orders made by the user
        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def watch_order_book_for_symbols(
        self, symbols: List[str], limit: Int = ..., params=...
    ) -> OrderBook:
        """
        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str[] symbols: unified array of symbols
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    async def watch_order_book(
        self, symbol: str, limit: Int = ..., params=...
    ) -> OrderBook:
        """
        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def handle_trade(self, client: Client, message): ...
    def handle_my_trade(self, client: Client, message): ...
    def parse_ws_trade(self, trade, market=...):  # -> Trade:
        ...
    def parse_ws_order_status(self, status):  # -> str | None:
        ...
    def handle_order(self, client: Client, message):  # -> None:
        ...
    def parse_ws_order(
        self, order, market=...
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
    def handle_ticker(self, client: Client, message): ...
    def parse_ticker(self, ticker, market=...) -> Ticker: ...
    def handle_delta(self, bookside, delta):  # -> None:
        ...
    def handle_deltas(self, bookside, deltas):  # -> None:
        ...
    def handle_order_book(self, client: Client, message):  # -> None:
        ...
    def handle_subscription_status(self, client: Client, message): ...
    def handle_error_message(self, client: Client, message):  # -> Literal[True]:
        ...
    def handle_message(self, client: Client, message):  # -> None:
        ...
