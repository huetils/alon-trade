"""
This type stub file was generated by pyright.
"""

from typing import List

import ccxt.async_support
from ccxt.async_support.base.ws.client import Client
from ccxt.base.types import Balances, Int, Market, OrderBook, Str, Ticker, Trade

class bitopro(ccxt.async_support.bitopro):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    async def watch_public(self, path, messageHash, marketId): ...
    async def watch_order_book(
        self, symbol: str, limit: Int = ..., params=...
    ) -> OrderBook:
        """
        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://github.com/bitoex/bitopro-offical-api-docs/blob/master/ws/public/order_book_stream.md

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def handle_order_book(self, client: Client, message):  # -> None:
        ...
    async def watch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://github.com/bitoex/bitopro-offical-api-docs/blob/master/ws/public/trade_stream.md

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    def handle_trade(self, client: Client, message):  # -> None:
        ...
    async def watch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        watches information on multiple trades made by the user

        https://github.com/bitoex/bitopro-offical-api-docs/blob/master/ws/private/matches_stream.md

        :param str symbol: unified market symbol of the market trades were made in
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trade structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    def handle_my_trade(self, client: Client, message):  # -> None:
        ...
    def parse_ws_trade(self, trade: dict, market: Market = ...) -> Trade: ...
    async def watch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://github.com/bitoex/bitopro-offical-api-docs/blob/master/ws/public/ticker_stream.md

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def handle_ticker(self, client: Client, message):  # -> None:
        ...
    def authenticate(self, url):  # -> None:
        ...
    async def watch_balance(self, params=...) -> Balances:
        """
        watch balance and get the amount of funds available for trading or funds locked in orders

        https://github.com/bitoex/bitopro-offical-api-docs/blob/master/ws/private/user_balance_stream.md

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    def handle_balance(self, client: Client, message):  # -> None:
        ...
    def handle_message(self, client: Client, message):  # -> None:
        ...
