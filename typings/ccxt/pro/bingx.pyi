"""
This type stub file was generated by pyright.
"""

from typing import List

import ccxt.async_support
from ccxt.async_support.base.ws.client import Client
from ccxt.base.types import (
    Balances,
    Int,
    Order,
    OrderBook,
    Str,
    Strings,
    Ticker,
    Tickers,
    Trade,
)

class bingx(ccxt.async_support.bingx):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    async def watch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://bingx-api.github.io/docs/#/en-us/spot/socket/market.html#Subscribe%20to%2024-hour%20Price%20Change
        https://bingx-api.github.io/docs/#/en-us/swapV2/socket/market.html#Subscribe%20to%2024-hour%20price%20changes
        https://bingx-api.github.io/docs/#/en-us/cswap/socket/market.html#Subscribe%20to%2024-Hour%20Price%20Change

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def handle_ticker(self, client: Client, message):  # -> None:
        ...
    def parse_ws_ticker(
        self, message, market=...
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
    async def watch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for all markets of a specific list

        https://bingx-api.github.io/docs/#/en-us/swapV2/socket/market.html#Subscribe%20to%2024-hour%20price%20changes%20of%20all%20trading%20pairs

        :param str[] symbols: unified symbol of the market to watch the tickers for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    async def watch_order_book_for_symbols(
        self, symbols: List[str], limit: Int = ..., params=...
    ) -> OrderBook:
        """
        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://bingx-api.github.io/docs/#/en-us/swapV2/socket/market.html#Subscribe%20Market%20Depth%20Data%20of%20all%20trading%20pairs

        :param str[] symbols: unified array of symbols
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    async def watch_ohlcv_for_symbols(
        self,
        symbolsAndTimeframes: List[List[str]],
        since: Int = ...,
        limit: Int = ...,
        params=...,
    ):  # -> dict[Any, Any]:
        """
        watches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://bingx-api.github.io/docs/#/en-us/swapV2/socket/market.html#Subscribe%20K-Line%20Data%20of%20all%20trading%20pairs

        :param str[][] symbolsAndTimeframes: array of arrays containing unified symbols and timeframes to fetch OHLCV data for, example [['BTC/USDT', '1m'], ['LTC/USDT', '5m']]
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...

    def get_order_book_limit_by_market_type(
        self, marketType: str, limit: Int = ...
    ):  # -> Int:
        ...
    def get_message_hash(
        self, unifiedChannel: str, symbol: Str = ..., extra: Str = ...
    ):  # -> str:
        ...
    async def watch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        watches information on multiple trades made in a market

        https://bingx-api.github.io/docs/#/spot/socket/market.html#Subscribe%20to%20tick-by-tick
        https://bingx-api.github.io/docs/#/swapV2/socket/market.html#Subscribe%20the%20Latest%20Trade%20Detail
        https://bingx-api.github.io/docs/#/en-us/cswap/socket/market.html#Subscription%20transaction%20by%20transaction

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def handle_trades(self, client: Client, message):  # -> None:
        ...
    async def watch_order_book(
        self, symbol: str, limit: Int = ..., params=...
    ) -> OrderBook:
        """
        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://bingx-api.github.io/docs/#/en-us/spot/socket/market.html#Subscribe%20Market%20Depth%20Data
        https://bingx-api.github.io/docs/#/en-us/swapV2/socket/market.html#Subscribe%20Market%20Depth%20Data
        https://bingx-api.github.io/docs/#/en-us/cswap/socket/market.html#Subscribe%20to%20Limited%20Depth

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def handle_delta(self, bookside, delta):  # -> None:
        ...
    def handle_order_book(self, client: Client, message):  # -> None:
        ...
    def parse_ws_ohlcv(self, ohlcv, market=...) -> list: ...
    def handle_ohlcv(self, client: Client, message):  # -> None:
        ...
    async def watch_ohlcv(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[list]:
        """
        watches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://bingx-api.github.io/docs/#/en-us/spot/socket/market.html#K-line%20Streams
        https://bingx-api.github.io/docs/#/en-us/swapV2/socket/market.html#Subscribe%20K-Line%20Data
        https://bingx-api.github.io/docs/#/en-us/cswap/socket/market.html#Subscribe%20to%20Latest%20Trading%20Pair%20K-Line

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...

    async def watch_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        watches information on multiple orders made by the user

        https://bingx-api.github.io/docs/#/en-us/spot/socket/account.html#Subscription%20order%20update%20data
        https://bingx-api.github.io/docs/#/en-us/swapV2/socket/account.html#Order%20update%20push
        https://bingx-api.github.io/docs/#/en-us/cswap/socket/account.html#Order%20update%20push

        :param str [symbol]: unified market symbol of the market orders are made in
        :param int [since]: the earliest time in ms to watch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def watch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        watches information on multiple trades made by the user

        https://bingx-api.github.io/docs/#/en-us/spot/socket/account.html#Subscription%20order%20update%20data
        https://bingx-api.github.io/docs/#/en-us/swapV2/socket/account.html#Order%20update%20push
        https://bingx-api.github.io/docs/#/en-us/cswap/socket/account.html#Order%20update%20push

        :param str [symbol]: unified market symbol of the market the trades are made in
        :param int [since]: the earliest time in ms to watch trades for
        :param int [limit]: the maximum number of trade structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    async def watch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://bingx-api.github.io/docs/#/en-us/spot/socket/account.html#Subscription%20account%20balance%20push
        https://bingx-api.github.io/docs/#/en-us/swapV2/socket/account.html#Account%20balance%20and%20position%20update%20push
        https://bingx-api.github.io/docs/#/en-us/cswap/socket/account.html#Account%20balance%20and%20position%20update%20push

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    def set_balance_cache(
        self, client: Client, type, subType, subscriptionHash, params
    ):  # -> None:
        ...
    async def load_balance_snapshot(
        self, client, messageHash, type, subType
    ):  # -> None:
        ...
    def handle_error_message(self, client, message):  # -> Literal[True]:
        ...
    async def keep_alive_listen_key(self, params=...):  # -> None:
        ...
    async def authenticate(self, params=...):  # -> None:
        ...
    async def pong(self, client, message):  # -> None:
        ...
    def handle_order(self, client, message):  # -> None:
        ...
    def handle_my_trades(self, client: Client, message):  # -> None:
        ...
    def handle_balance(self, client: Client, message):  # -> None:
        ...
    def handle_message(self, client: Client, message):  # -> None:
        ...
