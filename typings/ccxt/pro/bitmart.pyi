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
    Position,
    Str,
    Strings,
    Ticker,
    Tickers,
    Trade,
)

class bitmart(ccxt.async_support.bitmart):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    async def subscribe(self, channel, symbol, type, params=...): ...
    async def subscribe_multiple(
        self, channel: str, type: str, symbols: Strings = ..., params=...
    ): ...
    async def watch_balance(self, params=...) -> Balances:
        """

        https://developer-pro.bitmart.com/en/spot/#private-balance-change
        https://developer-pro.bitmart.com/en/futuresv2/#private-assets-channel

        watch balance and get the amount of funds available for trading or funds locked in orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    def set_balance_cache(self, client: Client, type, subscribeHash):  # -> None:
        ...
    async def load_balance_snapshot(self, client, messageHash, type):  # -> None:
        ...
    def handle_balance(self, client: Client, message):  # -> None:
        ...
    async def watch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """

        https://developer-pro.bitmart.com/en/spot/#public-trade-channel
        https://developer-pro.bitmart.com/en/futuresv2/#public-trade-channel

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

        https://developer-pro.bitmart.com/en/spot/#public-trade-channel

        get the list of most recent trades for a list of symbols
        :param str[] symbols: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    def get_params_for_multiple_sub(
        self, methodName: str, symbols: List[str], limit: Int = ..., params=...
    ):  # -> list[Any]:
        ...
    async def watch_ticker(self, symbol: str, params=...) -> Ticker:
        """

        https://developer-pro.bitmart.com/en/spot/#public-ticker-channel
        https://developer-pro.bitmart.com/en/futuresv2/#public-ticker-channel

        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market
        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    async def watch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """

        https://developer-pro.bitmart.com/en/spot/#public-ticker-channel
        https://developer-pro.bitmart.com/en/futuresv2/#public-ticker-channel

        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for all markets of a specific list
        :param str[] symbols: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    async def watch_bids_asks(self, symbols: Strings = ..., params=...) -> Tickers:
        """

        https://developer-pro.bitmart.com/en/spot/#public-ticker-channel
        https://developer-pro.bitmart.com/en/futuresv2/#public-ticker-channel

        watches best bid & ask for symbols
        :param str[] symbols: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def handle_bid_ask(self, client: Client, message):  # -> None:
        ...
    def parse_ws_bid_ask(
        self, ticker, market=...
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
    async def watch_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        watches information on multiple orders made by the user

        https://developer-pro.bitmart.com/en/spot/#private-order-progress
        https://developer-pro.bitmart.com/en/futuresv2/#private-order-channel

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def handle_orders(self, client: Client, message):  # -> None:
        ...
    def parse_ws_order(
        self, order: dict, market: Market = ...
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
    def parse_ws_order_status(self, statusId):  # -> str | None:
        ...
    def parse_ws_order_side(self, sideId):  # -> str | None:
        ...
    async def watch_positions(
        self, symbols: Strings = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Position]:
        """

        https://developer-pro.bitmart.com/en/futures/#private-position-channel

        watch all open positions
        :param str[]|None symbols: list of unified market symbols
        :param int [since]: the earliest time in ms to fetch positions
        :param int [limit]: the maximum number of positions to retrieve
        :param dict params: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `position structure <https://docs.ccxt.com/en/latest/manual.html#position-structure>`
        """
        ...

    def handle_positions(self, client: Client, message):  # -> None:
        ...
    def parse_ws_position(self, position, market: Market = ...):  # -> dict[Any, Any]:
        ...
    def handle_trade(self, client: Client, message):  # -> None:
        ...
    def handle_trade_loop(self, entry): ...
    def parse_ws_trade(self, trade: dict, market: Market = ...):  # -> dict[Any, Any]:
        ...
    def handle_ticker(self, client: Client, message):  # -> None:
        ...
    def parse_ws_swap_ticker(
        self, ticker, market: Market = ...
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
    async def watch_ohlcv(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[list]:
        """

        https://developer-pro.bitmart.com/en/spot/#public-kline-channel
        https://developer-pro.bitmart.com/en/futuresv2/#public-klinebin-channel

        watches historical candlestick data containing the open, high, low, and close price, and the volume of a market
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

        https://developer-pro.bitmart.com/en/spot/#public-depth-all-channel
        https://developer-pro.bitmart.com/en/spot/#public-depth-increase-channel
        https://developer-pro.bitmart.com/en/futuresv2/#public-depth-channel

        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.speed]: *futures only* '100ms' or '200ms'
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def handle_delta(self, bookside, delta):  # -> None:
        ...
    def handle_deltas(self, bookside, deltas):  # -> None:
        ...
    def handle_order_book_message(self, client: Client, message, orderbook): ...
    def handle_order_book(self, client: Client, message):  # -> None:
        ...
    async def watch_order_book_for_symbols(
        self, symbols: List[str], limit: Int = ..., params=...
    ) -> OrderBook:
        """
        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://developer-pro.bitmart.com/en/spot/#public-depth-increase-channel

        :param str[] symbols: unified array of symbols
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.depth]: the type of order book to subscribe to, default is 'depth/increase100', also accepts 'depth5' or 'depth20' or depth50
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    async def authenticate(self, type, params=...): ...
    def handle_subscription_status(self, client: Client, message): ...
    def handle_authenticate(self, client: Client, message):  # -> None:
        ...
    def handle_error_message(self, client: Client, message):  # -> bool:
        ...
    def handle_message(self, client: Client, message):  # -> None:
        ...
