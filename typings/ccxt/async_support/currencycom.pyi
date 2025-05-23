"""
This type stub file was generated by pyright.
"""

from typing import List

from ccxt.abstract.currencycom import ImplicitAPI
from ccxt.async_support.base.exchange import Exchange
from ccxt.base.types import (
    Account,
    Balances,
    Currencies,
    Currency,
    DepositAddress,
    Int,
    LedgerEntry,
    Leverage,
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
    TradingFees,
    Transaction,
)

class currencycom(Exchange, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    def nonce(self): ...
    async def fetch_time(self, params=...):  # -> int | None:
        """
        fetches the current integer timestamp in milliseconds from the exchange server

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/timeUsingGET

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int: the current integer timestamp in milliseconds from the exchange server
        """
        ...

    async def fetch_currencies(self, params=...) -> Currencies:
        """
        fetches all available currencies on an exchange

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/getCurrenciesUsingGET

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an associative dictionary of currencies
        """
        ...

    async def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for currencycom

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/exchangeInfoUsingGET

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...

    async def fetch_accounts(self, params=...) -> List[Account]:
        """
        fetch all the accounts associated with a profile

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/accountUsingGET

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `account structures <https://docs.ccxt.com/#/?id=account-structure>` indexed by the account type
        """
        ...

    async def fetch_trading_fees(self, params=...) -> TradingFees:
        """
        fetch the trading fees for multiple markets

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/accountUsingGET

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `fee structures <https://docs.ccxt.com/#/?id=fee-structure>` indexed by market symbols
        """
        ...

    def parse_balance(self, response, type=...):  # -> dict[Any, Any]:
        ...
    async def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/accountUsingGET

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    async def fetch_order_book(
        self, symbol: str, limit: Int = ..., params=...
    ) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/depthUsingGET

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

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/ticker_24hrUsingGET

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    async def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/ticker_24hrUsingGET

        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def parse_ohlcv(self, ohlcv, market: Market = ...) -> list: ...
    async def fetch_ohlcv(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[list]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/klinesUsingGET

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...

    def parse_trade(self, trade: dict, market: Market = ...) -> Trade: ...
    async def fetch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/aggTradesUsingGET

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    def parse_order(self, order: dict, market: Market = ...) -> Order: ...
    def parse_order_status(self, status: Str):  # -> str | None:
        ...
    def parse_order_type(self, status):  # -> str | None:
        ...
    def parse_order_time_in_force(self, status):  # -> str | None:
        ...
    def parse_order_side(self, status):  # -> str | None:
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

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/orderUsingPOST

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """
        fetches information on an order made by the user

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/getOrderUsingGET

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

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/openOrdersUsingGET

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def cancel_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """
        cancels an open order

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/cancelOrderUsingDELETE

        :param str id: order id
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

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/myTradesUsingGET

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    async def fetch_deposits(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
        fetch all deposits made to an account

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/getDepositsUsingGET

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

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/getWithdrawalsUsingGET

        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch withdrawals for
        :param int [limit]: the maximum number of withdrawals structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    async def fetch_deposits_withdrawals(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
        fetch history of deposits and withdrawals

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/getTransactionsUsingGET

        :param str [code]: unified currency code for the currency of the deposit/withdrawals, default is None
        :param int [since]: timestamp in ms of the earliest deposit/withdrawal, default is None
        :param int [limit]: max number of deposit/withdrawals to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a list of `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    async def fetch_transactions_by_method(
        self, method, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        ...
    def parse_transaction(
        self, transaction: dict, currency: Currency = ...
    ) -> Transaction: ...
    def parse_transaction_status(self, status: Str):  # -> str | None:
        ...
    def parse_transaction_type(self, type):  # -> str | None:
        ...
    async def fetch_ledger(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[LedgerEntry]:
        """
        fetch the history of changes, actions done by the user or operations that altered the balance of the user

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/getLedgerUsingGET

        :param str [code]: unified currency code, default is None
        :param int [since]: timestamp in ms of the earliest ledger entry, default is None
        :param int [limit]: max number of ledger entries to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ledger structure <https://docs.ccxt.com/#/?id=ledger>`
        """
        ...

    def parse_ledger_entry(
        self, item: dict, currency: Currency = ...
    ) -> LedgerEntry: ...
    def parse_ledger_entry_status(self, status):  # -> str | None:
        ...
    def parse_ledger_entry_type(self, type):  # -> str | None:
        ...
    async def fetch_leverage(self, symbol: str, params=...) -> Leverage:
        """
        fetch the set leverage for a market

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/leverageSettingsUsingGET

        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `leverage structure <https://docs.ccxt.com/#/?id=leverage-structure>`
        """
        ...

    def parse_leverage(self, leverage: dict, market: Market = ...) -> Leverage: ...
    async def fetch_deposit_address(self, code: str, params=...) -> DepositAddress:
        """
        fetch the deposit address for a currency associated with self account

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/getDepositAddressUsingGET

        :param str code: unified currency code
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...

    def parse_deposit_address(
        self, depositAddress, currency: Currency = ...
    ) -> DepositAddress: ...
    def sign(
        self, path, api=..., method=..., params=..., headers=..., body=...
    ):  # -> dict[str, Any]:
        ...
    async def fetch_positions(
        self, symbols: Strings = ..., params=...
    ):  # -> dict[Any, Any] | list[Any]:
        """
        fetch all open positions

        https://apitradedoc.currency.com/swagger-ui.html#/rest-api/tradingPositionsUsingGET

        :param str[]|None symbols: list of unified market symbols
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `position structure <https://docs.ccxt.com/#/?id=position-structure>`
        """
        ...

    def parse_position(
        self, position: dict, market: Market = ...
    ):  # -> dict[Any, Any]:
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
