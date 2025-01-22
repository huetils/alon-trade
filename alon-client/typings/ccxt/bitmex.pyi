"""
This type stub file was generated by pyright.
"""

from ccxt.base.exchange import Exchange
from ccxt.abstract.bitmex import ImplicitAPI
from ccxt.base.types import Balances, Currencies, Currency, DepositAddress, FundingRate, FundingRates, Int, LedgerEntry, Leverage, Leverages, Market, Num, Order, OrderBook, OrderSide, OrderType, Str, Strings, Ticker, Tickers, Trade, Transaction
from typing import List

class bitmex(Exchange, ImplicitAPI):
    def describe(self): # -> dict[Any, Any] | None:
        ...
    
    def fetch_currencies(self, params=...) -> Currencies:
        """
        fetches all available currencies on an exchange

        https://www.bitmex.com/api/explorer/#not /Wallet/Wallet_getAssetsConfig

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an associative dictionary of currencies
        """
        ...
    
    def convert_from_real_amount(self, code, amount): # -> None:
        ...
    
    def convert_to_real_amount(self, code: Str, amount: Str): # -> Str:
        ...
    
    def amount_to_precision(self, symbol, amount):
        ...
    
    def convert_from_raw_quantity(self, symbol, rawQuantity, currencySide=...): # -> None:
        ...
    
    def convert_from_raw_cost(self, symbol, rawQuantity): # -> None:
        ...
    
    def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for bitmex

        https://www.bitmex.com/api/explorer/#not /Instrument/Instrument_getActive

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...
    
    def parse_market(self, market: dict) -> Market:
        ...
    
    def parse_balance(self, response) -> Balances:
        ...
    
    def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://www.bitmex.com/api/explorer/#not /User/User_getMargin

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...
    
    def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://www.bitmex.com/api/explorer/#not /OrderBook/OrderBook_getL2

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...
    
    def fetch_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """
        fetches information on an order made by the user

        https://www.bitmex.com/api/explorer/#not /Order/Order_getOrders

        :param str id: the order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """

        https://www.bitmex.com/api/explorer/#not /Order/Order_getOrders

        fetches information on multiple orders made by the user
        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: the earliest time in ms to fetch orders for
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_open_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://www.bitmex.com/api/explorer/#not /Order/Order_getOrders

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_closed_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """
        fetches information on multiple closed orders made by the user

        https://www.bitmex.com/api/explorer/#not /Order/Order_getOrders

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_my_trades(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetch all trades made by the user

        https://www.bitmex.com/api/explorer/#not /Execution/Execution_getTradeHistory

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...
    
    def parse_ledger_entry_type(self, type): # -> str | None:
        ...
    
    def parse_ledger_entry(self, item: dict, currency: Currency = ...) -> LedgerEntry:
        ...
    
    def fetch_ledger(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[LedgerEntry]:
        """
        fetch the history of changes, actions done by the user or operations that altered the balance of the user

        https://www.bitmex.com/api/explorer/#not /User/User_getWalletHistory

        :param str [code]: unified currency code, default is None
        :param int [since]: timestamp in ms of the earliest ledger entry, default is None
        :param int [limit]: max number of ledger entries to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ledger structure <https://docs.ccxt.com/#/?id=ledger>`
        """
        ...
    
    def fetch_deposits_withdrawals(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Transaction]:
        """
        fetch history of deposits and withdrawals

        https://www.bitmex.com/api/explorer/#not /User/User_getWalletHistory

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
    
    def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://www.bitmex.com/api/explorer/#not /Instrument/Instrument_get

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://www.bitmex.com/api/explorer/#not /Instrument/Instrument_getActiveAndIndices

        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker:
        ...
    
    def parse_ohlcv(self, ohlcv, market: Market = ...) -> list:
        ...
    
    def fetch_ohlcv(self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...) -> List[list]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://www.bitmex.com/api/explorer/#not /Trade/Trade_getBucketed

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...
    
    def parse_trade(self, trade: dict, market: Market = ...) -> Trade:
        ...
    
    def parse_order_status(self, status: Str): # -> str | None:
        ...
    
    def parse_time_in_force(self, timeInForce: Str): # -> str | None:
        ...
    
    def parse_order(self, order: dict, market: Market = ...) -> Order:
        ...
    
    def fetch_trades(self, symbol: str, since: Int = ..., limit: Int = ..., params=...) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://www.bitmex.com/api/explorer/#not /Trade/Trade_get

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...
    
    def create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = ..., params=...): # -> Order:
        """
        create a trade order

        https://www.bitmex.com/api/explorer/#not /Order/Order_new

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param dict [params.triggerPrice]: the price at which a trigger order is triggered at
        :param dict [params.triggerDirection]: the direction whenever the trigger happens with relation to price - 'above' or 'below'
        :param float [params.trailingAmount]: the quote amount to trail away from the current market price
        :returns dict: an `order structure <https://github.com/ccxt/ccxt/wiki/Manual#order-structure>`
        """
        ...
    
    def edit_order(self, id: str, symbol: str, type: OrderType, side: OrderSide, amount: Num = ..., price: Num = ..., params=...): # -> Order:
        ...
    
    def cancel_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """
        cancels an open order

        https://www.bitmex.com/api/explorer/#not /Order/Order_cancel

        :param str id: order id
        :param str symbol: not used by bitmex cancelOrder()
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def cancel_orders(self, ids, symbol: Str = ..., params=...): # -> list[Any] | list[object]:
        """
        cancel multiple orders

        https://www.bitmex.com/api/explorer/#not /Order/Order_cancel

        :param str[] ids: order ids
        :param str symbol: not used by bitmex cancelOrders()
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def cancel_all_orders(self, symbol: Str = ..., params=...): # -> list[Any] | list[object]:
        """
        cancel all open orders

        https://www.bitmex.com/api/explorer/#not /Order/Order_cancelAll

        :param str symbol: unified market symbol, only orders in the market of self symbol are cancelled when symbol is not None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def cancel_all_orders_after(self, timeout: Int, params=...): # -> Any:
        """
        dead man's switch, cancel all orders after the given timeout

        https://www.bitmex.com/api/explorer/#not /Order/Order_cancelAllAfter

        :param number timeout: time in milliseconds, 0 represents cancel the timer
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: the api result
        """
        ...
    
    def fetch_leverages(self, symbols: Strings = ..., params=...) -> Leverages:
        """
        fetch the set leverage for all contract markets

        https://www.bitmex.com/api/explorer/#not /Position/Position_get

        :param str[] [symbols]: a list of unified market symbols
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a list of `leverage structures <https://docs.ccxt.com/#/?id=leverage-structure>`
        """
        ...
    
    def parse_leverage(self, leverage: dict, market: Market = ...) -> Leverage:
        ...
    
    def fetch_positions(self, symbols: Strings = ..., params=...): # -> dict[Any, Any] | list[Any]:
        """
        fetch all open positions

        https://www.bitmex.com/api/explorer/#not /Position/Position_get

        :param str[]|None symbols: list of unified market symbols
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `position structure <https://docs.ccxt.com/#/?id=position-structure>`
        """
        ...
    
    def parse_position(self, position: dict, market: Market = ...): # -> dict[Any, Any]:
        ...
    
    def withdraw(self, code: str, amount: float, address: str, tag=..., params=...) -> Transaction:
        """
        make a withdrawal

        https://www.bitmex.com/api/explorer/#not /User/User_requestWithdrawal

        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str tag:
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def fetch_funding_rates(self, symbols: Strings = ..., params=...) -> FundingRates:
        """
        fetch the funding rate for multiple markets

        https://www.bitmex.com/api/explorer/#not /Instrument/Instrument_getActiveAndIndices

        :param str[]|None symbols: list of unified market symbols
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `funding rate structures <https://docs.ccxt.com/#/?id=funding-rates-structure>`, indexed by market symbols
        """
        ...
    
    def parse_funding_rate(self, contract, market: Market = ...) -> FundingRate:
        ...
    
    def fetch_funding_rate_history(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        Fetches the history of funding rates

        https://www.bitmex.com/api/explorer/#not /Funding/Funding_get

        :param str symbol: unified symbol of the market to fetch the funding rate history for
        :param int [since]: timestamp in ms of the earliest funding rate to fetch
        :param int [limit]: the maximum amount of `funding rate structures <https://docs.ccxt.com/#/?id=funding-rate-history-structure>` to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: timestamp in ms for ending date filter
        :param bool [params.reverse]: if True, will sort results newest first
        :param int [params.start]: starting point for results
        :param str [params.columns]: array of column names to fetch in info, if omitted, will return all columns
        :param str [params.filter]: generic table filter, send json key/value pairs, such as {"key": "value"}, you can key on individual fields, and do more advanced querying on timestamps, see the `timestamp docs <https://www.bitmex.com/app/restAPI#Timestamp-Filters>` for more details
        :returns dict[]: a list of `funding rate structures <https://docs.ccxt.com/#/?id=funding-rate-history-structure>`
        """
        ...
    
    def parse_funding_rate_history(self, info, market: Market = ...): # -> dict[str, Any]:
        ...
    
    def set_leverage(self, leverage: Int, symbol: Str = ..., params=...): # -> Any:
        """
        set the level of leverage for a market

        https://www.bitmex.com/api/explorer/#not /Position/Position_updateLeverage

        :param float leverage: the rate of leverage
        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: response from the exchange
        """
        ...
    
    def set_margin_mode(self, marginMode: str, symbol: Str = ..., params=...): # -> Any:
        """
        set margin mode to 'cross' or 'isolated'

        https://www.bitmex.com/api/explorer/#not /Position/Position_isolateMargin

        :param str marginMode: 'cross' or 'isolated'
        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: response from the exchange
        """
        ...
    
    def fetch_deposit_address(self, code: str, params=...) -> DepositAddress:
        """
        fetch the deposit address for a currency associated with self account

        https://www.bitmex.com/api/explorer/#not /User/User_getDepositAddress

        :param str code: unified currency code
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.network]: deposit chain, can view all chains via self.publicGetWalletAssets, default is eth, unless the currency has a default chain within self.options['networks']
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...
    
    def parse_deposit_withdraw_fee(self, fee, currency: Currency = ...): # -> dict[Any, Any]:
        ...
    
    def fetch_deposit_withdraw_fees(self, codes: Strings = ..., params=...): # -> dict[Any, Any]:
        """
        fetch deposit and withdraw fees

        https://www.bitmex.com/api/explorer/#not /Wallet/Wallet_getAssetsConfig

        :param str[]|None codes: list of unified currency codes
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a list of `fee structures <https://docs.ccxt.com/#/?id=fee-structure>`
        """
        ...
    
    def calculate_rate_limiter_cost(self, api, method, path, params, config=...): # -> Literal[20, 1] | None:
        ...
    
    def fetch_liquidations(self, symbol: str, since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        retrieves the public liquidations of a trading pair

        https://www.bitmex.com/api/explorer/#not /Liquidation/Liquidation_get

        :param str symbol: unified CCXT market symbol
        :param int [since]: the earliest time in ms to fetch liquidations for
        :param int [limit]: the maximum number of liquidation structures to retrieve
        :param dict [params]: exchange specific parameters for the bitmex api endpoint
        :param int [params.until]: timestamp in ms of the latest liquidation
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns dict: an array of `liquidation structures <https://docs.ccxt.com/#/?id=liquidation-structure>`
        """
        ...
    
    def parse_liquidation(self, liquidation, market: Market = ...): # -> dict[Any, Any]:
        ...
    
    def handle_errors(self, code: int, reason: str, url: str, method: str, headers: dict, body: str, response, requestHeaders, requestBody): # -> None:
        ...
    
    def nonce(self): # -> int:
        ...
    
    def sign(self, path, api=..., method=..., params=..., headers=..., body=...): # -> dict[str, Any]:
        ...
    


