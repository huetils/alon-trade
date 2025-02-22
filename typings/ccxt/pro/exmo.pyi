"""
This type stub file was generated by pyright.
"""

from typing import List

import ccxt.async_support
from ccxt.async_support.base.ws.client import Client
from ccxt.base.types import (
    Balances,
    Int,
    Market,
    Order,
    OrderBook,
    Str,
    Strings,
    Ticker,
    Tickers,
    Trade,
)

class exmo(ccxt.async_support.exmo):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    def request_id(self):  # -> float | int:
        ...
    async def watch_balance(self, params=...) -> Balances:
        """
        watch balance and get the amount of funds available for trading or funds locked in orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    def handle_balance(self, client: Client, message):  # -> None:
        ...
    def parse_spot_balance(self, message):  # -> None:
        ...
    def parse_margin_balance(self, message):  # -> None:
        ...
    async def watch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#fd8f47bc-8517-43c0-bb60-1d61a86d4471

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    async def watch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for all markets of a specific list

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#fd8f47bc-8517-43c0-bb60-1d61a86d4471

        :param str[] [symbols]: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def handle_ticker(self, client: Client, message):  # -> None:
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

    def handle_trades(self, client: Client, message):  # -> None:
        ...
    async def watch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of trades associated with the user
        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    def handle_my_trades(self, client: Client, message):  # -> None:
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

    def handle_order_book(self, client: Client, message):  # -> None:
        ...
    def handle_delta(self, bookside, delta):  # -> None:
        ...
    def handle_deltas(self, bookside, deltas):  # -> None:
        ...
    async def watch_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#85f7bc03-b1c9-4cd2-bd22-8fd422272825
        https://documenter.getpostman.com/view/10287440/SzYXWKPi#95e4ed18-1791-4e6d-83ad-cbfe9be1051c

        watches information on multiple orders made by the user
        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def handle_orders(self, client: Client, message):  # -> None:
        ...
    def parse_ws_order(self, order: dict, market: Market = ...) -> Order: ...
    def parse_ws_trade(self, trade: dict, market: Market = ...) -> Trade: ...
    def handle_message(self, client: Client, message):  # -> None:
        ...
    def handle_subscribed(self, client: Client, message): ...
    def handle_info(self, client: Client, message): ...
    def handle_authentication_message(self, client: Client, message):  # -> None:
        ...
    async def authenticate(self, params=...): ...
