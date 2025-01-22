"""
This type stub file was generated by pyright.
"""

from ccxt.base.exchange import Exchange
from ccxt.abstract.btcbox import ImplicitAPI
from ccxt.base.types import Balances, Int, Market, Num, Order, OrderBook, OrderSide, OrderType, Str, Strings, Ticker, Tickers, Trade
from typing import List

class btcbox(Exchange, ImplicitAPI):
    def describe(self): # -> dict[Any, Any] | None:
        ...
    
    def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for ace
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...
    
    def parse_market(self, market: dict) -> Market:
        ...
    
    def parse_balance(self, response) -> Balances:
        ...
    
    def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://blog.btcbox.jp/en/archives/8762#toc13

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...
    
    def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://blog.btcbox.jp/en/archives/8762#toc6

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...
    
    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker:
        ...
    
    def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://blog.btcbox.jp/en/archives/8762#toc5

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market
        :param str[] [symbols]: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def parse_trade(self, trade: dict, market: Market = ...) -> Trade:
        ...
    
    def fetch_trades(self, symbol: str, since: Int = ..., limit: Int = ..., params=...) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://blog.btcbox.jp/en/archives/8762#toc7

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...
    
    def create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = ..., params=...): # -> Order:
        """
        create a trade order

        https://blog.btcbox.jp/en/archives/8762#toc18

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def cancel_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """
        cancels an open order

        https://blog.btcbox.jp/en/archives/8762#toc17

        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
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
        fetches information on an order made by the user

        https://blog.btcbox.jp/en/archives/8762#toc16

        :param str id: the order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_orders_by_type(self, type, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        ...
    
    def fetch_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """
        fetches information on multiple orders made by the user

        https://blog.btcbox.jp/en/archives/8762#toc15

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_open_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://blog.btcbox.jp/en/archives/8762#toc15

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def nonce(self): # -> int:
        ...
    
    def sign(self, path, api=..., method=..., params=..., headers=..., body=...): # -> dict[str, Any]:
        ...
    
    def handle_errors(self, httpCode: int, reason: str, url: str, method: str, headers: dict, body: str, response, requestHeaders, requestBody): # -> None:
        ...
    
    def request(self, path, api=..., method=..., params=..., headers=..., body=..., config=...): # -> Any | None:
        ...
    


