"""
This type stub file was generated by pyright.
"""

from ccxt.base.exchange import Exchange
from ccxt.abstract.bitfinex import ImplicitAPI
from ccxt.base.types import Balances, Currencies, Currency, DepositAddress, FundingRate, FundingRates, Int, LedgerEntry, MarginModification, Market, Num, Order, OrderBook, OrderRequest, OrderSide, OrderType, Str, Strings, Ticker, Tickers, Trade, TradingFees, Transaction, TransferEntry
from typing import List

class bitfinex(Exchange, ImplicitAPI):
    def describe(self): # -> dict[Any, Any] | None:
        ...
    
    def is_fiat(self, code): # -> bool:
        ...
    
    def get_currency_id(self, code):
        ...
    
    def get_currency_name(self, code): # -> dict[str, str]:
        ...
    
    def amount_to_precision(self, symbol, amount):
        ...
    
    def price_to_precision(self, symbol, price):
        ...
    
    def fetch_status(self, params=...): # -> dict[str, Any]:
        """
        the latest known information on the availability of the exchange API

        https://docs.bitfinex.com/reference/rest-public-platform-status

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `status structure <https://docs.ccxt.com/#/?id=exchange-status-structure>`
        """
        ...
    
    def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for bitfinex

        https://docs.bitfinex.com/reference/rest-public-conf

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...
    
    def fetch_currencies(self, params=...) -> Currencies:
        """
        fetches all available currencies on an exchange

        https://docs.bitfinex.com/reference/rest-public-conf

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an associative dictionary of currencies
        """
        ...
    
    def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://docs.bitfinex.com/reference/rest-auth-wallets

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...
    
    def transfer(self, code: str, amount: float, fromAccount: str, toAccount: str, params=...) -> TransferEntry:
        """
        transfer currency internally between wallets on the same account

        https://docs.bitfinex.com/reference/rest-auth-transfer

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
    
    def convert_derivatives_id(self, currency, type): # -> str | None:
        ...
    
    def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://docs.bitfinex.com/reference/rest-public-book

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return, bitfinex only allows 1, 25, or 100
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...
    
    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker:
        ...
    
    def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://docs.bitfinex.com/reference/rest-public-tickers

        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://docs.bitfinex.com/reference/rest-public-ticker

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def parse_trade(self, trade: dict, market: Market = ...) -> Trade:
        ...
    
    def fetch_trades(self, symbol: str, since: Int = ..., limit: Int = ..., params=...) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://docs.bitfinex.com/reference/rest-public-trades

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch, default 120, max 10000
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [available parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :param int [params.until]: the latest time in ms to fetch entries for
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...
    
    def fetch_ohlcv(self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...) -> List[list]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://docs.bitfinex.com/reference/rest-public-candles

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch, default 100 max 10000
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        :param int [params.until]: timestamp in ms of the latest candle to fetch
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [available parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        """
        ...
    
    def parse_ohlcv(self, ohlcv, market: Market = ...) -> list:
        ...
    
    def parse_order_status(self, status: Str): # -> str | None:
        ...
    
    def parse_order_flags(self, flags): # -> None:
        ...
    
    def parse_time_in_force(self, orderType): # -> str | None:
        ...
    
    def parse_order(self, order: dict, market: Market = ...) -> Order:
        ...
    
    def create_order_request(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = ..., params=...): # -> OrderedDict[Any, Any] | dict[Any, Any]:
        """
 @ignore
        helper function to build an order request
        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much you want to trade in units of the base currency
        :param float [price]: the price of the order, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param float [params.triggerPrice]: The price at which a trigger order is triggered at
        :param str [params.timeInForce]: "GTC", "IOC", "FOK", or "PO"
        :param bool [params.postOnly]:
        :param bool [params.reduceOnly]: Ensures that the executed order does not flip the opened position.
        :param int [params.flags]: additional order parameters: 4096(Post Only), 1024(Reduce Only), 16384(OCO), 64(Hidden), 512(Close), 524288(No Var Rates)
        :param int [params.lev]: leverage for a derivative order, supported by derivative symbol orders only. The value should be between 1 and 100 inclusive.
        :param str [params.price_traling]: The trailing price for a trailing stop order
        :param str [params.price_aux_limit]: Order price for stop limit orders
        :param str [params.price_oco_stop]: OCO stop price
        :returns dict: an `order structure <https://github.com/ccxt/ccxt/wiki/Manual#order-structure>`
        """
        ...
    
    def create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = ..., params=...): # -> Order:
        """
        create an order on the exchange

        https://docs.bitfinex.com/reference/rest-auth-submit-order

        :param str symbol: unified CCXT market symbol
        :param str type: 'limit' or 'market'
        :param str side: 'buy' or 'sell'
        :param float amount: the amount of currency to trade
        :param float [price]: price of the order
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param float [params.triggerPrice]: the price that triggers a trigger order
        :param str [params.timeInForce]: "GTC", "IOC", "FOK", or "PO"
        :param boolean [params.postOnly]: set to True if you want to make a post only order
        :param boolean [params.reduceOnly]: indicates that the order is to reduce the size of a position
        :param int [params.flags]: additional order parameters: 4096(Post Only), 1024(Reduce Only), 16384(OCO), 64(Hidden), 512(Close), 524288(No Var Rates)
        :param int [params.lev]: leverage for a derivative order, supported by derivative symbol orders only. The value should be between 1 and 100 inclusive.
        :param str [params.price_aux_limit]: order price for stop limit orders
        :param str [params.price_oco_stop]: OCO stop price
        :param str [params.trailingAmount]: *swap only* the quote amount to trail away from the current market price
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def create_orders(self, orders: List[OrderRequest], params=...): # -> list[Any] | list[object]:
        """
        create a list of trade orders

        https://docs.bitfinex.com/reference/rest-auth-order-multi

        :param Array orders: list of orders to create, each object should contain the parameters required by createOrder, namely symbol, type, side, amount, price and params
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def cancel_all_orders(self, symbol: Str = ..., params=...): # -> list[Any] | list[object]:
        """
        cancel all open orders

        https://docs.bitfinex.com/reference/rest-auth-cancel-orders-multiple

        :param str symbol: unified market symbol, only orders in the market of self symbol are cancelled when symbol is not None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def cancel_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """
        cancels an open order

        https://docs.bitfinex.com/reference/rest-auth-cancel-order

        :param str id: order id
        :param str symbol: Not used by bitfinex cancelOrder()
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def cancel_orders(self, ids, symbol: Str = ..., params=...): # -> list[Any] | list[object]:
        """
        cancel multiple orders at the same time

        https://docs.bitfinex.com/reference/rest-auth-cancel-orders-multiple

        :param str[] ids: order ids
        :param str symbol: unified market symbol, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an array of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_open_order(self, id: str, symbol: Str = ..., params=...):
        """
        fetch an open order by it's id

        https://docs.bitfinex.com/reference/rest-auth-retrieve-orders
        https://docs.bitfinex.com/reference/rest-auth-retrieve-orders-by-symbol

        :param str id: order id
        :param str symbol: unified market symbol, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_closed_order(self, id: str, symbol: Str = ..., params=...):
        """
        fetch an open order by it's id

        https://docs.bitfinex.com/reference/rest-auth-retrieve-orders
        https://docs.bitfinex.com/reference/rest-auth-retrieve-orders-by-symbol

        :param str id: order id
        :param str symbol: unified market symbol, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_open_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://docs.bitfinex.com/reference/rest-auth-retrieve-orders
        https://docs.bitfinex.com/reference/rest-auth-retrieve-orders-by-symbol

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

        https://docs.bitfinex.com/reference/rest-auth-retrieve-orders
        https://docs.bitfinex.com/reference/rest-auth-retrieve-orders-by-symbol

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: the latest time in ms to fetch entries for
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_order_trades(self, id: str, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetch all the trades made from a single order

        https://docs.bitfinex.com/reference/rest-auth-order-trades

        :param str id: order id
        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...
    
    def fetch_my_trades(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetch all trades made by the user

        https://docs.bitfinex.com/reference/rest-auth-trades
        https://docs.bitfinex.com/reference/rest-auth-trades-by-symbol

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...
    
    def create_deposit_address(self, code: str, params=...): # -> DepositAddress:
        """
        create a currency deposit address

        https://docs.bitfinex.com/reference/rest-auth-deposit-address

        :param str code: unified currency code of the currency for the deposit address
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...
    
    def fetch_deposit_address(self, code: str, params=...) -> DepositAddress:
        """
        fetch the deposit address for a currency associated with self account

        https://docs.bitfinex.com/reference/rest-auth-deposit-address

        :param str code: unified currency code
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...
    
    def parse_transaction_status(self, status: Str): # -> str | None:
        ...
    
    def parse_transaction(self, transaction: dict, currency: Currency = ...) -> Transaction:
        ...
    
    def fetch_trading_fees(self, params=...) -> TradingFees:
        """
        fetch the trading fees for multiple markets

        https://docs.bitfinex.com/reference/rest-auth-summary

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `fee structures <https://docs.ccxt.com/#/?id=fee-structure>` indexed by market symbols
        """
        ...
    
    def fetch_deposits_withdrawals(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Transaction]:
        """
        fetch history of deposits and withdrawals

        https://docs.bitfinex.com/reference/movement-info
        https://docs.bitfinex.com/reference/rest-auth-movements

        :param str [code]: unified currency code for the currency of the deposit/withdrawals, default is None
        :param int [since]: timestamp in ms of the earliest deposit/withdrawal, default is None
        :param int [limit]: max number of deposit/withdrawals to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a list of `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def withdraw(self, code: str, amount: float, address: str, tag=..., params=...) -> Transaction:
        """
        make a withdrawal

        https://docs.bitfinex.com/reference/rest-auth-withdraw

        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str tag:
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def fetch_positions(self, symbols: Strings = ..., params=...): # -> dict[Any, Any] | list[Any]:
        """
        fetch all open positions

        https://docs.bitfinex.com/reference/rest-auth-positions

        :param str[]|None symbols: list of unified market symbols
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `position structure <https://docs.ccxt.com/#/?id=position-structure>`
        """
        ...
    
    def parse_position(self, position: dict, market: Market = ...): # -> dict[Any, Any]:
        ...
    
    def nonce(self): # -> int:
        ...
    
    def sign(self, path, api=..., method=..., params=..., headers=..., body=...): # -> dict[str, Any]:
        ...
    
    def handle_errors(self, statusCode, statusText, url, method, headers, body, response, requestHeaders, requestBody): # -> list[Any]:
        ...
    
    def parse_ledger_entry_type(self, type: Str): # -> str | None:
        ...
    
    def parse_ledger_entry(self, item: dict, currency: Currency = ...) -> LedgerEntry:
        ...
    
    def fetch_ledger(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[LedgerEntry]:
        """
        fetch the history of changes, actions done by the user or operations that altered the balance of the user

        https://docs.bitfinex.com/reference/rest-auth-ledgers

        :param str [code]: unified currency code, default is None
        :param int [since]: timestamp in ms of the earliest ledger entry, default is None
        :param int [limit]: max number of ledger entries to return, default is None, max is 2500
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: timestamp in ms of the latest ledger entry
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [available parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns dict: a `ledger structure <https://docs.ccxt.com/#/?id=ledger>`
        """
        ...
    
    def fetch_funding_rates(self, symbols: Strings = ..., params=...) -> FundingRates:
        """
        fetch the current funding rate for multiple symbols

        https://docs.bitfinex.com/reference/rest-public-derivatives-status

        :param str[] symbols: list of unified market symbols
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `funding rate structures <https://docs.ccxt.com/#/?id=funding-rate-structure>`
        """
        ...
    
    def fetch_funding_rate_history(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetches historical funding rate prices

        https://docs.bitfinex.com/reference/rest-public-derivatives-status-history

        :param str symbol: unified market symbol
        :param int [since]: timestamp in ms of the earliest funding rate entry
        :param int [limit]: max number of funding rate entrys to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: timestamp in ms of the latest funding rate
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [available parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns dict: a `funding rate structure <https://docs.ccxt.com/#/?id=funding-rate-structure>`
        """
        ...
    
    def parse_funding_rate(self, contract, market: Market = ...) -> FundingRate:
        ...
    
    def parse_funding_rate_history(self, contract, market: Market = ...): # -> dict[str, Any]:
        ...
    
    def fetch_open_interests(self, symbols: Strings = ..., params=...): # -> dict[Any, Any] | list[Any]:
        """
        Retrieves the open interest for a list of symbols

        https://docs.bitfinex.com/reference/rest-public-derivatives-status

        :param str[] [symbols]: a list of unified CCXT market symbols
        :param dict [params]: exchange specific parameters
        :returns dict[]: a list of `open interest structures <https://docs.ccxt.com/#/?id=open-interest-structure>`
        """
        ...
    
    def fetch_open_interest(self, symbol: str, params=...): # -> OrderedDict[Any, Any] | dict[Any, Any]:
        """
        retrieves the open interest of a contract trading pair

        https://docs.bitfinex.com/reference/rest-public-derivatives-status

        :param str symbol: unified CCXT market symbol
        :param dict [params]: exchange specific parameters
        :returns dict: an `open interest structure <https://docs.ccxt.com/#/?id=open-interest-structure>`
        """
        ...
    
    def fetch_open_interest_history(self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        retrieves the open interest history of a currency

        https://docs.bitfinex.com/reference/rest-public-derivatives-status-history

        :param str symbol: unified CCXT market symbol
        :param str timeframe: the time period of each row of data, not used by bitfinex
        :param int [since]: the time in ms of the earliest record to retrieve unix timestamp
        :param int [limit]: the number of records in the response
        :param dict [params]: exchange specific parameters
        :param int [params.until]: the time in ms of the latest record to retrieve unix timestamp
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [available parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns: An array of `open interest structures <https://docs.ccxt.com/#/?id=open-interest-structure>`
        """
        ...
    
    def parse_open_interest(self, interest, market: Market = ...): # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
    
    def fetch_liquidations(self, symbol: str, since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        retrieves the public liquidations of a trading pair

        https://docs.bitfinex.com/reference/rest-public-liquidations

        :param str symbol: unified CCXT market symbol
        :param int [since]: the earliest time in ms to fetch liquidations for
        :param int [limit]: the maximum number of liquidation structures to retrieve
        :param dict [params]: exchange specific parameters
        :param int [params.until]: timestamp in ms of the latest liquidation
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [available parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns dict: an array of `liquidation structures <https://docs.ccxt.com/#/?id=liquidation-structure>`
        """
        ...
    
    def parse_liquidation(self, liquidation, market: Market = ...): # -> dict[Any, Any]:
        ...
    
    def set_margin(self, symbol: str, amount: float, params=...) -> MarginModification:
        """
        either adds or reduces margin in a swap position in order to set the margin to a specific value

        https://docs.bitfinex.com/reference/rest-auth-deriv-pos-collateral-set

        :param str symbol: unified market symbol of the market to set margin in
        :param float amount: the amount to set the margin to
        :param dict [params]: parameters specific to the exchange API endpoint
        :returns dict: A `margin structure <https://github.com/ccxt/ccxt/wiki/Manual#add-margin-structure>`
        """
        ...
    
    def parse_margin_modification(self, data, market=...) -> MarginModification:
        ...
    
    def fetch_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """
        fetches information on an order made by the user

        https://docs.bitfinex.com/reference/rest-auth-retrieve-orders
        https://docs.bitfinex.com/reference/rest-auth-retrieve-orders-by-symbol

        :param str id: the order id
        :param str [symbol]: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def edit_order(self, id: str, symbol: str, type: OrderType, side: OrderSide, amount: Num = ..., price: Num = ..., params=...): # -> Order:
        """
        edit a trade order

        https://docs.bitfinex.com/reference/rest-auth-update-order

        :param str id: edit order id
        :param str symbol: unified symbol of the market to edit an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much you want to trade in units of the base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param float [params.triggerPrice]: the price that triggers a trigger order
        :param boolean [params.postOnly]: set to True if you want to make a post only order
        :param boolean [params.reduceOnly]: indicates that the order is to reduce the size of a position
        :param int [params.flags]: additional order parameters: 4096(Post Only), 1024(Reduce Only), 16384(OCO), 64(Hidden), 512(Close), 524288(No Var Rates)
        :param int [params.leverage]: leverage for a derivative order, supported by derivative symbol orders only, the value should be between 1 and 100 inclusive
        :param int [params.clientOrderId]: a unique client order id for the order
        :param float [params.trailingAmount]: *swap only* the quote amount to trail away from the current market price
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    


