"""
This type stub file was generated by pyright.
"""

from typing import List

from ccxt.abstract.wazirx import ImplicitAPI
from ccxt.base.exchange import Exchange
from ccxt.base.types import (
    Balances,
    Currencies,
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

class wazirx(Exchange, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    def fetch_markets(self, params=...) -> List[Market]:
        """

        https://docs.wazirx.com/#exchange-info

        retrieves data on all markets for wazirx
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...

    def parse_market(self, market: dict) -> Market: ...
    def fetch_ohlcv(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[list]:
        """

        https://docs.wazirx.com/#kline-candlestick-data

        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market
        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents. Available values [1m,5m,15m,30m,1h,2h,4h,6h,12h,1d,1w]
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: timestamp in s of the latest candle to fetch
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...

    def parse_ohlcv(self, ohlcv, market: Market = ...) -> list: ...
    def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """

        https://docs.wazirx.com/#order-book

        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """

        https://docs.wazirx.com/#24hr-ticker-price-change-statistics

        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market
        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """

        https://docs.wazirx.com/#24hr-tickers-price-change-statistics

        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market
        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def fetch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """

        https://docs.wazirx.com/#recent-trades-list

        get the list of most recent trades for a particular symbol
        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    def parse_trade(self, trade: dict, market: Market = ...) -> Trade: ...
    def fetch_status(self, params=...):  # -> dict[str, Any]:
        """

        https://docs.wazirx.com/#system-status

        the latest known information on the availability of the exchange API
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `status structure <https://docs.ccxt.com/#/?id=exchange-status-structure>`
        """
        ...

    def fetch_time(self, params=...):  # -> int | None:
        """

        https://docs.wazirx.com/#check-server-time

        fetches the current integer timestamp in milliseconds from the exchange server
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int: the current integer timestamp in milliseconds from the exchange server
        """
        ...

    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker: ...
    def parse_balance(self, response) -> Balances: ...
    def fetch_balance(self, params=...) -> Balances:
        """

        https://docs.wazirx.com/#fund-details-user_data

        query for balance and get the amount of funds available for trading or funds locked in orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    def fetch_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """

        https://docs.wazirx.com/#all-orders-user_data

        fetches information on multiple orders made by the user
        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_open_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """

        https://docs.wazirx.com/#current-open-orders-user_data

        fetch all unfilled currently open orders
        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def cancel_all_orders(
        self, symbol: Str = ..., params=...
    ):  # -> list[Any] | list[object]:
        """

        https://docs.wazirx.com/#cancel-all-open-orders-on-a-symbol-trade

        cancel all open orders in a market
        :param str symbol: unified market symbol of the market to cancel orders in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def cancel_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """

        https://docs.wazirx.com/#cancel-order-trade

        cancels an open order
        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
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

        https://docs.wazirx.com/#new-order-trade

        create a trade order
        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def parse_order(self, order: dict, market: Market = ...) -> Order: ...
    def parse_order_status(self, status: Str):  # -> str | None:
        ...
    def fetch_currencies(self, params=...) -> Currencies:
        """
        fetches all available currencies on an exchange

        https://docs.wazirx.com/#all-coins-39-information-user_data

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an associative dictionary of currencies
        """
        ...

    def fetch_deposit_address(self, code: str, params=...) -> DepositAddress:
        """
        fetch the deposit address for a currency associated with self account

        https://docs.wazirx.com/#deposit-address-supporting-network-user_data

        :param str code: unified currency code of the currency for the deposit address
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.network]: unified network code, you can get network from fetchCurrencies
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...

    def fetch_withdrawals(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
        fetch all withdrawals made from an account

        https://docs.wazirx.com/#withdraw-history-supporting-network-user_data

        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch withdrawals for
        :param int [limit]: the maximum number of withdrawals structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: the latest time in ms to fetch entries for
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def parse_transaction_status(self, status: Str):  # -> str | None:
        ...
    def parse_transaction(
        self, transaction: dict, currency: Currency = ...
    ) -> Transaction: ...
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
