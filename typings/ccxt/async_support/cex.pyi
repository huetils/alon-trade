"""
This type stub file was generated by pyright.
"""

from ccxt.async_support.base.exchange import Exchange
from ccxt.abstract.cex import ImplicitAPI
from ccxt.base.types import Account, Balances, Currencies, Currency, DepositAddress, Int, LedgerEntry, Market, Num, Order, OrderBook, OrderSide, OrderType, Str, Strings, Ticker, Tickers, Trade, TradingFeeInterface, TradingFees, Transaction, TransferEntry
from typing import List

class cex(Exchange, ImplicitAPI):
    def describe(self): # -> dict[Any, Any] | None:
        ...
    
    async def fetch_currencies(self, params=...) -> Currencies:
        """
        fetches all available currencies on an exchange

        https://trade.cex.io/docs/#rest-public-api-calls-currencies-info

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an associative dictionary of currencies
        """
        ...
    
    def parse_currency(self, rawCurrency: dict) -> Currency:
        ...
    
    async def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for ace

        https://trade.cex.io/docs/#rest-public-api-calls-pairs-info

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...
    
    def parse_market(self, market: dict) -> Market:
        ...
    
    async def fetch_time(self, params=...): # -> int | None:
        """
        fetches the current integer timestamp in milliseconds from the exchange server
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int: the current integer timestamp in milliseconds from the exchange server
        """
        ...
    
    async def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://trade.cex.io/docs/#rest-public-api-calls-ticker

        :param str symbol:
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    async def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://trade.cex.io/docs/#rest-public-api-calls-ticker

        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker:
        ...
    
    async def fetch_trades(self, symbol: str, since: Int = ..., limit: Int = ..., params=...) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://trade.cex.io/docs/#rest-public-api-calls-trade-history

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: timestamp in ms of the latest entry
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...
    
    def parse_trade(self, trade: dict, market: Market = ...) -> Trade:
        ...
    
    async def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://trade.cex.io/docs/#rest-public-api-calls-order-book

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...
    
    async def fetch_ohlcv(self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...) -> List[list]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://trade.cex.io/docs/#rest-public-api-calls-candles

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: timestamp in ms of the latest entry
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...
    
    def parse_ohlcv(self, ohlcv, market: Market = ...) -> list:
        ...
    
    async def fetch_trading_fees(self, params=...) -> TradingFees:
        """
        fetch the trading fees for multiple markets

        https://trade.cex.io/docs/#rest-public-api-calls-candles

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `fee structures <https://docs.ccxt.com/#/?id=fee-structure>` indexed by market symbols
        """
        ...
    
    def parse_trading_fees(self, response, useKeyAsId=...) -> TradingFees:
        ...
    
    def parse_trading_fee(self, fee: dict, market: Market = ...) -> TradingFeeInterface:
        ...
    
    async def fetch_accounts(self, params=...) -> List[Account]:
        ...
    
    def parse_account(self, account: dict) -> Account:
        ...
    
    async def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://trade.cex.io/docs/#rest-private-api-calls-account-status-v3

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param dict [params.method]: 'privatePostGetMyWalletBalance' or 'privatePostGetMyAccountStatusV3'
        :param dict [params.account]:  in case 'privatePostGetMyAccountStatusV3' is chosen, self can specify the account name(default is empty string)
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...
    
    def parse_balance(self, response) -> Balances:
        ...
    
    async def fetch_orders_by_status(self, status: str, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """
        fetches information on multiple orders made by the user

        https://trade.cex.io/docs/#rest-private-api-calls-orders

        :param str status: order status to fetch for
        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: timestamp in ms of the latest entry
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_closed_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> List[Order]:
        """

        https://trade.cex.io/docs/#rest-private-api-calls-orders

        fetches information on multiple canceled orders made by the user
        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: timestamp in ms of the earliest order, default is None
        :param int [limit]: max number of orders to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_open_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> List[Order]:
        """

        https://trade.cex.io/docs/#rest-private-api-calls-orders

        fetches information on multiple canceled orders made by the user
        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: timestamp in ms of the earliest order, default is None
        :param int [limit]: max number of orders to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_open_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """
        fetches information on an open order made by the user

        https://trade.cex.io/docs/#rest-private-api-calls-orders

        :param str id: order id
        :param str [symbol]: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_closed_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """
        fetches information on an closed order made by the user

        https://trade.cex.io/docs/#rest-private-api-calls-orders

        :param str id: order id
        :param str [symbol]: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def parse_order_status(self, status: Str): # -> str | None:
        ...
    
    def parse_order(self, order: dict, market: Market = ...) -> Order:
        ...
    
    async def create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = ..., params=...): # -> Order:
        """
        create a trade order

        https://trade.cex.io/docs/#rest-private-api-calls-new-order

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.accountId]: account-id to use(default is empty string)
        :param float [params.triggerPrice]: the price at which a trigger order is triggered at
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def cancel_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """
        cancels an open order

        https://trade.cex.io/docs/#rest-private-api-calls-cancel-order

        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def cancel_all_orders(self, symbol: Str = ..., params=...): # -> list[Any] | list[object]:
        """
        cancel all open orders in a market

        https://trade.cex.io/docs/#rest-private-api-calls-cancel-all-orders

        :param str symbol: alpaca cancelAllOrders cannot setting symbol, it will cancel all open orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_ledger(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[LedgerEntry]:
        """
        fetch the history of changes, actions done by the user or operations that altered the balance of the user

        https://trade.cex.io/docs/#rest-private-api-calls-transaction-history

        :param str [code]: unified currency code
        :param int [since]: timestamp in ms of the earliest ledger entry
        :param int [limit]: max number of ledger entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: timestamp in ms of the latest ledger entry
        :returns dict: a `ledger structure <https://docs.ccxt.com/#/?id=ledger>`
        """
        ...
    
    def parse_ledger_entry(self, item: dict, currency: Currency = ...) -> LedgerEntry:
        ...
    
    def parse_ledger_entry_type(self, type): # -> str | None:
        ...
    
    async def fetch_deposits_withdrawals(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Transaction]:
        """
        fetch history of deposits and withdrawals

        https://trade.cex.io/docs/#rest-private-api-calls-funding-history

        :param str [code]: unified currency code for the currency of the deposit/withdrawals, default is None
        :param int [since]: timestamp in ms of the earliest deposit/withdrawal, default is None
        :param int [limit]: max number of deposit/withdrawals to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a list of `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def parse_transaction(self, transaction: dict, currency: Currency = ...) -> Transaction:
        ...
    
    def parse_transaction_status(self, status: Str): # -> str | None:
        ...
    
    async def transfer(self, code: str, amount: float, fromAccount: str, toAccount: str, params=...) -> TransferEntry:
        """
        transfer currency internally between wallets on the same account

        https://trade.cex.io/docs/#rest-private-api-calls-internal-transfer

        :param str code: unified currency code
        :param float amount: amount to transfer
        :param str fromAccount: 'SPOT', 'FUND', or 'CONTRACT'
        :param str toAccount: 'SPOT', 'FUND', or 'CONTRACT'
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transfer structure <https://docs.ccxt.com/#/?id=transfer-structure>`
        """
        ...
    
    async def transfer_between_main_and_sub_account(self, code: str, amount: float, fromAccount: str, toAccount: str, params=...) -> TransferEntry:
        ...
    
    async def transfer_between_sub_accounts(self, code: str, amount: float, fromAccount: str, toAccount: str, params=...) -> TransferEntry:
        ...
    
    def parse_transfer(self, transfer: dict, currency: Currency = ...) -> TransferEntry:
        ...
    
    async def fetch_deposit_address(self, code: str, params=...) -> DepositAddress:
        """
        fetch the deposit address for a currency associated with self account

        https://trade.cex.io/docs/#rest-private-api-calls-deposit-address

        :param str code: unified currency code
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.accountId]: account-id(default to empty string) to refer to(at self moment, only sub-accounts allowed by exchange)
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...
    
    def parse_deposit_address(self, depositAddress, currency: Currency = ...) -> DepositAddress:
        ...
    
    def sign(self, path, api=..., method=..., params=..., headers=..., body=...): # -> dict[str, Any]:
        ...
    
    def handle_errors(self, code: int, reason: str, url: str, method: str, headers: dict, body: str, response, requestHeaders, requestBody): # -> None:
        ...
    


