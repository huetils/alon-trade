"""
This type stub file was generated by pyright.
"""

from ccxt.async_support.base.exchange import Exchange
from ccxt.abstract.coinmate import ImplicitAPI
from ccxt.base.types import Balances, Currency, Int, Market, Num, Order, OrderBook, OrderSide, OrderType, Str, Strings, Ticker, Tickers, Trade, TradingFeeInterface, Transaction
from typing import List

class coinmate(Exchange, ImplicitAPI):
    def describe(self): # -> dict[Any, Any] | None:
        ...
    
    async def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for coinmate

        https://coinmate.docs.apiary.io/#reference/trading-pairs/get-trading-pairs/get

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...
    
    def parse_balance(self, response) -> Balances:
        ...
    
    async def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://coinmate.docs.apiary.io/#reference/balance/get-balances/post

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...
    
    async def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://coinmate.docs.apiary.io/#reference/order-book/get-order-book/get

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...
    
    async def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://coinmate.docs.apiary.io/#reference/ticker/get-ticker/get

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    async def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://coinmate.docs.apiary.io/#reference/ticker/get-ticker-all/get

        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker:
        ...
    
    async def fetch_deposits_withdrawals(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Transaction]:
        """
        fetch history of deposits and withdrawals

        https://coinmate.docs.apiary.io/#reference/transfers/get-transfer-history/post

        :param str [code]: unified currency code for the currency of the deposit/withdrawals, default is None
        :param int [since]: timestamp in ms of the earliest deposit/withdrawal, default is None
        :param int [limit]: max number of deposit/withdrawals to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a list of `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def parse_transaction_status(self, status: Str): # -> str | None:
        ...
    
    def parse_transaction(self, transaction: dict, currency: Currency = ...) -> Transaction:
        ...
    
    async def withdraw(self, code: str, amount: float, address: str, tag=..., params=...) -> Transaction:
        """
        make a withdrawal

        https://coinmate.docs.apiary.io/#reference/bitcoin-withdrawal-and-deposit/withdraw-bitcoins/post
        https://coinmate.docs.apiary.io/#reference/litecoin-withdrawal-and-deposit/withdraw-litecoins/post
        https://coinmate.docs.apiary.io/#reference/ethereum-withdrawal-and-deposit/withdraw-ethereum/post
        https://coinmate.docs.apiary.io/#reference/ripple-withdrawal-and-deposit/withdraw-ripple/post
        https://coinmate.docs.apiary.io/#reference/cardano-withdrawal-and-deposit/withdraw-cardano/post
        https://coinmate.docs.apiary.io/#reference/solana-withdrawal-and-deposit/withdraw-solana/post

        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str tag:
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    async def fetch_my_trades(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetch all trades made by the user

        https://coinmate.docs.apiary.io/#reference/trade-history/get-trade-history/post

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...
    
    def parse_trade(self, trade: dict, market: Market = ...) -> Trade:
        ...
    
    async def fetch_trades(self, symbol: str, since: Int = ..., limit: Int = ..., params=...) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://coinmate.docs.apiary.io/#reference/transactions/transactions/get

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...
    
    async def fetch_trading_fee(self, symbol: str, params=...) -> TradingFeeInterface:
        """
        fetch the trading fees for a market

        https://coinmate.docs.apiary.io/#reference/trader-fees/get-trading-fees/post

        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `fee structure <https://docs.ccxt.com/#/?id=fee-structure>`
        """
        ...
    
    async def fetch_open_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://coinmate.docs.apiary.io/#reference/order/get-open-orders/post

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """
        fetches information on multiple orders made by the user

        https://coinmate.docs.apiary.io/#reference/order/order-history/post

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def parse_order_status(self, status: Str): # -> str | None:
        ...
    
    def parse_order_type(self, type: Str): # -> str | None:
        ...
    
    def parse_order(self, order: dict, market: Market = ...) -> Order:
        ...
    
    async def create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = ..., params=...): # -> OrderedDict[Any, Any] | dict[Any, Any]:
        """
        create a trade order

        https://coinmate.docs.apiary.io/#reference/order/buy-limit-order/post
        https://coinmate.docs.apiary.io/#reference/order/sell-limit-order/post
        https://coinmate.docs.apiary.io/#reference/order/buy-instant-order/post
        https://coinmate.docs.apiary.io/#reference/order/sell-instant-order/post

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """
        fetches information on an order made by the user

        https://coinmate.docs.apiary.io/#reference/order/get-order-by-orderid/post
        https://coinmate.docs.apiary.io/#reference/order/get-order-by-clientorderid/post

        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def cancel_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """
        cancels an open order

        https://coinmate.docs.apiary.io/#reference/order/cancel-order/post

        :param str id: order id
        :param str symbol: not used by coinmate cancelOrder()
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def nonce(self): # -> int:
        ...
    
    def sign(self, path, api=..., method=..., params=..., headers=..., body=...): # -> dict[str, Any]:
        ...
    
    def handle_errors(self, code: int, reason: str, url: str, method: str, headers: dict, body: str, response, requestHeaders, requestBody): # -> None:
        ...
    


