"""
This type stub file was generated by pyright.
"""

from typing import List

from ccxt.abstract.latoken import ImplicitAPI
from ccxt.base.exchange import Exchange
from ccxt.base.types import (
    Balances,
    Currencies,
    Currency,
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
    TradingFeeInterface,
    Transaction,
    TransferEntry,
)

class latoken(Exchange, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    def nonce(self): ...
    def fetch_time(self, params=...):  # -> int | None:
        """
        fetches the current integer timestamp in milliseconds from the exchange server

        https://api.latoken.com/doc/v2/#tag/Time/operation/currentTime

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int: the current integer timestamp in milliseconds from the exchange server
        """
        ...

    def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for latoken

        https://api.latoken.com/doc/v2/#tag/Pair/operation/getActivePairs

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...

    def fetch_currencies_from_cache(self, params=...):  # -> None:
        ...
    def fetch_currencies(self, params=...) -> Currencies:
        """
        fetches all available currencies on an exchange
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an associative dictionary of currencies
        """
        ...

    def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://api.latoken.com/doc/v2/#tag/Account/operation/getBalancesByUser

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://api.latoken.com/doc/v2/#tag/Order-Book/operation/getOrderBook

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker: ...
    def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://api.latoken.com/doc/v2/#tag/Ticker/operation/getTicker

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://api.latoken.com/doc/v2/#tag/Ticker/operation/getAllTickers

        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def parse_trade(self, trade: dict, market: Market = ...) -> Trade: ...
    def fetch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://api.latoken.com/doc/v2/#tag/Trade/operation/getTradesByPair

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    def fetch_trading_fee(self, symbol: str, params=...) -> TradingFeeInterface:
        """
        fetch the trading fees for a market

        https://api.latoken.com/doc/v2/#tag/Trade/operation/getFeeByPair
        https://api.latoken.com/doc/v2/#tag/Trade/operation/getAuthFeeByPair

        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `fee structure <https://docs.ccxt.com/#/?id=fee-structure>`
        """
        ...

    def fetch_public_trading_fee(self, symbol: str, params=...):  # -> dict[str, Any]:
        ...
    def fetch_private_trading_fee(self, symbol: str, params=...):  # -> dict[str, Any]:
        ...
    def fetch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        fetch all trades made by the user

        https://api.latoken.com/doc/v2/#tag/Trade/operation/getTradesByTrader
        https://api.latoken.com/doc/v2/#tag/Trade/operation/getTradesByAssetAndTrader

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    def parse_order_status(self, status: Str):  # -> str | None:
        ...
    def parse_order_type(self, status):  # -> str | None:
        ...
    def parse_time_in_force(self, timeInForce: Str):  # -> str | None:
        ...
    def parse_order(self, order: dict, market: Market = ...) -> Order: ...
    def fetch_open_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://api.latoken.com/doc/v2/#tag/Order/operation/getMyActiveOrdersByPair
        https://api.latoken.com/doc/v2/#tag/StopOrder/operation/getMyActiveStopOrdersByPair  # stop

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.trigger]: True if fetching trigger orders
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetches information on multiple orders made by the user

        https://api.latoken.com/doc/v2/#tag/Order/operation/getMyOrders
        https://api.latoken.com/doc/v2/#tag/Order/operation/getMyOrdersByPair
        https://api.latoken.com/doc/v2/#tag/StopOrder/operation/getMyStopOrders       # stop
        https://api.latoken.com/doc/v2/#tag/StopOrder/operation/getMyStopOrdersByPair  # stop

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.trigger]: True if fetching trigger orders
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """
        fetches information on an order made by the user

        https://api.latoken.com/doc/v2/#tag/Order/operation/getOrderById
        https://api.latoken.com/doc/v2/#tag/StopOrder/operation/getStopOrderById

        :param str id: order id
        :param str [symbol]: not used by latoken fetchOrder
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.trigger]: True if fetching a trigger order
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def create_order(
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

               https://api.latoken.com/doc/v2/#tag/Order/operation/placeOrder
               https://api.latoken.com/doc/v2/#tag/StopOrder/operation/placeStopOrder  # stop

               :param str symbol: unified symbol of the market to create an order in
               :param str type: 'market' or 'limit'
               :param str side: 'buy' or 'sell'
               :param float amount: how much of currency you want to trade in units of base currency
               :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
               :param dict [params]: extra parameters specific to the exchange API endpoint
               :param float [params.triggerPrice]: the price at which a trigger order is triggered at

        EXCHANGE SPECIFIC PARAMETERS
               :param str [params.condition]: "GTC", "IOC", or  "FOK"
               :param str [params.clientOrderId]: [0 .. 50] characters, client's custom order id(free field for your convenience)
               :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def cancel_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """
        cancels an open order

        https://api.latoken.com/doc/v2/#tag/Order/operation/cancelOrder
        https://api.latoken.com/doc/v2/#tag/StopOrder/operation/cancelStopOrder  # stop

        :param str id: order id
        :param str symbol: not used by latoken cancelOrder()
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.trigger]: True if cancelling a trigger order
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def cancel_all_orders(
        self, symbol: Str = ..., params=...
    ):  # -> list[OrderedDict[Any, Any] | dict[Any, Any]]:
        """
        cancel all open orders in a market

        https://api.latoken.com/doc/v2/#tag/Order/operation/cancelAllOrders
        https://api.latoken.com/doc/v2/#tag/Order/operation/cancelAllOrdersByPair

        :param str symbol: unified market symbol of the market to cancel orders in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.trigger]: True if cancelling trigger orders
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_transactions(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        @deprecated
               use fetchDepositsWithdrawals instead

               https://api.latoken.com/doc/v2/#tag/Transaction/operation/getUserTransactions

               :param str code: unified currency code for the currency of the transactions, default is None
               :param int [since]: timestamp in ms of the earliest transaction, default is None
               :param int [limit]: max number of transactions to return, default is None
               :param dict [params]: extra parameters specific to the exchange API endpoint
               :returns dict: a list of `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def parse_transaction(
        self, transaction: dict, currency: Currency = ...
    ) -> Transaction: ...
    def parse_transaction_status(self, status: Str):  # -> str | None:
        ...
    def parse_transaction_type(self, type):  # -> str | None:
        ...
    def fetch_transfers(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[TransferEntry]:
        """
        fetch a history of internal transfers made on an account

        https://api.latoken.com/doc/v2/#tag/Transfer/operation/getUsersTransfers

        :param str code: unified currency code of the currency transferred
        :param int [since]: the earliest time in ms to fetch transfers for
        :param int [limit]: the maximum number of  transfers structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transfer structures <https://docs.ccxt.com/#/?id=transfer-structure>`
        """
        ...

    def transfer(
        self, code: str, amount: float, fromAccount: str, toAccount: str, params=...
    ) -> TransferEntry:
        """
        transfer currency internally between wallets on the same account

        https://api.latoken.com/doc/v2/#tag/Transfer/operation/transferByEmail
        https://api.latoken.com/doc/v2/#tag/Transfer/operation/transferById
        https://api.latoken.com/doc/v2/#tag/Transfer/operation/transferByPhone

        :param str code: unified currency code
        :param float amount: amount to transfer
        :param str fromAccount: account to transfer from
        :param str toAccount: account to transfer to
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transfer structure <https://docs.ccxt.com/#/?id=transfer-structure>`
        """
        ...

    def parse_transfer(
        self, transfer: dict, currency: Currency = ...
    ) -> TransferEntry: ...
    def parse_transfer_status(self, status: Str) -> Str: ...
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
