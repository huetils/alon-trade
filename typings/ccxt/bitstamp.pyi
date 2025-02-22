"""
This type stub file was generated by pyright.
"""

from typing import List

from ccxt.abstract.bitstamp import ImplicitAPI
from ccxt.base.exchange import Exchange
from ccxt.base.types import (
    Balances,
    Currencies,
    Currency,
    DepositAddress,
    Int,
    LedgerEntry,
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
    TradingFees,
    Transaction,
    TransferEntry,
)

class bitstamp(Exchange, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for bitstamp

        https://www.bitstamp.net/api/#tag/Market-info/operation/GetTradingPairsInfo

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...

    def construct_currency_object(
        self, id, code, name, precision, minCost, originalPayload
    ):  # -> dict[str, Any]:
        ...
    def fetch_markets_from_cache(self, params=...):  # -> None:
        ...
    def fetch_currencies(self, params=...) -> Currencies:
        """
        fetches all available currencies on an exchange

        https://www.bitstamp.net/api/#tag/Market-info/operation/GetTradingPairsInfo

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an associative dictionary of currencies
        """
        ...

    def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://www.bitstamp.net/api/#tag/Order-book/operation/GetOrderBook

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

        https://www.bitstamp.net/api/#tag/Tickers/operation/GetMarketTicker

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://www.bitstamp.net/api/#tag/Tickers/operation/GetCurrencyPairTickers

        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def get_currency_id_from_transaction(self, transaction):  # -> str | None:
        ...
    def get_market_from_trade(
        self, trade
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any] | MarketInterface | None:
        ...
    def parse_trade(self, trade: dict, market: Market = ...) -> Trade: ...
    def fetch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://www.bitstamp.net/api/#tag/Transactions-public/operation/GetTransactions

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    def parse_ohlcv(self, ohlcv, market: Market = ...) -> list: ...
    def fetch_ohlcv(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[list]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://www.bitstamp.net/api/#tag/Market-info/operation/GetOHLCData

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...

    def parse_balance(self, response) -> Balances: ...
    def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://www.bitstamp.net/api/#tag/Account-balances/operation/GetAccountBalances

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    def fetch_trading_fee(self, symbol: str, params=...) -> TradingFeeInterface:
        """
        fetch the trading fees for a market

        https://www.bitstamp.net/api/#tag/Fees/operation/GetTradingFeesForCurrency

        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `fee structure <https://docs.ccxt.com/#/?id=fee-structure>`
        """
        ...

    def parse_trading_fee(
        self, fee: dict, market: Market = ...
    ) -> TradingFeeInterface: ...
    def parse_trading_fees(self, fees):  # -> dict[Any, Any]:
        ...
    def fetch_trading_fees(self, params=...) -> TradingFees:
        """
        fetch the trading fees for multiple markets

        https://www.bitstamp.net/api/#tag/Fees/operation/GetAllTradingFees

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `fee structures <https://docs.ccxt.com/#/?id=fee-structure>` indexed by market symbols
        """
        ...

    def fetch_transaction_fees(
        self, codes: Strings = ..., params=...
    ):  # -> dict[Any, Any]:
        """
        @deprecated
               please use fetchDepositWithdrawFees instead

               https://www.bitstamp.net/api/#tag/Fees

               :param str[]|None codes: list of unified currency codes
               :param dict [params]: extra parameters specific to the exchange API endpoint
               :returns dict[]: a list of `fee structures <https://docs.ccxt.com/#/?id=fee-structure>`
        """
        ...

    def parse_transaction_fees(self, response, codes=...):  # -> dict[Any, Any]:
        ...
    def fetch_deposit_withdraw_fees(self, codes=..., params=...):  # -> dict[Any, Any]:
        """
        fetch deposit and withdraw fees

        https://www.bitstamp.net/api/#tag/Fees/operation/GetAllWithdrawalFees

        :param str[]|None codes: list of unified currency codes
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `fee structures <https://docs.ccxt.com/#/?id=fee-structure>`
        """
        ...

    def parse_deposit_withdraw_fee(self, fee, currency=...):  # -> dict[str, Any]:
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

        https://www.bitstamp.net/api/#tag/Orders/operation/OpenInstantBuyOrder
        https://www.bitstamp.net/api/#tag/Orders/operation/OpenMarketBuyOrder
        https://www.bitstamp.net/api/#tag/Orders/operation/OpenLimitBuyOrder
        https://www.bitstamp.net/api/#tag/Orders/operation/OpenInstantSellOrder
        https://www.bitstamp.net/api/#tag/Orders/operation/OpenMarketSellOrder
        https://www.bitstamp.net/api/#tag/Orders/operation/OpenLimitSellOrder

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def cancel_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """
        cancels an open order

        https://www.bitstamp.net/api/#tag/Orders/operation/CancelOrder

        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def cancel_all_orders(
        self, symbol: Str = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        cancel all open orders

        https://www.bitstamp.net/api/#tag/Orders/operation/CancelAllOrders
        https://www.bitstamp.net/api/#tag/Orders/operation/CancelOrdersForMarket

        :param str symbol: unified market symbol, only orders in the market of self symbol are cancelled when symbol is not None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def parse_order_status(self, status: Str):  # -> str | None:
        ...
    def fetch_order_status(
        self, id: str, symbol: Str = ..., params=...
    ):  # -> str | None:
        ...
    def fetch_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """
        fetches information on an order made by the user

        https://www.bitstamp.net/api/#tag/Orders/operation/GetOrderStatus

        :param str id: the order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        fetch all trades made by the user

        https://www.bitstamp.net/api/#tag/Transactions-private/operation/GetUserTransactions
        https://www.bitstamp.net/api/#tag/Transactions-private/operation/GetUserTransactionsForMarket

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    def fetch_deposits_withdrawals(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
        fetch history of deposits and withdrawals

        https://www.bitstamp.net/api/#tag/Transactions-private/operation/GetUserTransactions

        :param str [code]: unified currency code for the currency of the deposit/withdrawals, default is None
        :param int [since]: timestamp in ms of the earliest deposit/withdrawal, default is None
        :param int [limit]: max number of deposit/withdrawals to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a list of `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def fetch_withdrawals(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
        fetch all withdrawals made from an account

        https://www.bitstamp.net/api/#tag/Withdrawals/operation/GetWithdrawalRequests

        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch withdrawals for
        :param int [limit]: the maximum number of withdrawals structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def parse_transaction(
        self, transaction: dict, currency: Currency = ...
    ) -> Transaction: ...
    def parse_transaction_status(self, status: Str):  # -> str | None:
        ...
    def parse_order(self, order: dict, market: Market = ...) -> Order: ...
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

        https://www.bitstamp.net/api/#tag/Transactions-private/operation/GetUserTransactions

        :param str [code]: unified currency code, default is None
        :param int [since]: timestamp in ms of the earliest ledger entry, default is None
        :param int [limit]: max number of ledger entries to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ledger structure <https://docs.ccxt.com/#/?id=ledger>`
        """
        ...

    def fetch_open_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://www.bitstamp.net/api/#tag/Orders/operation/GetAllOpenOrders
        https://www.bitstamp.net/api/#tag/Orders/operation/GetOpenOrdersForMarket

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def get_currency_name(self, code):
        """
        @ignore
               :param str code: Unified currency code
               :returns str: lowercase version of code
        """
        ...

    def is_fiat(self, code): ...
    def fetch_deposit_address(self, code: str, params=...) -> DepositAddress:
        """
        fetch the deposit address for a currency associated with self account

        https://www.bitstamp.net/api/#tag/Deposits/operation/GetCryptoDepositAddress

        :param str code: unified currency code
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...

    def withdraw(
        self, code: str, amount: float, address: str, tag=..., params=...
    ) -> Transaction:
        """
        make a withdrawal

        https://www.bitstamp.net/api/#tag/Withdrawals/operation/RequestFiatWithdrawal
        https://www.bitstamp.net/api/#tag/Withdrawals/operation/RequestCryptoWithdrawal

        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str tag:
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def transfer(
        self, code: str, amount: float, fromAccount: str, toAccount: str, params=...
    ) -> TransferEntry:
        """
        transfer currency internally between wallets on the same account

        https://www.bitstamp.net/api/#tag/Sub-account/operation/TransferFromMainToSub
        https://www.bitstamp.net/api/#tag/Sub-account/operation/TransferFromSubToMain

        :param str code: unified currency code
        :param float amount: amount to transfer
        :param str fromAccount: account to transfer from
        :param str toAccount: account to transfer to
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transfer structure <https://docs.ccxt.com/#/?id=transfer-structure>`
        """
        ...

    def parse_transfer(self, transfer, currency=...):  # -> dict[str, Any]:
        ...
    def parse_transfer_status(self, status: Str) -> Str: ...
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
