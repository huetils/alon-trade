"""
This type stub file was generated by pyright.
"""

from typing import List

from ccxt.abstract.alpaca import ImplicitAPI
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

class alpaca(Exchange, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    async def fetch_time(self, params=...):  # -> float | int:
        """
        fetches the current integer timestamp in milliseconds from the exchange server
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int: the current integer timestamp in milliseconds from the exchange server
        """
        ...

    async def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for alpaca

        https://docs.alpaca.markets/reference/get-v2-assets

        :param dict [params]: extra parameters specific to the exchange api endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...

    def parse_market(self, asset) -> Market: ...
    async def fetch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://docs.alpaca.markets/reference/cryptotrades
        https://docs.alpaca.markets/reference/cryptolatesttrades

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.loc]: crypto location, default: us
        :param str [params.method]: method, default: marketPublicGetV1beta3CryptoLocTrades
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    async def fetch_order_book(
        self, symbol: str, limit: Int = ..., params=...
    ) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://docs.alpaca.markets/reference/cryptolatestorderbooks

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.loc]: crypto location, default: us
        :returns dict: A dictionary of `order book structures <https://github.com/ccxt/ccxt/wiki/Manual#order-book-structure>` indexed by market symbols
        """
        ...

    async def fetch_ohlcv(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[list]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://docs.alpaca.markets/reference/cryptobars
        https://docs.alpaca.markets/reference/cryptolatestbars

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the alpha api endpoint
        :param str [params.loc]: crypto location, default: us
        :param str [params.method]: method, default: marketPublicGetV1beta3CryptoLocBars
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...

    def parse_ohlcv(self, ohlcv, market: Market = ...) -> list: ...
    async def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://docs.alpaca.markets/reference/cryptosnapshots-1

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.loc]: crypto location, default: us
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    async def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://docs.alpaca.markets/reference/cryptosnapshots-1

        :param str[] symbols: unified symbols of the markets to fetch tickers for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.loc]: crypto location, default: us
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def generate_client_order_id(self, params):  # -> str | None:
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

        https://docs.alpaca.markets/reference/postorder

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market', 'limit' or 'stop_limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param float [params.triggerPrice]: The price at which a trigger order is triggered at
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def cancel_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """
        cancels an open order

        https://docs.alpaca.markets/reference/deleteorderbyorderid

        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def cancel_all_orders(
        self, symbol: Str = ..., params=...
    ):  # -> list[Any] | list[object] | list[OrderedDict[Any, Any] | dict[Any, Any]]:
        """
        cancel all open orders in a market

        https://docs.alpaca.markets/reference/deleteallorders

        :param str symbol: alpaca cancelAllOrders cannot setting symbol, it will cancel all open orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """
        fetches information on an order made by the user

        https://docs.alpaca.markets/reference/getorderbyorderid

        :param str id: the order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetches information on multiple orders made by the user

        https://docs.alpaca.markets/reference/getallorders

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: the latest time in ms to fetch orders for
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_open_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://docs.alpaca.markets/reference/getallorders

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: the latest time in ms to fetch orders for
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_closed_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetches information on multiple closed orders made by the user

        https://docs.alpaca.markets/reference/getallorders

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: the latest time in ms to fetch orders for
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def edit_order(
        self,
        id: str,
        symbol: str,
        type: OrderType,
        side: OrderSide,
        amount: Num = ...,
        price: Num = ...,
        params=...,
    ):  # -> Order:
        """
        edit a trade order

        https://docs.alpaca.markets/reference/patchorderbyorderid-1

        :param str id: order id
        :param str [symbol]: unified symbol of the market to create an order in
        :param str [type]: 'market', 'limit' or 'stop_limit'
        :param str [side]: 'buy' or 'sell'
        :param float [amount]: how much of the currency you want to trade in units of the base currency
        :param float [price]: the price for the order, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.triggerPrice]: the price to trigger a stop order
        :param str [params.timeInForce]: for crypto trading either 'gtc' or 'ioc' can be used
        :param str [params.clientOrderId]: a unique identifier for the order, automatically generated if not sent
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def parse_order(self, order: dict, market: Market = ...) -> Order: ...
    def parse_order_status(self, status: Str):  # -> str | None:
        ...
    def parse_time_in_force(self, timeInForce: Str):  # -> str | None:
        ...
    async def fetch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        fetch all trades made by the user

        https://docs.alpaca.markets/reference/getaccountactivitiesbyactivitytype-1

        :param str [symbol]: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trade structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: the latest time in ms to fetch trades for
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    def parse_trade(self, trade: dict, market: Market = ...) -> Trade: ...
    async def fetch_deposit_address(self, code: str, params=...) -> DepositAddress:
        """
        fetch the deposit address for a currency associated with self account

        https://docs.alpaca.markets/reference/listcryptofundingwallets

        :param str code: unified currency code
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...

    def parse_deposit_address(
        self, depositAddress, currency: Currency = ...
    ) -> DepositAddress: ...
    async def withdraw(
        self, code: str, amount: float, address: str, tag=..., params=...
    ) -> Transaction:
        """
        make a withdrawal

        https://docs.alpaca.markets/reference/createcryptotransferforaccount

        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str tag: a memo for the transaction
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    async def fetch_transactions_helper(
        self, type, code, since, limit, params
    ):  # -> list[Any] | list[object]:
        ...
    async def fetch_deposits_withdrawals(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
        fetch history of deposits and withdrawals

        https://docs.alpaca.markets/reference/listcryptofundingtransfers

        :param str [code]: unified currency code for the currency of the deposit/withdrawals, default is None
        :param int [since]: timestamp in ms of the earliest deposit/withdrawal, default is None
        :param int [limit]: max number of deposit/withdrawals to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a list of `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    async def fetch_deposits(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
        fetch all deposits made to an account

        https://docs.alpaca.markets/reference/listcryptofundingtransfers

        :param str [code]: unified currency code
        :param int [since]: the earliest time in ms to fetch deposits for
        :param int [limit]: the maximum number of deposit structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    async def fetch_withdrawals(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
        fetch all withdrawals made from an account

        https://docs.alpaca.markets/reference/listcryptofundingtransfers

        :param str [code]: unified currency code
        :param int [since]: the earliest time in ms to fetch withdrawals for
        :param int [limit]: the maximum number of withdrawal structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def parse_transaction(
        self, transaction: dict, currency: Currency = ...
    ) -> Transaction: ...
    def parse_transaction_status(self, status: Str):  # -> str | None:
        ...
    def parse_transaction_type(self, type):  # -> str | None:
        ...
    async def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://docs.alpaca.markets/reference/getaccount-1

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    def parse_balance(self, response) -> Balances: ...
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
