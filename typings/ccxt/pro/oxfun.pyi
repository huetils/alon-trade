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
    Num,
    Order,
    OrderBook,
    OrderSide,
    OrderType,
    Position,
    Str,
    Strings,
    Ticker,
    Tickers,
    Trade,
)

class oxfun(ccxt.async_support.oxfun):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    async def subscribe_multiple(self, messageHashes, argsArray, params=...): ...
    async def watch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        watches information on multiple trades made in a market

        https://docs.ox.fun/?json#trade

        :param str symbol: unified market symbol of the market trades were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of trade structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int|str [params.tag]: If given it will be echoed in the reply and the max size of tag is 32
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    async def watch_trades_for_symbols(
        self, symbols: List[str], since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://docs.ox.fun/?json#trade

        :param str[] symbols:
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int|str [params.tag]: If given it will be echoed in the reply and the max size of tag is 32
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    def handle_trades(self, client: Client, message):  # -> None:
        ...
    def parse_ws_trade(self, trade, market=...) -> Trade: ...
    async def watch_ohlcv(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[list]:
        """
        watches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://docs.ox.fun/?json#candles

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int|str [params.tag]: If given it will be echoed in the reply and the max size of tag is 32
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
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

        https://docs.ox.fun/?json#candles

        :param str[][] symbolsAndTimeframes: array of arrays containing unified symbols and timeframes to fetch OHLCV data for, example [['BTC/USDT', '1m'], ['LTC/USDT', '5m']]
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int|str [params.tag]: If given it will be echoed in the reply and the max size of tag is 32
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...

    def handle_ohlcv(self, client: Client, message):  # -> None:
        ...
    def parse_ws_ohlcv(self, ohlcv, market: Market = ...) -> list: ...
    async def watch_order_book(
        self, symbol: str, limit: Int = ..., params=...
    ) -> OrderBook:
        """
        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://docs.ox.fun/?json#fixed-size-order-book
        https://docs.ox.fun/?json#full-order-book

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    async def watch_order_book_for_symbols(
        self, symbols: List[str], limit: Int = ..., params=...
    ) -> OrderBook:
        """
        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://docs.ox.fun/?json#fixed-size-order-book
        https://docs.ox.fun/?json#full-order-book

        :param str[] symbols: unified array of symbols
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int|str [params.tag]: If given it will be echoed in the reply and the max size of tag is 32
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def handle_order_book(self, client: Client, message):  # -> None:
        ...
    async def watch_ticker(self, symbol: str, params=...) -> Ticker:
        """

        https://docs.ox.fun/?json#ticker

        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market
        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int|str [params.tag]: If given it will be echoed in the reply and the max size of tag is 32
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    async def watch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """

        https://docs.ox.fun/?json#ticker

        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for all markets of a specific list
        :param str[] [symbols]: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int|str [params.tag]: If given it will be echoed in the reply and the max size of tag is 32
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def handle_ticker(self, client: Client, message):  # -> None:
        ...
    async def watch_bids_asks(self, symbols: Strings = ..., params=...) -> Tickers:
        """

        https://docs.ox.fun/?json#best-bid-ask

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
    async def watch_balance(self, params=...) -> Balances:
        """

        https://docs.ox.fun/?json#balance-channel

        watch balance and get the amount of funds available for trading or funds locked in orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int|str [params.tag]: If given it will be echoed in the reply and the max size of tag is 32
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    def handle_balance(self, client, message):  # -> None:
        ...
    async def watch_positions(
        self, symbols: Strings = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Position]:
        """

               https://docs.ox.fun/?json#position-channel

               watch all open positions
               :param str[]|None symbols: list of unified market symbols
        @param since
        @param limit
               :param dict params: extra parameters specific to the exchange API endpoint
               :param int|str [params.tag]: If given it will be echoed in the reply and the max size of tag is 32
               :returns dict[]: a list of `position structure <https://docs.ccxt.com/en/latest/manual.html#position-structure>`
        """
        ...

    def handle_positions(self, client: Client, message):  # -> None:
        ...
    def parse_ws_position(self, position, market: Market = ...):  # -> dict[Any, Any]:
        ...
    async def watch_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        watches information on multiple orders made by the user

        https://docs.ox.fun/?json#order-channel

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int|str [params.tag]: If given it will be echoed in the reply and the max size of tag is 32
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def handle_orders(self, client: Client, message):  # -> None:
        ...
    async def create_order_ws(
        self,
        symbol: str,
        type: OrderType,
        side: OrderSide,
        amount: float,
        price: Num = ...,
        params=...,
    ) -> Order:
        """

        https://docs.ox.fun/?json#order-commands

        create a trade order
        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market', 'limit', 'STOP_LIMIT' or 'STOP_MARKET'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.clientOrderId]: a unique id for the order
        :param int [params.timestamp]: in milliseconds. If an order reaches the matching engine and the current timestamp exceeds timestamp + recvWindow, then the order will be rejected.
        :param int [params.recvWindow]: in milliseconds. If an order reaches the matching engine and the current timestamp exceeds timestamp + recvWindow, then the order will be rejected. If timestamp is provided without recvWindow, then a default recvWindow of 1000ms is used.
        :param float [params.cost]: the quote quantity that can be used alternative for the amount for market buy orders
        :param float [params.triggerPrice]: The price at which a trigger order is triggered at
        :param float [params.limitPrice]: Limit price for the STOP_LIMIT order
        :param bool [params.postOnly]: if True, the order will only be posted if it will be a maker order
        :param str [params.timeInForce]: GTC(default), IOC, FOK, PO, MAKER_ONLY or MAKER_ONLY_REPRICE(reprices order to the best maker only price if the specified price were to lead to a taker trade)
        :param str [params.selfTradePreventionMode]: NONE, EXPIRE_MAKER, EXPIRE_TAKER or EXPIRE_BOTH for more info check here {@link https://docs.ox.fun/?json#self-trade-prevention-modes}
        :param str [params.displayQuantity]: for an iceberg order, pass both quantity and displayQuantity fields in the order request
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def edit_order_ws(
        self,
        id: str,
        symbol: str,
        type: OrderType,
        side: OrderSide,
        amount: Num = ...,
        price: Num = ...,
        params=...,
    ) -> Order:
        """
        edit a trade order

        https://docs.ox.fun/?json#modify-order

        :param str id: order id
        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of the currency you want to trade in units of the base currency
        :param float|None [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.timestamp]: in milliseconds. If an order reaches the matching engine and the current timestamp exceeds timestamp + recvWindow, then the order will be rejected.
        :param int [params.recvWindow]: in milliseconds. If an order reaches the matching engine and the current timestamp exceeds timestamp + recvWindow, then the order will be rejected. If timestamp is provided without recvWindow, then a default recvWindow of 1000ms is used.
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def handle_place_orders(self, client: Client, message):  # -> None:
        ...
    async def cancel_order_ws(self, id: str, symbol: Str = ..., params=...) -> Order:
        """

        https://docs.ox.fun/?json#cancel-order

        cancels an open order
        :param str id: order id
        :param str symbol: unified market symbol, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def cancel_orders_ws(self, ids: List[str], symbol: Str = ..., params=...):
        """

        https://www.okx.com/docs-v5/en/#order-book-trading-trade-ws-mass-cancel-order

        cancel multiple orders
        :param str[] ids: order ids
        :param str symbol: unified market symbol, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def authenticate(self, params=...): ...
    def handle_authentication_message(self, client: Client, message):  # -> None:
        ...
    def ping(self, client: Client):  # -> Literal['ping']:
        ...
    def handle_pong(self, client: Client, message): ...
    def handle_message(self, client: Client, message):  # -> None:
        ...
