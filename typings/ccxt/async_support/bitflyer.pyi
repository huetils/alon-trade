"""
This type stub file was generated by pyright.
"""

from typing import List

from ccxt.abstract.bitflyer import ImplicitAPI
from ccxt.async_support.base.exchange import Exchange
from ccxt.base.types import (
    Balances,
    Currency,
    FundingRate,
    Int,
    Market,
    MarketInterface,
    Num,
    Order,
    OrderBook,
    OrderSide,
    OrderType,
    Str,
    Strings,
    Ticker,
    Trade,
    TradingFeeInterface,
    Transaction,
)

class bitflyer(Exchange, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    def parse_expiry_date(self, expiry):  # -> int | None:
        ...
    def safe_market(
        self,
        marketId: Str = ...,
        market: Market = ...,
        delimiter: Str = ...,
        marketType: Str = ...,
    ) -> MarketInterface: ...
    async def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for bitflyer

        https://lightning.bitflyer.com/docs?lang=en#market-list

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...

    def parse_balance(self, response) -> Balances: ...
    async def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://lightning.bitflyer.com/docs?lang=en#get-account-asset-balance

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    async def fetch_order_book(
        self, symbol: str, limit: Int = ..., params=...
    ) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://lightning.bitflyer.com/docs?lang=en#order-book

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker: ...
    async def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://lightning.bitflyer.com/docs?lang=en#ticker

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
        get the list of most recent trades for a particular symbol

        https://lightning.bitflyer.com/docs?lang=en#list-executions

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    async def fetch_trading_fee(self, symbol: str, params=...) -> TradingFeeInterface:
        """
        fetch the trading fees for a market

        https://lightning.bitflyer.com/docs?lang=en#get-trading-commission

        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `fee structure <https://docs.ccxt.com/#/?id=fee-structure>`
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
        create a trade order

        https://lightning.bitflyer.com/docs?lang=en#send-a-new-order

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def cancel_order(
        self, id: str, symbol: Str = ..., params=...
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        """
        cancels an open order

        https://lightning.bitflyer.com/docs?lang=en#cancel-order

        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def parse_order_status(self, status: Str):  # -> str | None:
        ...
    def parse_order(self, order: dict, market: Market = ...) -> Order: ...
    async def fetch_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetches information on multiple orders made by the user

        https://lightning.bitflyer.com/docs?lang=en#list-orders

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_open_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://lightning.bitflyer.com/docs?lang=en#list-orders

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
        fetches information on multiple closed orders made by the user

        https://lightning.bitflyer.com/docs?lang=en#list-orders

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_order(self, id: str, symbol: Str = ..., params=...):
        """
        fetches information on an order made by the user

        https://lightning.bitflyer.com/docs?lang=en#list-orders

        :param str id: the order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        fetch all trades made by the user

        https://lightning.bitflyer.com/docs?lang=en#list-executions

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    async def fetch_positions(self, symbols: Strings = ..., params=...):  # -> Any:
        """
        fetch all open positions

        https://lightning.bitflyer.com/docs?lang=en#get-open-interest-summary

        :param str[] symbols: list of unified market symbols
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `position structure <https://docs.ccxt.com/#/?id=position-structure>`
        """
        ...

    async def withdraw(
        self, code: str, amount: float, address: str, tag=..., params=...
    ) -> Transaction:
        """
        make a withdrawal

        https://lightning.bitflyer.com/docs?lang=en#withdrawing-funds

        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str tag:
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    async def fetch_deposits(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
        fetch all deposits made to an account

        https://lightning.bitflyer.com/docs?lang=en#get-crypto-assets-deposit-history

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

        https://lightning.bitflyer.com/docs?lang=en#get-crypto-assets-transaction-history

        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch withdrawals for
        :param int [limit]: the maximum number of withdrawals structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def parse_deposit_status(self, status):  # -> str | None:
        ...
    def parse_withdrawal_status(self, status):  # -> str | None:
        ...
    def parse_transaction(
        self, transaction: dict, currency: Currency = ...
    ) -> Transaction: ...
    async def fetch_funding_rate(self, symbol: str, params=...) -> FundingRate:
        """
        fetch the current funding rate

        https://lightning.bitflyer.com/docs#funding-rate

        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `funding rate structure <https://docs.ccxt.com/#/?id=funding-rate-structure>`
        """
        ...

    def parse_funding_rate(self, contract, market: Market = ...) -> FundingRate: ...
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
