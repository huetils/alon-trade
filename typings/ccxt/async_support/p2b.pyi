"""
This type stub file was generated by pyright.
"""

from typing import List

from ccxt.abstract.p2b import ImplicitAPI
from ccxt.async_support.base.exchange import Exchange
from ccxt.base.types import (
    Int,
    Market,
    Num,
    Order,
    OrderSide,
    OrderType,
    Str,
    Strings,
    Ticker,
    Tickers,
)

class p2b(Exchange, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    async def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for bigone

        https://github.com/P2B-team/p2b-api-docs/blob/master/api-doc.md#markets

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...

    def parse_market(self, market: dict) -> Market: ...
    async def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://futures-docs.poloniex.com/#get-real-time-ticker-of-all-symbols

        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    async def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://github.com/P2B-team/p2b-api-docs/blob/master/api-doc.md#ticker

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def parse_ticker(
        self, ticker, market: Market = ...
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
    async def fetch_order_book(
        self, symbol: str, limit: Int = ..., params=...
    ):  # -> dict[str, Any]:
        """
               fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

               https://github.com/P2B-team/p2b-api-docs/blob/master/api-doc.md#depth-result

               :param str symbol: unified symbol of the market to fetch the order book for
               :param int [limit]: the maximum amount of order book entries to return
               :param dict [params]: extra parameters specific to the exchange API endpoint

        EXCHANGE SPECIFIC PARAMETERS
               :param str [params.interval]: 0(default), 0.00000001, 0.0000001, 0.000001, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1
               :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    async def fetch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        get the list of most recent trades for a particular symbol

        https://github.com/P2B-team/p2b-api-docs/blob/master/api-doc.md#history

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: 1-100, default=50
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int params['lastId']: order id
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    def parse_trade(self, trade: dict, market: Market = ...):  # -> dict[Any, Any]:
        ...
    async def fetch_ohlcv(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://github.com/P2B-team/p2b-api-docs/blob/master/api-doc.md#kline

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: 1m, 1h, or 1d
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: 1-500, default=50
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.offset]: default=0, with self value the last candles are returned
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...

    def parse_ohlcv(self, ohlcv, market: Market = ...) -> list: ...
    async def fetch_balance(self, params=...):  # -> dict[Any, Any]:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://github.com/P2B-team/p2b-api-docs/blob/master/api-doc.md#all-balances

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    def parse_balance(self, response):  # -> dict[Any, Any]:
        ...
    async def create_order(
        self,
        symbol: str,
        type: OrderType,
        side: OrderSide,
        amount: float,
        price: Num = ...,
        params=...,
    ):  # -> Order:
        """
        create a trade order

        https://github.com/P2B-team/p2b-api-docs/blob/master/api-doc.md#create-order

        :param str symbol: unified symbol of the market to create an order in
        :param str type: must be 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float price: the price at which the order is to be fulfilled, in units of the quote currency
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def cancel_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """
        cancels an open order

        https://github.com/P2B-team/p2b-api-docs/blob/master/api-doc.md#cancel-order

        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_open_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
               fetch all unfilled currently open orders

               https://github.com/P2B-team/p2b-api-docs/blob/master/api-doc.md#open-orders

               :param str symbol: unified market symbol of the market orders were made in
               :param int [since]: the earliest time in ms to fetch orders for
               :param int [limit]: the maximum number of order structures to retrieve
               :param dict [params]: extra parameters specific to the exchange API endpoint

        EXCHANGE SPECIFIC PARAMETERS
               :param int [params.offset]: 0-10000, default=0
               :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_order_trades(
        self, id: str, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
               fetch all the trades made from a single order

               https://github.com/P2B-team/p2b-api-docs/blob/master/api-doc.md#deals-by-order-id

               :param str id: order id
               :param str symbol: unified market symbol
               :param int [since]: the earliest time in ms to fetch trades for
               :param int [limit]: 1-100, default=50
               :param dict [params]: extra parameters specific to the exchange API endpoint

        EXCHANGE SPECIFIC PARAMETERS
               :param int [params.offset]: 0-10000, default=0
               :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    async def fetch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
               fetch all trades made by the user, only the transaction records in the past 3 month can be queried, the time between since and params["until"] cannot be longer than 24 hours

               https://github.com/P2B-team/p2b-api-docs/blob/master/api-doc.md#deals-history-by-market

               :param str symbol: unified market symbol of the market orders were made in
               :param int [since]: the earliest time in ms to fetch orders for, default = params["until"] - 86400000
               :param int [limit]: 1-100, default=50
               :param dict [params]: extra parameters specific to the exchange API endpoint
               :param int [params.until]: the latest time in ms to fetch orders for, default = current timestamp or since + 86400000

        EXCHANGE SPECIFIC PARAMETERS
               :param int [params.offset]: 0-10000, default=0
               :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    async def fetch_closed_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
               fetches information on multiple closed orders made by the user, the time between since and params["untnil"] cannot be longer than 24 hours

               https://github.com/P2B-team/p2b-api-docs/blob/master/api-doc.md#orders-history-by-market

               :param str symbol: unified market symbol of the market orders were made in
               :param int [since]: the earliest time in ms to fetch orders for, default = params["until"] - 86400000
               :param int [limit]: 1-100, default=50
               :param dict [params]: extra parameters specific to the exchange API endpoint
               :param int [params.until]: the latest time in ms to fetch orders for, default = current timestamp or since + 86400000

        EXCHANGE SPECIFIC PARAMETERS
               :param int [params.offset]: 0-10000, default=0
               :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def parse_order(self, order: dict, market: Market = ...) -> Order: ...
    def sign(
        self, path, api=..., method=..., params=..., headers=..., body=...
    ):  # -> dict[str, Any]:
        ...
    def handle_errors(
        self,
        code: int,
        reason: str,
        url: str,
        method: str,
        headers: dict,
        body: str,
        response,
        requestHeaders,
        requestBody,
    ):  # -> None:
        ...
