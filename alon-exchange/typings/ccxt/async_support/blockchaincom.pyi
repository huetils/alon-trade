"""
This type stub file was generated by pyright.
"""

from ccxt.async_support.base.exchange import Exchange
from ccxt.abstract.blockchaincom import ImplicitAPI
from ccxt.base.types import Balances, Currency, DepositAddress, Int, Market, Num, Order, OrderBook, OrderSide, OrderType, Str, Strings, Ticker, Tickers, Trade, TradingFees, Transaction
from typing import List

class blockchaincom(Exchange, ImplicitAPI):
    def describe(self): # -> dict[Any, Any] | None:
        ...
    
    async def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for blockchaincom

        https://api.blockchain.com/v3/#getsymbols

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...
    
    async def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://api.blockchain.com/v3/#getl3orderbook

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...
    
    async def fetch_l3_order_book(self, symbol: str, limit: Int = ..., params=...): # -> dict[str, Any]:
        """
        fetches level 3 information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://api.blockchain.com/v3/#getl3orderbook

        :param str symbol: unified market symbol
        :param int [limit]: max number of orders to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order book structure <https://docs.ccxt.com/#/?id=order-book-structure>`
        """
        ...
    
    async def fetch_l2_order_book(self, symbol: str, limit: Int = ..., params=...): # -> dict[str, Any]:
        ...
    
    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker:
        ...
    
    async def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://api.blockchain.com/v3/#gettickerbysymbol

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    async def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://api.blockchain.com/v3/#gettickers

        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def parse_order_state(self, state): # -> str | None:
        ...
    
    def parse_order(self, order: dict, market: Market = ...) -> Order:
        ...
    
    async def create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = ..., params=...): # -> Order:
        """
        create a trade order

        https://api.blockchain.com/v3/#createorder

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def cancel_order(self, id: str, symbol: Str = ..., params=...): # -> OrderedDict[Any, Any] | dict[Any, Any]:
        """
        cancels an open order

        https://api.blockchain.com/v3/#deleteorder

        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def cancel_all_orders(self, symbol: Str = ..., params=...): # -> list[OrderedDict[Any, Any] | dict[Any, Any]]:
        """
        cancel all open orders

        https://api.blockchain.com/v3/#deleteallorders

        :param str symbol: unified market symbol of the market to cancel orders in, all markets are used if None, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_trading_fees(self, params=...) -> TradingFees:
        """
        fetch the trading fees for multiple markets

        https://api.blockchain.com/v3/#getfees

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `fee structures <https://docs.ccxt.com/#/?id=fee-structure>` indexed by market symbols
        """
        ...
    
    async def fetch_canceled_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetches information on multiple canceled orders made by the user

        https://api.blockchain.com/v3/#getorders

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: timestamp in ms of the earliest order, default is None
        :param int [limit]: max number of orders to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_closed_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """
        fetches information on multiple closed orders made by the user

        https://api.blockchain.com/v3/#getorders

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

        https://api.blockchain.com/v3/#getorders

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_orders_by_state(self, state, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        ...
    
    def parse_trade(self, trade: dict, market: Market = ...) -> Trade:
        ...
    
    async def fetch_my_trades(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetch all trades made by the user

        https://api.blockchain.com/v3/#getfills

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...
    
    async def fetch_deposit_address(self, code: str, params=...) -> DepositAddress:
        """
        fetch the deposit address for a currency associated with self account

        https://api.blockchain.com/v3/#getdepositaddress

        :param str code: unified currency code
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...
    
    def parse_transaction_state(self, state): # -> str | None:
        ...
    
    def parse_transaction(self, transaction: dict, currency: Currency = ...) -> Transaction:
        ...
    
    async def withdraw(self, code: str, amount: float, address: str, tag=..., params=...) -> Transaction:
        """
        make a withdrawal

        https://api.blockchain.com/v3/#createwithdrawal

        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str tag:
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    async def fetch_withdrawals(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Transaction]:
        """
        fetch all withdrawals made from an account

        https://api.blockchain.com/v3/#getwithdrawals

        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch withdrawals for
        :param int [limit]: the maximum number of withdrawals structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    async def fetch_withdrawal(self, id: str, code: Str = ..., params=...): # -> Transaction:
        """
        fetch data on a currency withdrawal via the withdrawal id

        https://api.blockchain.com/v3/#getwithdrawalbyid

        :param str id: withdrawal id
        :param str code: not used by blockchaincom.fetchWithdrawal
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    async def fetch_deposits(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Transaction]:
        """
        fetch all deposits made to an account

        https://api.blockchain.com/v3/#getdeposits

        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch deposits for
        :param int [limit]: the maximum number of deposits structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    async def fetch_deposit(self, id: str, code: Str = ..., params=...): # -> Transaction:
        """
        fetch information on a deposit

        https://api.blockchain.com/v3/#getdepositbyid

        :param str id: deposit id
        :param str code: not used by blockchaincom fetchDeposit()
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    async def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://api.blockchain.com/v3/#getaccounts

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...
    
    async def fetch_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """
        fetches information on an order made by the user

        https://api.blockchain.com/v3/#getorderbyid

        :param str id: the order id
        :param str symbol: not used by blockchaincom fetchOrder
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def sign(self, path, api=..., method=..., params=..., headers=..., body=...): # -> dict[str, Any]:
        ...
    
    def handle_errors(self, code: int, reason: str, url: str, method: str, headers: dict, body: str, response, requestHeaders, requestBody): # -> None:
        ...
    


