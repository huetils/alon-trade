"""
This type stub file was generated by pyright.
"""

from ccxt.base.exchange import Exchange
from ccxt.abstract.bitso import ImplicitAPI
from ccxt.base.types import Balances, Currency, DepositAddress, Int, LedgerEntry, Market, Num, Order, OrderBook, OrderSide, OrderType, Str, Strings, Ticker, Trade, TradingFees, Transaction
from typing import List

class bitso(Exchange, ImplicitAPI):
    def describe(self): # -> dict[Any, Any] | None:
        ...
    
    def fetch_ledger(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[LedgerEntry]:
        """
        fetch the history of changes, actions done by the user or operations that altered the balance of the user
        :param str [code]: unified currency code, default is None
        :param int [since]: timestamp in ms of the earliest ledger entry, default is None
        :param int [limit]: max number of ledger entries to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ledger structure <https://docs.ccxt.com/#/?id=ledger>`
        """
        ...
    
    def parse_ledger_entry_type(self, type): # -> str | None:
        ...
    
    def parse_ledger_entry(self, item: dict, currency: Currency = ...) -> LedgerEntry:
        ...
    
    def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for bitso

        https://docs.bitso.com/bitso-api/docs/list-available-books

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...
    
    def parse_balance(self, response) -> Balances:
        ...
    
    def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://docs.bitso.com/bitso-api/docs/get-account-balance

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...
    
    def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://docs.bitso.com/bitso-api/docs/list-order-book

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

        https://docs.bitso.com/bitso-api/docs/ticker

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def fetch_ohlcv(self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...) -> List[list]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market
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
    
    def parse_trade(self, trade: dict, market: Market = ...) -> Trade:
        ...
    
    def fetch_trades(self, symbol: str, since: Int = ..., limit: Int = ..., params=...) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://docs.bitso.com/bitso-api/docs/list-trades

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...
    
    def fetch_trading_fees(self, params=...) -> TradingFees:
        """
        fetch the trading fees for multiple markets

        https://docs.bitso.com/bitso-api/docs/list-fees

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `fee structures <https://docs.ccxt.com/#/?id=fee-structure>` indexed by market symbols
        """
        ...
    
    def fetch_my_trades(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetch all trades made by the user

        https://docs.bitso.com/bitso-api/docs/user-trades

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...
    
    def create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = ..., params=...): # -> OrderedDict[Any, Any] | dict[Any, Any]:
        """
        create a trade order

        https://docs.bitso.com/bitso-api/docs/place-an-order

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def cancel_order(self, id: str, symbol: Str = ..., params=...): # -> OrderedDict[Any, Any] | dict[Any, Any]:
        """
        cancels an open order

        https://docs.bitso.com/bitso-api/docs/cancel-an-order

        :param str id: order id
        :param str symbol: not used by bitso cancelOrder()
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def cancel_orders(self, ids, symbol: Str = ..., params=...): # -> list[Any]:
        """
        cancel multiple orders

        https://docs.bitso.com/bitso-api/docs/cancel-an-order

        :param str[] ids: order ids
        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def cancel_all_orders(self, symbol: Str = ..., params=...): # -> list[Any]:
        """
        cancel all open orders

        https://docs.bitso.com/bitso-api/docs/cancel-an-order

        :param None symbol: bitso does not support canceling orders for only a specific market
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def parse_order_status(self, status: Str): # -> str | None:
        ...
    
    def parse_order(self, order: dict, market: Market = ...) -> Order:
        ...
    
    def fetch_open_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://docs.bitso.com/bitso-api/docs/list-open-orders

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """
        fetches information on an order made by the user

        https://docs.bitso.com/bitso-api/docs/look-up-orders

        :param str id: the order id
        :param str symbol: not used by bitso fetchOrder
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_order_trades(self, id: str, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetch all the trades made from a single order

        https://docs.bitso.com/bitso-api/docs/list-user-trades

        :param str id: order id
        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...
    
    def fetch_deposit(self, id: str, code: Str = ..., params=...): # -> Transaction:
        """
        fetch information on a deposit

        https://docs.bitso.com/bitso-payouts-funding/docs/fundings

        :param str id: deposit id
        :param str code: bitso does not support filtering by currency code and will ignore self argument
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def fetch_deposits(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Transaction]:
        """
        fetch all deposits made to an account

        https://docs.bitso.com/bitso-payouts-funding/docs/fundings

        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch deposits for
        :param int [limit]: the maximum number of deposits structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def fetch_deposit_address(self, code: str, params=...) -> DepositAddress:
        """
        fetch the deposit address for a currency associated with self account
        :param str code: unified currency code
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...
    
    def fetch_transaction_fees(self, codes: Strings = ..., params=...): # -> dict[Any, Any]:
        """
 @deprecated
        please use fetchDepositWithdrawFees instead

        https://docs.bitso.com/bitso-api/docs/list-fees

        :param str[]|None codes: list of unified currency codes
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `fee structures <https://docs.ccxt.com/#/?id=fee-structure>`
        """
        ...
    
    def fetch_deposit_withdraw_fees(self, codes: Strings = ..., params=...): # -> dict[Any, Any]:
        """
        fetch deposit and withdraw fees

        https://docs.bitso.com/bitso-api/docs/list-fees

        :param str[]|None codes: list of unified currency codes
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `fee structures <https://docs.ccxt.com/#/?id=fee-structure>`
        """
        ...
    
    def parse_deposit_withdraw_fees(self, response, codes=..., currencyIdKey=...): # -> dict[Any, Any]:
        ...
    
    def withdraw(self, code: str, amount: float, address: str, tag=..., params=...) -> Transaction:
        """
        make a withdrawal
        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str tag:
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def parse_transaction(self, transaction: dict, currency: Currency = ...) -> Transaction:
        ...
    
    def parse_transaction_status(self, status: Str): # -> str | None:
        ...
    
    def nonce(self): # -> int:
        ...
    
    def sign(self, path, api=..., method=..., params=..., headers=..., body=...): # -> dict[str, Any]:
        ...
    
    def handle_errors(self, httpCode: int, reason: str, url: str, method: str, headers: dict, body: str, response, requestHeaders, requestBody): # -> None:
        ...
    


