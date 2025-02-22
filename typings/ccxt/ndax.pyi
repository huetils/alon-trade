"""
This type stub file was generated by pyright.
"""

from typing import List

from ccxt.abstract.ndax import ImplicitAPI
from ccxt.base.exchange import Exchange
from ccxt.base.types import (
    Account,
    Balances,
    Currencies,
    Currency,
    DepositAddress,
    IndexType,
    Int,
    LedgerEntry,
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

class ndax(Exchange, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    def sign_in(self, params=...):  # -> Any:
        """
        sign in, must be called prior to using other authenticated methods

        https://apidoc.ndax.io/#authenticate2fa

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns: response from exchange
        """
        ...

    def fetch_currencies(self, params=...) -> Currencies:
        """
        fetches all available currencies on an exchange

        https://apidoc.ndax.io/#getproduct

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an associative dictionary of currencies
        """
        ...

    def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for ndax

        https://apidoc.ndax.io/#getinstruments

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...

    def parse_market(self, market: dict) -> Market: ...
    def parse_order_book(
        self,
        orderbook,
        symbol,
        timestamp=...,
        bidsKey=...,
        asksKey=...,
        priceKey: IndexType = ...,
        amountKey: IndexType = ...,
        countOrIdKey: IndexType = ...,
    ):  # -> dict[Any, Any]:
        ...
    def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://apidoc.ndax.io/#getl2snapshot

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

        https://apidoc.ndax.io/#getlevel1

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def parse_ohlcv(self, ohlcv, market: Market = ...) -> list: ...
    def fetch_ohlcv(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[list]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://apidoc.ndax.io/#gettickerhistory

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...

    def parse_trade(self, trade: dict, market: Market = ...) -> Trade: ...
    def fetch_trades(
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

    def fetch_accounts(self, params=...) -> List[Account]:
        """
        fetch all the accounts associated with a profile

        https://apidoc.ndax.io/#getuseraccounts

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `account structures <https://docs.ccxt.com/#/?id=account-structure>` indexed by the account type
        """
        ...

    def parse_balance(self, response) -> Balances: ...
    def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://apidoc.ndax.io/#getaccountpositions

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    def parse_ledger_entry_type(self, type):  # -> str | None:
        ...
    def parse_ledger_entry(
        self, item: dict, currency: Currency = ...
    ) -> LedgerEntry: ...
    def fetch_ledger(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[LedgerEntry]:
        """
        fetch the history of changes, actions done by the user or operations that altered the balance of the user

        https://apidoc.ndax.io/#getaccounttransactions

        :param str [code]: unified currency code, default is None
        :param int [since]: timestamp in ms of the earliest ledger entry, default is None
        :param int [limit]: max number of ledger entries to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ledger structure <https://docs.ccxt.com/#/?id=ledger>`
        """
        ...

    def parse_order_status(self, status: Str):  # -> str | None:
        ...
    def parse_order(self, order: dict, market: Market = ...) -> Order: ...
    def create_order(
        self,
        symbol: str,
        type: OrderType,
        side: OrderSide,
        amount: float,
        price: Num = ...,
        params=...,
    ):
        """
        create a trade order

        https://apidoc.ndax.io/#sendorder

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param float [params.triggerPrice]: the price at which a trigger order would be triggered
        :param str [params.clientOrderId]: a unique id for the order
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def edit_order(
        self,
        id: str,
        symbol: str,
        type: OrderType,
        side: OrderSide,
        amount: Num = ...,
        price: Num = ...,
        params=...,
    ): ...
    def fetch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):
        """
        fetch all trades made by the user

        https://apidoc.ndax.io/#gettradeshistory

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    def cancel_all_orders(self, symbol: Str = ..., params=...):
        """
        cancel all open orders

        https://apidoc.ndax.io/#cancelallorders

        :param str symbol: unified market symbol, only orders in the market of self symbol are cancelled when symbol is not None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def cancel_order(self, id: str, symbol: Str = ..., params=...):
        """
        cancels an open order

        https://apidoc.ndax.io/#cancelorder

        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.clientOrderId]: a unique id for the order
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_open_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://apidoc.ndax.io/#getopenorders

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetches information on multiple orders made by the user

        https://apidoc.ndax.io/#getorderhistory

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_order(self, id: str, symbol: Str = ..., params=...):
        """
        fetches information on an order made by the user

        https://apidoc.ndax.io/#getorderstatus

        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_order_trades(
        self, id: str, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):
        """
        fetch all the trades made from a single order

        https://apidoc.ndax.io/#getorderhistorybyorderid

        :param str id: order id
        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    def fetch_deposit_address(self, code: str, params=...) -> DepositAddress:
        """
        fetch the deposit address for a currency associated with self account
        :param str code: unified currency code
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...

    def parse_deposit_address(
        self, depositAddress, currency: Currency = ...
    ) -> DepositAddress: ...
    def create_deposit_address(self, code: str, params=...):  # -> DepositAddress:
        """
        create a currency deposit address
        :param str code: unified currency code of the currency for the deposit address
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...

    def fetch_deposits(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
        fetch all deposits made to an account

        https://apidoc.ndax.io/#getdeposits

        :param str code: unified currency code
        :param int [since]: not used by ndax fetchDeposits
        :param int [limit]: the maximum number of deposits structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def fetch_withdrawals(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
        fetch all withdrawals made from an account

        https://apidoc.ndax.io/#getwithdraws

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
    def withdraw(
        self, code: str, amount: float, address: str, tag=..., params=...
    ) -> Transaction:
        """
        make a withdrawal
        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str tag:
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
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
