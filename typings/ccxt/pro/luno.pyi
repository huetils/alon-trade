"""
This type stub file was generated by pyright.
"""

from typing import List

import ccxt.async_support
from ccxt.async_support.base.ws.client import Client
from ccxt.base.types import IndexType, Int, OrderBook, Trade

class luno(ccxt.async_support.luno):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    async def watch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://www.luno.com/en/developers/api#tag/Streaming-API

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of    trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    def handle_trades(self, client: Client, message, subscription):  # -> None:
        ...
    def parse_trade(self, trade, market=...) -> Trade: ...
    async def watch_order_book(
        self, symbol: str, limit: Int = ..., params=...
    ) -> OrderBook:
        """
        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dictConstructor [params]: extra parameters specific to the exchange API endpoint
        :param str [params.type]: accepts l2 or l3 for level 2 or level 3 order book
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def handle_order_book(self, client: Client, message, subscription):  # -> None:
        ...
    def custom_parse_order_book(
        self,
        orderbook,
        symbol,
        timestamp=...,
        bidsKey=...,
        asksKey: IndexType = ...,
        priceKey: IndexType = ...,
        amountKey: IndexType = ...,
        countOrIdKey: IndexType = ...,
    ):  # -> dict[str, Any]:
        ...
    def parse_bids_asks(
        self,
        bidasks,
        priceKey: IndexType = ...,
        amountKey: IndexType = ...,
        thirdKey: IndexType = ...,
    ):  # -> list[Any]:
        ...
    def custom_parse_bid_ask(
        self,
        bidask,
        priceKey: IndexType = ...,
        amountKey: IndexType = ...,
        thirdKey: IndexType = ...,
    ):  # -> list[Any | None]:
        ...
    def handle_delta(self, orderbook, message):  # -> None:
        ...
    def handle_message(self, client: Client, message):  # -> None:
        ...
