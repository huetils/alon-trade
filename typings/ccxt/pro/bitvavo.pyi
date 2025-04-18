"""
This type stub file was generated by pyright.
"""

from typing import List

import ccxt.async_support
from ccxt.async_support.base.ws.client import Client
from ccxt.base.types import (
    Balances,
    Int,
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
    TradingFees,
)

class bitvavo(ccxt.async_support.bitvavo):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    async def watch_public(self, name, symbol, params=...): ...
    async def watch_public_multiple(
        self, methodName, channelName: str, symbols, params=...
    ): ...
    async def watch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://docs.bitvavo.com/#tag/Market-data-subscription-WebSocket/paths/~1subscribeTicker24h/post

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    async def watch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for all markets of a specific list

        https://docs.bitvavo.com/#tag/Market-data-subscription-WebSocket/paths/~1subscribeTicker24h/post

        :param str[] [symbols]: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def handle_ticker(self, client: Client, message):  # -> None:
        ...
    async def watch_bids_asks(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        watches best bid & ask for symbols

        https://docs.bitvavo.com/#tag/Market-data-subscription-WebSocket/paths/~1subscribeTicker24h/post

        :param str[] symbols: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def handle_bid_ask(self, client: Client, message):  # -> None:
        ...
    def parse_ws_bid_ask(
        self, ticker, market=...
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
    async def watch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol
        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    def handle_trade(self, client: Client, message):  # -> None:
        ...
    async def watch_ohlcv(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[list]:
        """
        watches historical candlestick data containing the open, high, low, and close price, and the volume of a market
        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...

    def handle_fetch_ohlcv(self, client: Client, message):  # -> None:
        ...
    def handle_ohlcv(self, client: Client, message):  # -> None:
        ...
    async def watch_order_book(
        self, symbol: str, limit: Int = ..., params=...
    ) -> OrderBook:
        """
        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def handle_delta(self, bookside, delta):  # -> None:
        ...
    def handle_deltas(self, bookside, deltas):  # -> None:
        ...
    def handle_order_book_message(self, client: Client, message, orderbook): ...
    def handle_order_book(self, client: Client, message):  # -> None:
        ...
    async def watch_order_book_snapshot(self, client, message, subscription): ...
    def handle_order_book_snapshot(self, client: Client, message):  # -> None:
        ...
    def handle_order_book_subscription(
        self, client: Client, message, subscription
    ):  # -> None:
        ...
    def handle_order_book_subscriptions(
        self, client: Client, message, marketIds
    ):  # -> None:
        ...
    async def watch_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        watches information on multiple orders made by the user
        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def watch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        watches information on multiple trades made by the user
        :param str symbol: unified market symbol of the market trades were made in
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trade structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    async def create_order_ws(
        self,
        symbol: str,
        type: OrderType,
        side: OrderSide,
        amount: float,
        price: Num = ...,
        params=...,
    ) -> Order:
        """
        create a trade order

        https://docs.bitvavo.com/#tag/Orders/paths/~1order/post

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float price: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the bitvavo api endpoint
        :param str [params.timeInForce]: "GTC", "IOC", or "PO"
        :param float [params.stopPrice]: The price at which a trigger order is triggered at
        :param float [params.triggerPrice]: The price at which a trigger order is triggered at
        :param bool [params.postOnly]: If True, the order will only be posted to the order book and not executed immediately
        :param float [params.stopLossPrice]: The price at which a stop loss order is triggered at
        :param float [params.takeProfitPrice]: The price at which a take profit order is triggered at
        :param str [params.triggerType]: "price"
        :param str [params.triggerReference]: "lastTrade", "bestBid", "bestAsk", "midPrice" Only for stop orders: Use self to determine which parameter will trigger the order
        :param str [params.selfTradePrevention]: "decrementAndCancel", "cancelOldest", "cancelNewest", "cancelBoth"
        :param bool [params.disableMarketProtection]: don't cancel if the next fill price is 10% worse than the best fill price
        :param bool [params.responseRequired]: Set self to 'false' when only an acknowledgement of success or failure is required, self is faster.
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def edit_order_ws(
        self,
        id: str,
        symbol: str,
        type: OrderType,
        side: OrderSide,
        amount: Num = ...,
        price: Num = ...,
        params=...,
    ) -> Order:
        """
        edit a trade order

        https://docs.bitvavo.com/#tag/Orders/paths/~1order/put

        :param str id: cancel order id
        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float [amount]: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the bitvavo api endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def cancel_order_ws(self, id: str, symbol: Str = ..., params=...):
        """

        https://docs.bitvavo.com/#tag/Orders/paths/~1order/delete

        cancels an open order
        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the bitvavo api endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def cancel_all_orders_ws(self, symbol: Str = ..., params=...):
        """

        https://docs.bitvavo.com/#tag/Orders/paths/~1orders/delete

        cancel all open orders
        :param str symbol: unified market symbol, only orders in the market of self symbol are cancelled when symbol is not None
        :param dict [params]: extra parameters specific to the bitvavo api endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def handle_multiple_orders(self, client: Client, message):  # -> None:
        ...
    async def fetch_order_ws(self, id: str, symbol: Str = ..., params=...) -> Order:
        """

        https://docs.bitvavo.com/#tag/General/paths/~1assets/get

        fetches information on an order made by the user
        :param str id: the order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the bitvavo api endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_orders_ws(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """

        https://docs.bitvavo.com/#tag/Orders/paths/~1orders/get

        fetches information on multiple orders made by the user
        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of  orde structures to retrieve
        :param dict [params]: extra parameters specific to the bitvavo api endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def request_id(self):  # -> int:
        ...
    async def watch_request(self, action, request): ...
    async def fetch_open_orders_ws(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetch all unfilled currently open orders
        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the bitvavo api endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    async def fetch_my_trades_ws(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """

        https://docs.bitvavo.com/#tag/Trades

        fetch all trades made by the user
        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the bitvavo api endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    def handle_my_trades(self, client: Client, message):  # -> None:
        ...
    async def withdraw_ws(self, code: str, amount, address, tag=..., params=...):
        """
        make a withdrawal
        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str tag:
        :param dict [params]: extra parameters specific to the bitvavo api endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def handle_withdraw(self, client: Client, message):  # -> None:
        ...
    async def fetch_withdrawals_ws(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """

        https://docs.bitvavo.com/#tag/Account/paths/~1withdrawalHistory/get

        fetch all withdrawals made from an account
        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch withdrawals for
        :param int [limit]: the maximum number of withdrawals structures to retrieve
        :param dict [params]: extra parameters specific to the bitvavo api endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def handle_withdraws(self, client: Client, message):  # -> None:
        ...
    async def fetch_ohlcv_ws(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[list]:
        """

        https://docs.bitvavo.com/#tag/Market-Data/paths/~1{market}~1candles/get

        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market
        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the bitvavo api endpoint
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...

    async def fetch_deposits_ws(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """

        https://docs.bitvavo.com/#tag/Account/paths/~1depositHistory/get

        fetch all deposits made to an account
        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch deposits for
        :param int [limit]: the maximum number of deposits structures to retrieve
        :param dict [params]: extra parameters specific to the bitvavo api endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def handle_deposits(self, client: Client, message):  # -> None:
        ...
    async def fetch_trading_fees_ws(self, params=...) -> TradingFees:
        """

        https://docs.bitvavo.com/#tag/Account/paths/~1account/get

        fetch the trading fees for multiple markets
        :param dict [params]: extra parameters specific to the bitvavo api endpoint
        :returns dict: a dictionary of `fee structures <https://docs.ccxt.com/#/?id=fee-structure>` indexed by market symbols
        """
        ...

    async def fetch_markets_ws(self, params=...):
        """

        https://docs.bitvavo.com/#tag/General/paths/~1markets/get

        retrieves data on all markets for bitvavo
        :param dict [params]: extra parameters specific to the exchange api endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...

    async def fetch_currencies_ws(self, params=...):
        """

        https://docs.bitvavo.com/#tag/General/paths/~1assets/get

        fetches all available currencies on an exchange
        :param dict [params]: extra parameters specific to the bitvavo api endpoint
        :returns dict: an associative dictionary of currencies
        """
        ...

    def handle_fetch_currencies(self, client: Client, message):  # -> None:
        ...
    def handle_trading_fees(self, client, message):  # -> None:
        ...
    async def fetch_balance_ws(self, params=...) -> Balances:
        """

        https://docs.bitvavo.com/#tag/Account/paths/~1balance/get

        query for balance and get the amount of funds available for trading or funds locked in orders
        :param dict [params]: extra parameters specific to the bitvavo api endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/en/latest/manual.html?#balance-structure>`
        """
        ...

    def handle_fetch_balance(self, client: Client, message):  # -> None:
        ...
    def handle_single_order(self, client: Client, message):  # -> None:
        ...
    def handle_markets(self, client: Client, message):  # -> None:
        ...
    def build_message_hash(self, action, params=...): ...
    def action_and_market_message_hash(self, action, params=...): ...
    def action_and_order_id_message_hash(self, action, params=...): ...
    def handle_order(self, client: Client, message):  # -> None:
        ...
    def handle_my_trade(self, client: Client, message):  # -> None:
        ...
    def handle_subscription_status(self, client: Client, message): ...
    async def authenticate(self, params=...): ...
    def handle_authentication_message(self, client: Client, message):  # -> None:
        ...
    def handle_error_message(self, client: Client, message):  # -> None:
        ...
    def handle_message(self, client: Client, message):  # -> None:
        ...
