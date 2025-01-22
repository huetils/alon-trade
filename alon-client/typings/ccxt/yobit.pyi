"""
This type stub file was generated by pyright.
"""

from ccxt.base.exchange import Exchange
from ccxt.abstract.yobit import ImplicitAPI
from ccxt.base.types import Balances, DepositAddress, Int, Market, Num, Order, OrderBook, OrderSide, OrderType, Str, Strings, Ticker, Tickers, Trade, TradingFees, Transaction
from typing import List

class yobit(Exchange, ImplicitAPI):
    def describe(self): # -> dict[Any, Any] | None:
        ...
    
    def parse_balance(self, response) -> Balances:
        ...
    
    def fetch_balance(self, params=...) -> Balances:
        """

        https://yobit.net/en/api

        query for balance and get the amount of funds available for trading or funds locked in orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...
    
    def fetch_markets(self, params=...) -> List[Market]:
        """

        https://yobit.net/en/api

        retrieves data on all markets for yobit
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...
    
    def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """

        https://yobit.net/en/api

        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...
    
    def fetch_order_books(self, symbols: Strings = ..., limit: Int = ..., params=...): # -> dict[Any, Any]:
        """

        https://yobit.net/en/api

        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data for multiple markets
        :param str[]|None symbols: list of unified market symbols, all symbols fetched if None, default is None
        :param int [limit]: max number of entries per orderbook to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbol
        """
        ...
    
    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker:
        ...
    
    def fetch_tickers_helper(self, idsString: str, params=...) -> Tickers:
        ...
    
    def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """

        https://yobit.net/en/api

        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market
        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param dict [params.all]: you can set to `true` for convenience to fetch all tickers from self exchange by sending multiple requests
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """

        https://yobit.net/en/api

        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market
        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def parse_trade(self, trade: dict, market: Market = ...) -> Trade:
        ...
    
    def fetch_trades(self, symbol: str, since: Int = ..., limit: Int = ..., params=...) -> List[Trade]:
        """

        https://yobit.net/en/api

        get the list of most recent trades for a particular symbol
        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...
    
    def fetch_trading_fees(self, params=...) -> TradingFees:
        """

        https://yobit.net/en/api

        fetch the trading fees for multiple markets
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `fee structures <https://docs.ccxt.com/#/?id=fee-structure>` indexed by market symbols
        """
        ...
    
    def create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = ..., params=...): # -> Order:
        """

        https://yobit.net/en/api

        create a trade order
        :param str symbol: unified symbol of the market to create an order in
        :param str type: must be 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def cancel_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """

        https://yobit.net/en/api

        cancels an open order
        :param str id: order id
        :param str symbol: not used by yobit cancelOrder()
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def parse_order_status(self, status: Str): # -> str | None:
        ...
    
    def parse_order(self, order: dict, market: Market = ...) -> Order:
        ...
    
    def fetch_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """

        https://yobit.net/en/api

        fetches information on an order made by the user
        :param str id: order id
        :param str symbol: not used by yobit fetchOrder
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_open_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """

        https://yobit.net/en/api

        fetch all unfilled currently open orders
        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of open order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_my_trades(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """

        https://yobit.net/en/api

        fetch all trades made by the user
        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...
    
    def create_deposit_address(self, code: str, params=...): # -> dict[str, Any]:
        """

        https://yobit.net/en/api

        create a currency deposit address
        :param str code: unified currency code of the currency for the deposit address
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...
    
    def fetch_deposit_address(self, code: str, params=...) -> DepositAddress:
        """
        fetch the deposit address for a currency associated with self account

        https://yobit.net/en/api

        :param str code: unified currency code
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...
    
    def withdraw(self, code: str, amount: float, address: str, tag=..., params=...) -> Transaction:
        """

        https://yobit.net/en/api

        make a withdrawal
        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str tag:
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def sign(self, path, api=..., method=..., params=..., headers=..., body=...): # -> dict[str, Any]:
        ...
    
    def handle_errors(self, httpCode: int, reason: str, url: str, method: str, headers: dict, body: str, response, requestHeaders, requestBody): # -> None:
        ...
    


