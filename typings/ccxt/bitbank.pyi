"""
This type stub file was generated by pyright.
"""

from typing import List

from ccxt.abstract.bitbank import ImplicitAPI
from ccxt.base.exchange import Exchange
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
    Ticker,
    Trade,
    TradingFees,
    Transaction,
)

class bitbank(Exchange, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for bitbank

        https://github.com/bitbankinc/bitbank-api-docs/blob/38d6d7c6f486c793872fd4b4087a0d090a04cd0a/rest-api.md#get-all-pairs-info

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...

    def parse_market(self, entry) -> Market: ...
    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker: ...
    def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://github.com/bitbankinc/bitbank-api-docs/blob/38d6d7c6f486c793872fd4b4087a0d090a04cd0a/public-api.md#ticker

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://github.com/bitbankinc/bitbank-api-docs/blob/38d6d7c6f486c793872fd4b4087a0d090a04cd0a/public-api.md#depth

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def parse_trade(self, trade: dict, market: Market = ...) -> Trade: ...
    def fetch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://github.com/bitbankinc/bitbank-api-docs/blob/38d6d7c6f486c793872fd4b4087a0d090a04cd0a/public-api.md#transactions

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    def fetch_trading_fees(self, params=...) -> TradingFees:
        """
        fetch the trading fees for multiple markets

        https://github.com/bitbankinc/bitbank-api-docs/blob/38d6d7c6f486c793872fd4b4087a0d090a04cd0a/rest-api.md#get-all-pairs-info

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `fee structures <https://docs.ccxt.com/#/?id=fee-structure>` indexed by market symbols
        """
        ...

    def parse_ohlcv(self, ohlcv, market: Market = ...) -> list: ...
    def fetch_ohlcv(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[list]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://github.com/bitbankinc/bitbank-api-docs/blob/38d6d7c6f486c793872fd4b4087a0d090a04cd0a/public-api.md#candlestick

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

        https://github.com/bitbankinc/bitbank-api-docs/blob/38d6d7c6f486c793872fd4b4087a0d090a04cd0a/rest-api.md#assets

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
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
    ):  # -> Order:
        """
        create a trade order

        https://github.com/bitbankinc/bitbank-api-docs/blob/38d6d7c6f486c793872fd4b4087a0d090a04cd0a/rest-api.md#create-new-order

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

        https://github.com/bitbankinc/bitbank-api-docs/blob/38d6d7c6f486c793872fd4b4087a0d090a04cd0a/rest-api.md#cancel-order

        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """
        fetches information on an order made by the user

        https://github.com/bitbankinc/bitbank-api-docs/blob/38d6d7c6f486c793872fd4b4087a0d090a04cd0a/rest-api.md#fetch-order-information

        :param str id: the order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_open_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://github.com/bitbankinc/bitbank-api-docs/blob/38d6d7c6f486c793872fd4b4087a0d090a04cd0a/rest-api.md#fetch-active-orders

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        fetch all trades made by the user

        https://github.com/bitbankinc/bitbank-api-docs/blob/38d6d7c6f486c793872fd4b4087a0d090a04cd0a/rest-api.md#fetch-trade-history

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    def fetch_deposit_address(self, code: str, params=...) -> DepositAddress:
        """
        fetch the deposit address for a currency associated with self account

        https://github.com/bitbankinc/bitbank-api-docs/blob/38d6d7c6f486c793872fd4b4087a0d090a04cd0a/rest-api.md#get-withdrawal-accounts

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

        https://github.com/bitbankinc/bitbank-api-docs/blob/38d6d7c6f486c793872fd4b4087a0d090a04cd0a/rest-api.md#new-withdrawal-request

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
