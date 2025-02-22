"""
This type stub file was generated by pyright.
"""

from typing import List

import ccxt.async_support
from ccxt.async_support.base.ws.client import Client
from ccxt.base.types import (
    Int,
    Market,
    Order,
    OrderBook,
    Position,
    Str,
    Strings,
    Ticker,
    Trade,
)

class vertex(ccxt.async_support.vertex):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    def request_id(self, url):  # -> float | int:
        ...
    async def watch_public(self, messageHash, message): ...
    async def watch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        watches information on multiple trades made in a market

        https://docs.vertexprotocol.com/developer-resources/api/subscriptions/streams

        :param str symbol: unified market symbol of the market trades were made in
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trade structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    def handle_trade(self, client: Client, message):  # -> None:
        ...
    async def watch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        watches information on multiple trades made by the user

        https://docs.vertexprotocol.com/developer-resources/api/subscriptions/streams

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.user]: user address, will default to self.walletAddress if not provided
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def handle_my_trades(self, client: Client, message):  # -> None:
        ...
    def parse_ws_trade(self, trade, market=...):  # -> dict[Any, Any]:
        ...
    async def watch_ticker(self, symbol: str, params=...) -> Ticker:
        """

        https://docs.vertexprotocol.com/developer-resources/api/subscriptions/streams

        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market
        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def parse_ws_ticker(
        self, ticker, market=...
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
    def handle_ticker(self, client: Client, message): ...
    async def watch_order_book(
        self, symbol: str, limit: Int = ..., params=...
    ) -> OrderBook:
        """

        https://docs.vertexprotocol.com/developer-resources/api/subscriptions/streams

        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return.
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def handle_order_book_subscription(
        self, client: Client, message, subscription
    ):  # -> None:
        ...
    async def fetch_order_book_snapshot(
        self, client, message, subscription
    ):  # -> None:
        ...
    def handle_order_book(self, client: Client, message):  # -> None:
        ...
    def handle_order_book_message(self, client: Client, message, orderbook): ...
    def handle_delta(self, bookside, delta):  # -> None:
        ...
    def handle_deltas(self, bookside, deltas):  # -> None:
        ...
    def handle_subscription_status(self, client: Client, message): ...
    async def watch_positions(
        self, symbols: Strings = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Position]:
        """

               https://docs.vertexprotocol.com/developer-resources/api/subscriptions/streams

               watch all open positions
               :param str[]|None symbols: list of unified market symbols
        @param since
        @param limit
               :param dict params: extra parameters specific to the exchange API endpoint
               :param str [params.user]: user address, will default to self.walletAddress if not provided
               :returns dict[]: a list of `position structure <https://docs.ccxt.com/en/latest/manual.html#position-structure>`
        """
        ...

    def set_positions_cache(
        self, client: Client, symbols: Strings = ..., params=...
    ):  # -> None:
        ...
    async def load_positions_snapshot(
        self, client, messageHash, symbols, params
    ):  # -> None:
        ...
    def handle_positions(self, client, message):  # -> None:
        ...
    def parse_ws_position(self, position, market=...):  # -> dict[Any, Any]:
        ...
    def handle_auth(self, client: Client, message):  # -> None:
        ...
    def build_ws_authentication_sig(
        self, message, chainId, verifyingContractAddress
    ): ...
    async def authenticate(self, params=...): ...
    async def watch_private(self, messageHash, message, params=...): ...
    async def watch_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        watches information on multiple orders made by the user

        https://docs.vertexprotocol.com/developer-resources/api/subscriptions/streams

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def parse_ws_order_status(self, status):  # -> str | None:
        ...
    def parse_ws_order(self, order, market: Market = ...) -> Order: ...
    def handle_order_update(self, client: Client, message):  # -> None:
        ...
    def handle_error_message(self, client: Client, message):  # -> bool:
        ...
    def handle_message(self, client: Client, message):  # -> None:
        ...
