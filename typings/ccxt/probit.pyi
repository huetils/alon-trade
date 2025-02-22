"""
This type stub file was generated by pyright.
"""

from ccxt.base.exchange import Exchange
from ccxt.abstract.probit import ImplicitAPI
from ccxt.base.types import Balances, Currencies, Currency, DepositAddress, Int, Market, Num, Order, OrderBook, OrderSide, OrderType, Str, Strings, Ticker, Tickers, Trade, Transaction
from typing import List

class probit(Exchange, ImplicitAPI):
    def describe(self): # -> dict[Any, Any] | None:
        ...
    
    def fetch_markets(self, params=...) -> List[Market]:
        """

        https://docs-en.probit.com/reference/market

        retrieves data on all markets for probit
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...
    
    def parse_market(self, market: dict) -> Market:
        ...
    
    def fetch_currencies(self, params=...) -> Currencies:
        """

        https://docs-en.probit.com/reference/currency

        fetches all available currencies on an exchange
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an associative dictionary of currencies
        """
        ...
    
    def parse_balance(self, response) -> Balances:
        ...
    
    def fetch_balance(self, params=...) -> Balances:
        """

        https://docs-en.probit.com/reference/balance

        query for balance and get the amount of funds available for trading or funds locked in orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...
    
    def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """

        https://docs-en.probit.com/reference/order_book

        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...
    
    def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """

        https://docs-en.probit.com/reference/ticker

        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market
        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """

        https://docs-en.probit.com/reference/ticker

        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market
        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker:
        ...
    
    def fetch_my_trades(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """

        https://docs-en.probit.com/reference/trade

        fetch all trades made by the user
        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...
    
    def fetch_trades(self, symbol: str, since: Int = ..., limit: Int = ..., params=...) -> List[Trade]:
        """

        https://docs-en.probit.com/reference/trade-1

        get the list of most recent trades for a particular symbol
        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...
    
    def parse_trade(self, trade: dict, market: Market = ...) -> Trade:
        ...
    
    def fetch_time(self, params=...): # -> int | None:
        """

        https://docs-en.probit.com/reference/time

        fetches the current integer timestamp in milliseconds from the exchange server
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int: the current integer timestamp in milliseconds from the exchange server
        """
        ...
    
    def normalize_ohlcv_timestamp(self, timestamp, timeframe, after=...): # -> Str:
        ...
    
    def fetch_ohlcv(self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...) -> List[list]:
        """

        https://docs-en.probit.com/reference/candle

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
    
    def fetch_open_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """

        https://docs-en.probit.com/reference/open_order-1

        fetch all unfilled currently open orders
        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_closed_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """

        https://docs-en.probit.com/reference/order

        fetches information on multiple closed orders made by the user
        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """

        https://docs-en.probit.com/reference/order-3

        fetches information on an order made by the user
        :param str id: the order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def parse_order_status(self, status: Str): # -> str | None:
        ...
    
    def parse_order(self, order: dict, market: Market = ...) -> Order:
        ...
    
    def cost_to_precision(self, symbol, cost):
        ...
    
    def create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = ..., params=...): # -> Order:
        """
        create a trade order

        https://docs-en.probit.com/reference/order-1

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much you want to trade in units of the base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param float [params.cost]: the quote quantity that can be used alternative for the amount for market buy orders
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def cancel_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """

        https://docs-en.probit.com/reference/order-2

        cancels an open order
        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def parse_deposit_address(self, depositAddress, currency: Currency = ...) -> DepositAddress:
        ...
    
    def fetch_deposit_address(self, code: str, params=...) -> DepositAddress:
        """

        https://docs-en.probit.com/reference/deposit_address

        fetch the deposit address for a currency associated with self account
        :param str code: unified currency code
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...
    
    def fetch_deposit_addresses(self, codes: Strings = ..., params=...) -> List[DepositAddress]:
        """

        https://docs-en.probit.com/reference/deposit_address

        fetch deposit addresses for multiple currencies and chain types
        :param str[]|None codes: list of unified currency codes, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a list of `address structures <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...
    
    def withdraw(self, code: str, amount: float, address: str, tag=..., params=...) -> Transaction:
        """

        https://docs-en.probit.com/reference/withdrawal

        make a withdrawal
        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str tag:
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def fetch_deposits(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Transaction]:
        """
        fetch all deposits made to an account
        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch deposits for
        :param int [limit]: the maximum number of transaction structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def fetch_withdrawals(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Transaction]:
        """
        fetch all withdrawals made to an account
        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch withdrawals for
        :param int [limit]: the maximum number of transaction structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def fetch_deposits_withdrawals(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetch history of deposits and withdrawals

        https://docs-en.probit.com/reference/transferpayment

        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch transactions for
        :param int [limit]: the maximum number of transaction structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: the latest time in ms to fetch transactions for
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def parse_transaction(self, transaction: dict, currency: Currency = ...) -> Transaction:
        ...
    
    def parse_transaction_status(self, status: Str): # -> str | None:
        ...
    
    def fetch_deposit_withdraw_fees(self, codes: Strings = ..., params=...): # -> dict[Any, Any]:
        """

        https://docs-en.probit.com/reference/currency

        fetch deposit and withdraw fees
        :param str[]|None codes: list of unified currency codes
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `fees structures <https://docs.ccxt.com/#/?id=fee-structure>`
        """
        ...
    
    def parse_deposit_withdraw_fee(self, fee, currency: Currency = ...): # -> dict[str, Any]:
        ...
    
    def nonce(self): # -> int:
        ...
    
    def sign(self, path, api=..., method=..., params=..., headers=..., body=...): # -> dict[str, Any]:
        ...
    
    def sign_in(self, params=...): # -> Any:
        """

        https://docs-en.probit.com/reference/token

        sign in, must be called prior to using other authenticated methods
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns: response from exchange
        """
        ...
    
    def handle_errors(self, code: int, reason: str, url: str, method: str, headers: dict, body: str, response, requestHeaders, requestBody): # -> None:
        ...
    


