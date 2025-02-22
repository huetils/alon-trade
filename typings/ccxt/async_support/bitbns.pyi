"""
This type stub file was generated by pyright.
"""

from typing import List

from ccxt.abstract.bitbns import ImplicitAPI
from ccxt.async_support.base.exchange import Exchange
from ccxt.base.types import (
    Balances,
    Currency,
    DepositAddress,
    Int,
    Market,
    Num,
    Order,
    OrderBook,
    OrderSide,
    OrderType,
    Str,
    Strings,
    Ticker,
    Tickers,
    Trade,
    Transaction,
)

class bitbns(Exchange, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    async def fetch_status(self, params=...):  # -> dict[str, Any]:
        """
        the latest known information on the availability of the exchange API
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `status structure <https://docs.ccxt.com/#/?id=exchange-status-structure>`
        """
        ...

    async def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for bitbns
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...

    async def fetch_order_book(
        self, symbol: str, limit: Int = ..., params=...
    ) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker: ...
    async def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market
        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def parse_balance(self, response) -> Balances: ...
    async def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    def parse_status(self, status):  # -> str | None:
        ...
    def parse_order(self, order: dict, market: Market = ...) -> Order: ...
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

               https://docs.bitbns.com/bitbns/rest-endpoints/order-apis/version-2/place-orders
               https://docs.bitbns.com/bitbns/rest-endpoints/order-apis/version-1/market-orders-quantity  # market orders

               :param str symbol: unified symbol of the market to create an order in
               :param str type: 'market' or 'limit'
               :param str side: 'buy' or 'sell'
               :param float amount: how much of currency you want to trade in units of base currency
               :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
               :param dict [params]: extra parameters specific to the exchange API endpoint
               :param float [params.triggerPrice]: the price at which a trigger order is triggered at

        EXCHANGE SPECIFIC PARAMETERS
               :param float [params.target_rate]: *requires params.trail_rate when set, type must be 'limit'* a bracket order is placed when set
               :param float [params.trail_rate]: *requires params.target_rate when set, type must be 'limit'* a bracket order is placed when set
               :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def cancel_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """
        cancels an open order

        https://docs.bitbns.com/bitbns/rest-endpoints/order-apis/version-2/cancel-orders
        https://docs.bitbns.com/bitbns/rest-endpoints/order-apis/version-1/cancel-stop-loss-orders

        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.trigger]: True if cancelling a trigger order
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """
        fetches information on an order made by the user

        https://docs.bitbns.com/bitbns/rest-endpoints/order-apis/version-1/order-status

        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_open_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://docs.bitbns.com/bitbns/rest-endpoints/order-apis/version-2/order-status-limit
        https://docs.bitbns.com/bitbns/rest-endpoints/order-apis/version-2/order-status-limit/order-status-stop-limit

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of open orders structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.trigger]: True if fetching trigger orders
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def parse_trade(self, trade: dict, market: Market = ...) -> Trade: ...
    async def fetch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        fetch all trades made by the user
        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    async def fetch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol
        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    async def fetch_deposits(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
        fetch all deposits made to an account
        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch deposits for
        :param int [limit]: the maximum number of deposits structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    async def fetch_withdrawals(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
        fetch all withdrawals made from an account
        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch withdrawals for
        :param int [limit]: the maximum number of withdrawals structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def parse_transaction_status_by_type(self, status, type=...):  # -> str | None:
        ...
    def parse_transaction(
        self, transaction: dict, currency: Currency = ...
    ) -> Transaction: ...
    async def fetch_deposit_address(self, code: str, params=...) -> DepositAddress:
        """
        fetch the deposit address for a currency associated with self account
        :param str code: unified currency code
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...

    def nonce(self):  # -> int:
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
