"""
This type stub file was generated by pyright.
"""

from typing import List

from ccxt.abstract.poloniexfutures import ImplicitAPI
from ccxt.async_support.base.exchange import Exchange
from ccxt.base.types import (
    Balances,
    FundingRate,
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
)

class poloniexfutures(Exchange, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    async def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for poloniexfutures

        https://api-docs.poloniex.com/futures/api/symbol

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...

    def parse_market(self, market: dict) -> Market: ...
    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker: ...
    async def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://api-docs.poloniex.com/futures/api/ticker#get-real-time-ticker-20

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    async def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://api-docs.poloniex.com/futures/api/ticker#get-real-time-ticker-of-all-symbols

        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    async def fetch_order_book(
        self, symbol: str, limit: Int = ..., params=...
    ) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://api-docs.poloniex.com/futures/api/orderbook#get-full-order-book---level-2
        https://api-docs.poloniex.com/futures/api/orderbook#get-full-order-book--level-3

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    async def fetch_l3_order_book(
        self, symbol: str, limit: Int = ..., params=...
    ):  # -> Coroutine[Any, Any, OrderBook]:
        """
        fetches level 3 information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://api-docs.poloniex.com/futures/api/orderbook#get-full-order-book--level-3

        :param str symbol: unified market symbol
        :param int [limit]: max number of orders to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order book structure <https://docs.ccxt.com/#/?id=order-book-structure>`
        """
        ...

    def parse_trade(self, trade: dict, market: Market = ...) -> Trade: ...
    async def fetch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://api-docs.poloniex.com/futures/api/historical#transaction-history

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    async def fetch_time(self, params=...):  # -> int | None:
        """
        fetches the current integer timestamp in milliseconds from the poloniexfutures server

        https://api-docs.poloniex.com/futures/api/time#server-time

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int: the current integer timestamp in milliseconds from the poloniexfutures server
        """
        ...

    async def fetch_ohlcv(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[list]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://api-docs.poloniex.com/futures/api/kline#get-k-line-data-of-contract

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...

    def parse_balance(self, response) -> Balances: ...
    async def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://api-docs.poloniex.com/futures/api/account#get-account-overview

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    async def create_order(
        self,
        symbol: str,
        type: OrderType,
        side: OrderSide,
        amount: float,
        price: Num = ...,
        params=...,
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        """
        Create an order on the exchange

        https://api-docs.poloniex.com/futures/api/orders#place-an-order

        :param str symbol: Unified CCXT market symbol
        :param str type: 'limit' or 'market'
        :param str side: 'buy' or 'sell'
        :param float amount: the amount of currency to trade
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]:  extra parameters specific to the exchange API endpoint
        :param float [params.leverage]: Leverage size of the order
        :param float [params.triggerPrice]: The price at which a trigger order is triggered at
        :param bool [params.reduceOnly]: A mark to reduce the position size only. Set to False by default. Need to set the position size when reduceOnly is True.
        :param str [params.timeInForce]: GTC, GTT, IOC, or FOK, default is GTC, limit orders only
        :param str [params.postOnly]: Post only flag, invalid when timeInForce is IOC or FOK
        :param str [params.clientOid]: client order id, defaults to uuid if not passed
        :param str [params.remark]: remark for the order, length cannot exceed 100 utf8 characters
        :param str [params.stop]: 'up' or 'down', defaults to 'up' if side is sell and 'down' if side is buy, requires stopPrice
        :param str [params.stopPriceType]:  TP, IP or MP, defaults to TP
        :param bool [params.closeOrder]: set to True to close position
        :param bool [params.forceHold]: A mark to forcely hold the funds for an order, even though it's an order to reduce the position size. This helps the order stay on the order book and not get canceled when the position size changes. Set to False by default.
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def cancel_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """
        cancels an open order

        https://api-docs.poloniex.com/futures/api/orders#cancel-an-order

        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_positions(
        self, symbols: Strings = ..., params=...
    ):  # -> dict[Any, Any] | list[Any]:
        """
        fetch all open positions

        https://api-docs.poloniex.com/futures/api/positions#get-position-list

        :param str[]|None symbols: list of unified market symbols
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `position structure <https://docs.ccxt.com/#/?id=position-structure>`
        """
        ...

    def parse_position(
        self, position: dict, market: Market = ...
    ):  # -> dict[str, Any]:
        ...
    async def fetch_funding_history(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any]:
        """
        fetch the history of funding payments paid and received on self account

        https://api-docs.poloniex.com/futures/api/funding-fees#get-funding-history

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch funding history for
        :param int [limit]: the maximum number of funding history structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `funding history structure <https://docs.ccxt.com/#/?id=funding-history-structure>`
        """
        ...

    async def cancel_all_orders(self, symbol: Str = ..., params=...):  # -> list[Any]:
        """
        cancel all open orders
        :param str symbol: unified market symbol, only orders in the market of self symbol are cancelled when symbol is not None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param dict [params.trigger]: When True, all the trigger orders will be cancelled
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_orders_by_status(
        self, status, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        fetches a list of orders placed on the exchange

        https://api-docs.poloniex.com/futures/api/orders#get-order-listdeprecated
        https://api-docs.poloniex.com/futures/api/orders#get-untriggered-stop-order-list

        :param str status: 'active' or 'closed', only 'active' is valid for stop orders
        :param str symbol: unified symbol for the market to retrieve orders from
        :param int [since]: timestamp in ms of the earliest order to retrieve
        :param int [limit]: The maximum number of orders to retrieve
        :param dict [params]: exchange specific parameters
        :param bool [params.stop]: set to True to retrieve untriggered stop orders
        :param int [params.until]: End time in ms
        :param str [params.side]: buy or sell
        :param str [params.type]: limit or market
        :returns: An `array of order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_open_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://api-docs.poloniex.com/futures/api/orders#get-order-listdeprecated
        https://api-docs.poloniex.com/futures/api/orders#get-untriggered-stop-order-list

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: end time in ms
        :param str [params.side]: buy or sell
        :param str [params.type]: limit, or market
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_closed_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetches information on multiple closed orders made by the user

        https://api-docs.poloniex.com/futures/api/orders#get-order-listdeprecated
        https://api-docs.poloniex.com/futures/api/orders#get-untriggered-stop-order-list

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: end time in ms
        :param str [params.side]: buy or sell
        :param str [params.type]: limit, or market
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_order(
        self, id: Str = ..., symbol: Str = ..., params=...
    ):  # -> Order:
        """
        fetches information on an order made by the user

        https://api-docs.poloniex.com/futures/api/orders#get-details-of-a-single-order
        https://api-docs.poloniex.com/futures/api/orders#get-single-order-by-clientoid

        :param str id: the order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def parse_order(self, order: dict, market: Market = ...) -> Order: ...
    async def fetch_funding_rate(self, symbol: str, params=...) -> FundingRate:
        """
        fetch the current funding rate

        https://api-docs.poloniex.com/futures/api/futures-index#get-premium-index

        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `funding rate structure <https://docs.ccxt.com/#/?id=funding-rate-structure>`
        """
        ...

    async def fetch_funding_interval(self, symbol: str, params=...) -> FundingRate:
        """
        fetch the current funding rate interval

        https://api-docs.poloniex.com/futures/api/futures-index#get-premium-index

        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `funding rate structure <https://docs.ccxt.com/#/?id=funding-rate-structure>`
        """
        ...

    def parse_funding_rate(self, data, market: Market = ...) -> FundingRate: ...
    def parse_funding_interval(self, interval):  # -> str | None:
        ...
    async def fetch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        fetch all trades made by the user

        https://api-docs.poloniex.com/futures/api/fills#get-fillsdeprecated

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.orderIdFills]: filles for a specific order(other parameters can be ignored if specified)
        :param str [params.side]: buy or sell
        :param str [params.type]:  limit, market, limit_stop or market_stop
        :param int [params.endAt]: end time(milisecond)
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    async def set_margin_mode(
        self, marginMode: str, symbol: Str = ..., params=...
    ):  # -> Any:
        """
        set margin mode to 'cross' or 'isolated'

        https://api-docs.poloniex.com/futures/api/margin-mode#change-margin-mode

        :param str marginMode: "0"(isolated) or "1"(cross)
        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: response from the exchange
        """
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
