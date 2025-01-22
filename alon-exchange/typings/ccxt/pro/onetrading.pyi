"""
This type stub file was generated by pyright.
"""

import ccxt.async_support
from ccxt.base.types import Balances, Int, Order, OrderBook, Str, Strings, Ticker, Tickers, Trade
from ccxt.async_support.base.ws.client import Client
from typing import List

class onetrading(ccxt.async_support.onetrading):
    def describe(self): # -> dict[Any, Any] | None:
        ...
    
    async def watch_balance(self, params=...) -> Balances:
        """

        https://developers.bitpanda.com/exchange/#account-history-channel

        watch balance and get the amount of funds available for trading or funds locked in orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...
    
    def handle_balance_snapshot(self, client, message): # -> None:
        ...
    
    async def watch_ticker(self, symbol: str, params=...) -> Ticker:
        """

        https://developers.bitpanda.com/exchange/#market-ticker-channel

        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market
        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    async def watch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """

        https://developers.bitpanda.com/exchange/#market-ticker-channel

        watches price tickers, a statistical calculation with the information for all markets or those specified.
        :param str symbols: unified symbols of the markets to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an array of `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def handle_ticker(self, client: Client, message): # -> None:
        ...
    
    def parse_ws_ticker(self, ticker, market=...): # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
    
    async def watch_my_trades(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Trade]:
        """

        https://developers.bitpanda.com/exchange/#account-history-channel

        get the list of trades associated with the user
        :param str symbol: unified symbol of the market to fetch trades for. Use 'any' to watch all trades
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...
    
    async def watch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """

        https://developers.bitpanda.com/exchange/#market-ticker-channel

        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...
    
    def handle_order_book(self, client: Client, message): # -> None:
        ...
    
    def handle_delta(self, orderbook, delta): # -> None:
        ...
    
    def handle_deltas(self, orderbook, deltas): # -> None:
        ...
    
    async def watch_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """

        https://developers.bitpanda.com/exchange/#account-history-channel

        watches information on multiple orders made by the user
        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.channel]: can listen to orders using ACCOUNT_HISTORY or TRADING
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def handle_trading(self, client: Client, message): # -> None:
        ...
    
    def parse_trading_order(self, order, market=...): # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
    
    def parse_trading_order_status(self, status): # -> str | None:
        ...
    
    def handle_orders(self, client: Client, message): # -> None:
        ...
    
    def handle_account_update(self, client: Client, message): # -> None:
        ...
    
    def parse_ws_order_status(self, status): # -> str | None:
        ...
    
    def update_balance(self, balance): # -> None:
        ...
    
    async def watch_ohlcv(self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...) -> List[list]:
        """

        https://developers.bitpanda.com/exchange/#candlesticks-channel

        watches historical candlestick data containing the open, high, low, and close price, and the volume of a market
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
    
    def find_timeframe(self, timeframe, timeframes=...): # -> None:
        ...
    
    def handle_subscriptions(self, client: Client, message):
        ...
    
    def handle_heartbeat(self, client: Client, message):
        ...
    
    def handle_error_message(self, client: Client, message):
        ...
    
    def handle_message(self, client: Client, message): # -> None:
        ...
    
    def handle_price_point_updates(self, client: Client, message):
        ...
    
    def handle_authentication_message(self, client: Client, message):
        ...
    
    async def watch_many(self, messageHash, request, subscriptionHash, symbols: Strings = ..., params=...):
        ...
    
    async def authenticate(self, params=...):
        ...
    


