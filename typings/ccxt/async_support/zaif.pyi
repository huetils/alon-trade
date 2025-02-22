"""
This type stub file was generated by pyright.
"""

from typing import List

from ccxt.abstract.zaif import ImplicitAPI
from ccxt.async_support.base.exchange import Exchange
from ccxt.base.types import (
    Balances,
    Currency,
    Int,
    Market,
    Num,
    Order,
    OrderBook,
    OrderSide,
    OrderType,
    Str,
    Ticker,
    Trade,
    Transaction,
)

class zaif(Exchange, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    async def fetch_markets(self, params=...) -> List[Market]:
        """

        https://zaif-api-document.readthedocs.io/ja/latest/PublicAPI.html#id12

        retrieves data on all markets for zaif
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...

    def parse_market(self, market: dict) -> Market: ...
    def parse_balance(self, response) -> Balances: ...
    async def fetch_balance(self, params=...) -> Balances:
        """

        https://zaif-api-document.readthedocs.io/ja/latest/TradingAPI.html#id10

        query for balance and get the amount of funds available for trading or funds locked in orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    async def fetch_order_book(
        self, symbol: str, limit: Int = ..., params=...
    ) -> OrderBook:
        """

        https://zaif-api-document.readthedocs.io/ja/latest/PublicAPI.html#id34

        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker: ...
    async def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """

        https://zaif-api-document.readthedocs.io/ja/latest/PublicAPI.html#id22

        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market
        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def parse_trade(self, trade: dict, market: Market = ...) -> Trade: ...
    async def fetch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """

        https://zaif-api-document.readthedocs.io/ja/latest/PublicAPI.html#id28

        get the list of most recent trades for a particular symbol
        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    async def create_order(
        self,
        symbol: str,
        type: OrderType,
        side: OrderSide,
        amount: float,
        price: Num = ...,
        params=...,
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        """

        https://zaif-api-document.readthedocs.io/ja/latest/MarginTradingAPI.html#id23

        create a trade order
        :param str symbol: unified symbol of the market to create an order in
        :param str type: must be 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def cancel_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """

        https://zaif-api-document.readthedocs.io/ja/latest/TradingAPI.html#id37

        cancels an open order
        :param str id: order id
        :param str symbol: not used by zaif cancelOrder()
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def parse_order(self, order: dict, market: Market = ...) -> Order: ...
    async def fetch_open_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """

        https://zaif-api-document.readthedocs.io/ja/latest/MarginTradingAPI.html#id28

        fetch all unfilled currently open orders
        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_closed_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """

        https://zaif-api-document.readthedocs.io/ja/latest/TradingAPI.html#id24

        fetches information on multiple closed orders made by the user
        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def withdraw(
        self, code: str, amount: float, address: str, tag=..., params=...
    ) -> Transaction:
        """

        https://zaif-api-document.readthedocs.io/ja/latest/TradingAPI.html#id41

        make a withdrawal
        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str tag:
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def parse_transaction(
        self, transaction: dict, currency: Currency = ...
    ) -> Transaction: ...
    def custom_nonce(self):  # -> str:
        ...
    def sign(
        self, path, api=..., method=..., params=..., headers=..., body=...
    ):  # -> dict[str, Any]:
        ...
    def handle_errors(
        self,
        httpCode: int,
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
