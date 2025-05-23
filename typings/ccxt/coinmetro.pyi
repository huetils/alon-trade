"""
This type stub file was generated by pyright.
"""

from typing import List

from ccxt.abstract.coinmetro import ImplicitAPI
from ccxt.base.exchange import Exchange
from ccxt.base.types import (
    Balances,
    Currencies,
    Currency,
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
    Strings,
    Ticker,
    Tickers,
    Trade,
)

class coinmetro(Exchange, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    def fetch_currencies(self, params=...) -> Currencies:
        """
        fetches all available currencies on an exchange

        https://documenter.getpostman.com/view/3653795/SVfWN6KS#d5876d43-a3fe-4479-8c58-24d0f044edfb

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an associative dictionary of currencies
        """
        ...

    def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for coinmetro

        https://documenter.getpostman.com/view/3653795/SVfWN6KS#9fd18008-338e-4863-b07d-722878a46832

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...

    def parse_market(self, market: dict) -> Market: ...
    def parse_market_id(self, marketId):  # -> dict[Any, Any]:
        ...
    def parse_market_precision_and_limits(self, currencyId):  # -> dict[Any, Any]:
        ...
    def fetch_ohlcv(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[list]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://documenter.getpostman.com/view/3653795/SVfWN6KS#13cfb5bc-7bfb-4847-85e1-e0f35dfb3573

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: the latest time in ms to fetch entries for
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...

    def parse_ohlcv(self, ohlcv, market: Market = ...) -> list: ...
    def fetch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://documenter.getpostman.com/view/3653795/SVfWN6KS#6ee5d698-06da-4570-8c84-914185e05065

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch(default 200, max 500)
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    def fetch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        fetch all trades made by the user

        https://documenter.getpostman.com/view/3653795/SVfWN6KS#4d48ae69-8ee2-44d1-a268-71f84e557b7b

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve(default 500, max 1000)
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    def parse_trade(self, trade: dict, market: Market = ...) -> Trade: ...
    def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://documenter.getpostman.com/view/3653795/SVfWN6KS#26ad80d7-8c46-41b5-9208-386f439a8b87

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return(default 100, max 200)
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def parse_bids_asks(
        self,
        bidasks,
        priceKey: IndexType = ...,
        amountKey: IndexType = ...,
        countOrIdKey: IndexType = ...,
    ):  # -> list[Any]:
        ...
    def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://documenter.getpostman.com/view/3653795/SVfWN6KS#6ecd1cd1-f162-45a3-8b3b-de690332a485

        :param str[] [symbols]: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def fetch_bids_asks(
        self, symbols: Strings = ..., params=...
    ):  # -> dict[Any, Any] | list[Any]:
        """
        fetches the bid and ask price and volume for multiple markets

        https://documenter.getpostman.com/view/3653795/SVfWN6KS#6ecd1cd1-f162-45a3-8b3b-de690332a485

        :param str[] [symbols]: unified symbols of the markets to fetch the bids and asks for, all markets are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker: ...
    def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://documenter.getpostman.com/view/3653795/SVfWN6KS#741a1dcc-7307-40d0-acca-28d003d1506a

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    def parse_balance(self, balances) -> Balances: ...
    def fetch_ledger(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[LedgerEntry]:
        """
        fetch the history of changes, actions done by the user or operations that altered the balance of the user

        https://documenter.getpostman.com/view/3653795/SVfWN6KS#4e7831f7-a0e7-4c3e-9336-1d0e5dcb15cf

        :param str [code]: unified currency code, default is None
        :param int [since]: timestamp in ms of the earliest ledger entry, default is None
        :param int [limit]: max number of ledger entries to return(default 200, max 500)
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: the latest time in ms to fetch entries for
        :returns dict: a `ledger structure <https://docs.ccxt.com/#/?id=ledger>`
        """
        ...

    def parse_ledger_entry(
        self, item: dict, currency: Currency = ...
    ) -> LedgerEntry: ...
    def parse_ledger_entry_description(self, description):  # -> list[str | Any | None]:
        ...
    def parse_ledger_entry_type(self, type):  # -> str | None:
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

        https://documenter.getpostman.com/view/3653795/SVfWN6KS#a4895a1d-3f50-40ae-8231-6962ef06c771

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param float [params.cost]: the quote quantity that can be used alternative for the amount in market orders
        :param str [params.timeInForce]: "GTC", "IOC", "FOK", "GTD"
        :param number [params.expirationTime]: timestamp in millisecond, for GTD orders only
        :param float [params.triggerPrice]: the price at which a trigger order is triggered at
        :param float [params.stopLossPrice]: *margin only* The price at which a stop loss order is triggered at
        :param float [params.takeProfitPrice]: *margin only* The price at which a take profit order is triggered at
        :param bool [params.margin]: True for creating a margin order
        :param str [params.fillStyle]: fill style of the limit order: "sell" fulfills selling quantity "buy" fulfills buying quantity "base" fulfills base currency quantity "quote" fulfills quote currency quantity
        :param str [params.clientOrderId]: client's comment
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def handle_create_order_side(
        self, sellingCurrency, buyingCurrency, sellingQty, buyingQty, request=...
    ): ...
    def encode_order_time_in_force(self, timeInForce):  # -> None:
        ...
    def cancel_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """
        cancels an open order

        https://documenter.getpostman.com/view/3653795/SVfWN6KS#eaea86da-16ca-4c56-9f00-5b1cb2ad89f8
        https://documenter.getpostman.com/view/3653795/SVfWN6KS#47f913fb-8cab-49f4-bc78-d980e6ced316

        :param str id: order id
        :param str symbol: not used by coinmetro cancelOrder()
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.margin]: True for cancelling a margin order
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def close_position(
        self, symbol: str, side: OrderSide = ..., params=...
    ):  # -> Order:
        """
        closes an open position

        https://documenter.getpostman.com/view/3653795/SVfWN6KS#47f913fb-8cab-49f4-bc78-d980e6ced316

        :param str symbol: not used by coinmetro closePosition()
        :param str [side]: not used by coinmetro closePosition()
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.orderID]: order id
        :param number [params.fraction]: fraction of order to close, between 0 and 1(defaults to 1)
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_open_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://documenter.getpostman.com/view/3653795/SVfWN6KS#518afd7a-4338-439c-a651-d4fdaa964138

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of open order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_canceled_and_closed_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetches information on multiple canceled and closed orders made by the user

        https://documenter.getpostman.com/view/3653795/SVfWN6KS#4d48ae69-8ee2-44d1-a268-71f84e557b7b

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """
        fetches information on an order made by the user

        https://documenter.getpostman.com/view/3653795/SVfWN6KS#95bbed87-db1c-47a7-a03e-aa247e91d5a6

        :param int|str id: order id
        :param str symbol: not used by coinmetro fetchOrder()
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def parse_order(self, order: dict, market: Market = ...) -> Order: ...
    def parse_order_time_in_force(self, timeInForce):  # -> None:
        ...
    def borrow_cross_margin(
        self, code: str, amount: float, params=...
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        """
        create a loan to borrow margin

        https://documenter.getpostman.com/view/3653795/SVfWN6KS#5b90b3b9-e5db-4d07-ac9d-d680a06fd110

        :param str code: unified currency code of the currency to borrow
        :param float amount: the amount to borrow
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `margin loan structure <https://docs.ccxt.com/#/?id=margin-loan-structure>`
        """
        ...

    def parse_margin_loan(self, info, currency: Currency = ...):  # -> dict[str, Any]:
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
