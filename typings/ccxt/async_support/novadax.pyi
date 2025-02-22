"""
This type stub file was generated by pyright.
"""

from ccxt.async_support.base.exchange import Exchange
from ccxt.abstract.novadax import ImplicitAPI
from ccxt.base.types import Account, Balances, Currency, Int, Market, Num, Order, OrderBook, OrderSide, OrderType, Str, Strings, Ticker, Tickers, Trade, Transaction, TransferEntry
from typing import List

class novadax(Exchange, ImplicitAPI):
    def describe(self): # -> dict[Any, Any] | None:
        ...
    
    async def fetch_time(self, params=...): # -> int | None:
        """
        fetches the current integer timestamp in milliseconds from the exchange server

        https://doc.novadax.com/en-US/#get-current-system-time

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int: the current integer timestamp in milliseconds from the exchange server
        """
        ...
    
    async def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for novadax

        https://doc.novadax.com/en-US/#get-all-supported-trading-symbol

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...
    
    def parse_market(self, market: dict) -> Market:
        ...
    
    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker:
        ...
    
    async def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://doc.novadax.com/en-US/#get-latest-ticker-for-specific-pair

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    async def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://doc.novadax.com/en-US/#get-latest-tickers-for-all-trading-pairs

        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    async def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://doc.novadax.com/en-US/#get-market-depth

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...
    
    def parse_trade(self, trade: dict, market: Market = ...) -> Trade:
        ...
    
    async def fetch_trades(self, symbol: str, since: Int = ..., limit: Int = ..., params=...) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://doc.novadax.com/en-US/#get-recent-trades

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...
    
    async def fetch_ohlcv(self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...) -> List[list]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://doc.novadax.com/en-US/#get-kline-data

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...
    
    def parse_ohlcv(self, ohlcv, market: Market = ...) -> list:
        ...
    
    def parse_balance(self, response) -> Balances:
        ...
    
    async def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://doc.novadax.com/en-US/#get-account-balance

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...
    
    async def create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = ..., params=...): # -> Order:
        """
        create a trade order

        https://doc.novadax.com/en-US/#order-introduction

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much you want to trade in units of the base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param float [params.cost]: for spot market buy orders, the quote quantity that can be used alternative for the amount
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def cancel_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """
        cancels an open order

        https://doc.novadax.com/en-US/#cancel-an-order

        :param str id: order id
        :param str symbol: not used by novadax cancelOrder()
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """
        fetches information on an order made by the user

        https://doc.novadax.com/en-US/#get-order-details

        :param str id: order id
        :param str symbol: not used by novadax fetchOrder
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """
        fetches information on multiple orders made by the user

        https://doc.novadax.com/en-US/#get-order-history

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_open_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://doc.novadax.com/en-US/#get-order-history

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_closed_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """
        fetches information on multiple closed orders made by the user

        https://doc.novadax.com/en-US/#get-order-history

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_order_trades(self, id: str, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetch all the trades made from a single order

        https://doc.novadax.com/en-US/#get-order-match-details

        :param str id: order id
        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...
    
    def parse_order_status(self, status: Str): # -> str | None:
        ...
    
    def parse_order(self, order: dict, market: Market = ...) -> Order:
        ...
    
    async def transfer(self, code: str, amount: float, fromAccount: str, toAccount: str, params=...) -> TransferEntry:
        """
        transfer currency internally between wallets on the same account

        https://doc.novadax.com/en-US/#get-sub-account-transfer

        :param str code: unified currency code
        :param float amount: amount to transfer
        :param str fromAccount: account to transfer from
        :param str toAccount: account to transfer to
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transfer structure <https://docs.ccxt.com/#/?id=transfer-structure>`
        """
        ...
    
    def parse_transfer(self, transfer: dict, currency: Currency = ...) -> TransferEntry:
        ...
    
    def parse_transfer_status(self, status: Str) -> Str:
        ...
    
    async def withdraw(self, code: str, amount: float, address: str, tag=..., params=...) -> Transaction:
        """
        make a withdrawal

        https://doc.novadax.com/en-US/#send-cryptocurrencies

        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str tag:
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    async def fetch_accounts(self, params=...) -> List[Account]:
        """
        fetch all the accounts associated with a profile

        https://doc.novadax.com/en-US/#get-sub-account-list

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `account structures <https://docs.ccxt.com/#/?id=account-structure>` indexed by the account type
        """
        ...
    
    async def fetch_deposits(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Transaction]:
        """
        fetch all deposits made to an account

        https://doc.novadax.com/en-US/#wallet-records-of-deposits-and-withdraws

        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch deposits for
        :param int [limit]: the maximum number of deposits structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    async def fetch_withdrawals(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Transaction]:
        """
        fetch all withdrawals made from an account

        https://doc.novadax.com/en-US/#wallet-records-of-deposits-and-withdraws

        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch withdrawals for
        :param int [limit]: the maximum number of withdrawals structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    async def fetch_deposits_withdrawals(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Transaction]:
        """
        fetch history of deposits and withdrawals

        https://doc.novadax.com/en-US/#wallet-records-of-deposits-and-withdraws

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
    
    async def fetch_my_trades(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetch all trades made by the user

        https://doc.novadax.com/en-US/#get-order-history

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...
    
    def sign(self, path, api=..., method=..., params=..., headers=..., body=...): # -> dict[str, Any]:
        ...
    
    def handle_errors(self, code: int, reason: str, url: str, method: str, headers: dict, body: str, response, requestHeaders, requestBody): # -> None:
        ...
    


