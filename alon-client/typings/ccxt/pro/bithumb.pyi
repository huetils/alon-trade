"""
This type stub file was generated by pyright.
"""

import ccxt.async_support
from ccxt.base.types import Int, OrderBook, Strings, Ticker, Tickers, Trade
from ccxt.async_support.base.ws.client import Client
from typing import List

class bithumb(ccxt.async_support.bithumb):
    def describe(self): # -> dict[Any, Any] | None:
        ...
    
    async def watch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://apidocs.bithumb.com/v1.2.0/reference/%EB%B9%97%EC%8D%B8-%EA%B1%B0%EB%9E%98%EC%86%8C-%EC%A0%95%EB%B3%B4-%EC%88%98%EC%8B%A0

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.channel]: the channel to subscribe to, tickers by default. Can be tickers, sprd-tickers, index-tickers, block-tickers
        :returns dict: a `ticker structure <https://github.com/ccxt/ccxt/wiki/Manual#ticker-structure>`
        """
        ...
    
    async def watch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for all markets of a specific list

        https://apidocs.bithumb.com/v1.2.0/reference/%EB%B9%97%EC%8D%B8-%EA%B1%B0%EB%9E%98%EC%86%8C-%EC%A0%95%EB%B3%B4-%EC%88%98%EC%8B%A0

        :param str[] symbols: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def handle_ticker(self, client: Client, message): # -> None:
        ...
    
    def parse_ws_ticker(self, ticker, market=...): # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
    
    async def watch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """

        https://apidocs.bithumb.com/v1.2.0/reference/%EB%B9%97%EC%8D%B8-%EA%B1%B0%EB%9E%98%EC%86%8C-%EC%A0%95%EB%B3%B4-%EC%88%98%EC%8B%A0

        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://github.com/ccxt/ccxt/wiki/Manual#order-book-structure>` indexed by market symbols
        """
        ...
    
    def handle_order_book(self, client: Client, message): # -> None:
        ...
    
    def handle_delta(self, orderbook, delta): # -> None:
        ...
    
    def handle_deltas(self, orderbook, deltas): # -> None:
        ...
    
    async def watch_trades(self, symbol: str, since: Int = ..., limit: Int = ..., params=...) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://apidocs.bithumb.com/v1.2.0/reference/%EB%B9%97%EC%8D%B8-%EA%B1%B0%EB%9E%98%EC%86%8C-%EC%A0%95%EB%B3%B4-%EC%88%98%EC%8B%A0

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://github.com/ccxt/ccxt/wiki/Manual#public-trades>`
        """
        ...
    
    def handle_trades(self, client, message): # -> None:
        ...
    
    def parse_ws_trade(self, trade, market=...): # -> dict[Any, Any]:
        ...
    
    def handle_error_message(self, client: Client, message): # -> Literal[True]:
        ...
    
    def handle_message(self, client: Client, message): # -> None:
        ...
    


