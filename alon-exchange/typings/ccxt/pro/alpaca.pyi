"""
This type stub file was generated by pyright.
"""

import ccxt.async_support
from ccxt.base.types import Int, Order, OrderBook, Str, Ticker, Trade
from ccxt.async_support.base.ws.client import Client
from typing import List

class alpaca(ccxt.async_support.alpaca):
    def describe(self): # -> dict[Any, Any] | None:
        ...
    
    async def watch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://docs.alpaca.markets/docs/real-time-crypto-pricing-data#quotes

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def handle_ticker(self, client: Client, message): # -> None:
        ...
    
    def parse_ticker(self, ticker, market=...) -> Ticker:
        ...
    
    async def watch_ohlcv(self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...) -> List[list]:
        """
        watches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://docs.alpaca.markets/docs/real-time-crypto-pricing-data#bars

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...
    
    def handle_ohlcv(self, client: Client, message): # -> None:
        ...
    
    async def watch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://docs.alpaca.markets/docs/real-time-crypto-pricing-data#orderbooks

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return.
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...
    
    def handle_order_book(self, client: Client, message): # -> None:
        ...
    
    def handle_delta(self, bookside, delta): # -> None:
        ...
    
    def handle_deltas(self, bookside, deltas): # -> None:
        ...
    
    async def watch_trades(self, symbol: str, since: Int = ..., limit: Int = ..., params=...) -> List[Trade]:
        """
        watches information on multiple trades made in a market

        https://docs.alpaca.markets/docs/real-time-crypto-pricing-data#trades

        :param str symbol: unified market symbol of the market trades were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of trade structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...
    
    def handle_trades(self, client: Client, message): # -> None:
        ...
    
    async def watch_my_trades(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Trade]:
        """
        watches information on multiple trades made by the user

        https://docs.alpaca.markets/docs/websocket-streaming#trade-updates

        :param str symbol: unified market symbol of the market trades were made in
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trade structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.unifiedMargin]: use unified margin account
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...
    
    async def watch_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """
        watches information on multiple orders made by the user
        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def handle_trade_update(self, client: Client, message): # -> None:
        ...
    
    def handle_order(self, client: Client, message): # -> None:
        ...
    
    def handle_my_trade(self, client: Client, message): # -> None:
        ...
    
    def parse_my_trade(self, trade, market=...): # -> dict[Any, Any]:
        ...
    
    async def authenticate(self, url, params=...):
        ...
    
    def handle_error_message(self, client: Client, message):
        ...
    
    def handle_connected(self, client: Client, message):
        ...
    
    def handle_crypto_message(self, client: Client, message): # -> None:
        ...
    
    def handle_trading_message(self, client: Client, message): # -> None:
        ...
    
    def handle_message(self, client: Client, message): # -> None:
        ...
    
    def handle_authenticate(self, client: Client, message): # -> None:
        ...
    
    def handle_subscription(self, client: Client, message):
        ...
    


