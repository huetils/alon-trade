"""
This type stub file was generated by pyright.
"""

from ccxt.base.exchange import Exchange
from ccxt.abstract.exmo import ImplicitAPI
from ccxt.base.types import Balances, Currencies, Currency, DepositAddress, Int, MarginModification, Market, Num, Order, OrderBook, OrderSide, OrderType, Str, Strings, Ticker, Tickers, Trade, TradingFees, Transaction
from typing import List

class exmo(Exchange, ImplicitAPI):
    def describe(self): # -> dict[Any, Any] | None:
        ...
    
    def modify_margin_helper(self, symbol: str, amount, type, params=...): # -> MarginModification:
        ...
    
    def parse_margin_modification(self, data: dict, market: Market = ...) -> MarginModification:
        ...
    
    def reduce_margin(self, symbol: str, amount: float, params=...) -> MarginModification:
        """
        remove margin from a position

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#eebf9f25-0289-4946-9482-89872c738449

        :param str symbol: unified market symbol
        :param float amount: the amount of margin to remove
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `margin structure <https://docs.ccxt.com/#/?id=reduce-margin-structure>`
        """
        ...
    
    def add_margin(self, symbol: str, amount: float, params=...) -> MarginModification:
        """
        add margin

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#143ef808-79ca-4e49-9e79-a60ea4d8c0e3

        :param str symbol: unified market symbol
        :param float amount: amount of margin to add
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `margin structure <https://docs.ccxt.com/#/?id=add-margin-structure>`
        """
        ...
    
    def fetch_trading_fees(self, params=...) -> TradingFees:
        """
        fetch the trading fees for multiple markets

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#90927062-256c-4b03-900f-2b99131f9a54
        https://documenter.getpostman.com/view/10287440/SzYXWKPi#7de7e75c-5833-45a8-b937-c2276d235aaa

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `fee structures <https://docs.ccxt.com/#/?id=fee-structure>` indexed by market symbols
        """
        ...
    
    def fetch_private_trading_fees(self, params=...): # -> dict[Any, Any]:
        ...
    
    def fetch_public_trading_fees(self, params=...): # -> dict[Any, Any]:
        ...
    
    def parse_fixed_float_value(self, input): # -> float | Literal[0] | None:
        ...
    
    def fetch_transaction_fees(self, codes: Strings = ..., params=...): # -> dict[Any, Any]:
        """
 @deprecated
        please use fetchDepositWithdrawFees instead

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#4190035d-24b1-453d-833b-37e0a52f88e2

        :param str[]|None codes: list of unified currency codes
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a list of `transaction fees structures <https://docs.ccxt.com/#/?id=fees-structure>`
        """
        ...
    
    def fetch_deposit_withdraw_fees(self, codes: Strings = ..., params=...): # -> dict[Any, Any]:
        """
        fetch deposit and withdraw fees

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#4190035d-24b1-453d-833b-37e0a52f88e2

        :param str[]|None codes: list of unified currency codes
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a list of `transaction fees structures <https://docs.ccxt.com/#/?id=fees-structure>`
        """
        ...
    
    def parse_deposit_withdraw_fee(self, fee, currency: Currency = ...): # -> dict[str, Any]:
        ...
    
    def fetch_currencies(self, params=...) -> Currencies:
        """
        fetches all available currencies on an exchange

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#7cdf0ca8-9ff6-4cf3-aa33-bcec83155c49
        https://documenter.getpostman.com/view/10287440/SzYXWKPi#4190035d-24b1-453d-833b-37e0a52f88e2

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an associative dictionary of currencies
        """
        ...
    
    def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for exmo

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#7de7e75c-5833-45a8-b937-c2276d235aaa

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...
    
    def fetch_ohlcv(self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...) -> List[list]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#65eeb949-74e5-4631-9184-c38387fe53e8

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: timestamp in ms of the latest candle to fetch
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...
    
    def parse_ohlcv(self, ohlcv, market: Market = ...) -> list:
        ...
    
    def parse_balance(self, response) -> Balances:
        ...
    
    def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#59c5160f-27a1-4d9a-8cfb-7979c7ffaac6
        https://documenter.getpostman.com/view/10287440/SzYXWKPi#c8388df7-1f9f-4d41-81c4-5a387d171dc6

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.marginMode]: *isolated* fetches the isolated margin balance
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...
    
    def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#c60c51a8-e683-4f45-a000-820723d37871

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...
    
    def fetch_order_books(self, symbols: Strings = ..., limit: Int = ..., params=...): # -> dict[Any, Any]:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data for multiple markets

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#c60c51a8-e683-4f45-a000-820723d37871

        :param str[]|None symbols: list of unified market symbols, all symbols fetched if None, default is None
        :param int [limit]: max number of entries per orderbook to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbol
        """
        ...
    
    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker:
        ...
    
    def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#4c8e6459-3503-4361-b012-c34bb9f7e385

        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#4c8e6459-3503-4361-b012-c34bb9f7e385

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

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#5a5a9c0d-cf17-47f6-9d62-6d4404ebd5ac

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...
    
    def fetch_my_trades(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetch all trades made by the user

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#b8d8d9af-4f46-46a1-939b-ad261d79f452  # spot
        https://documenter.getpostman.com/view/10287440/SzYXWKPi#f4b1aaf8-399f-403b-ab5e-4926d967a106  # margin

        :param str symbol: a symbol is required but it can be a single string, or a non-empty array
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: *required for margin orders* the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint

 EXCHANGE SPECIFIC PARAMETERS
        :param int [params.offset]: last deal offset, default = 0
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...
    
    def create_market_order_with_cost(self, symbol: str, side: OrderSide, cost: float, params=...): # -> Order:
        """
        create a market order by providing the symbol, side and cost

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#80daa469-ec59-4d0a-b229-6a311d8dd1cd

        :param str symbol: unified symbol of the market to create an order in
        :param str side: 'buy' or 'sell'
        :param float cost: how much you want to trade in units of the quote currency
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def create_market_buy_order_with_cost(self, symbol: str, cost: float, params=...): # -> Order:
        """
        create a market buy order by providing the symbol and cost

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#80daa469-ec59-4d0a-b229-6a311d8dd1cd

        :param str symbol: unified symbol of the market to create an order in
        :param float cost: how much you want to trade in units of the quote currency
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def create_market_sell_order_with_cost(self, symbol: str, cost: float, params=...): # -> Order:
        """
        create a market sell order by providing the symbol and cost

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#80daa469-ec59-4d0a-b229-6a311d8dd1cd

        :param str symbol: unified symbol of the market to create an order in
        :param float cost: how much you want to trade in units of the quote currency
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = ..., params=...): # -> Order:
        """
        create a trade order

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#80daa469-ec59-4d0a-b229-6a311d8dd1cd
        https://documenter.getpostman.com/view/10287440/SzYXWKPi#de6f4321-eeac-468c-87f7-c4ad7062e265  # stop market
        https://documenter.getpostman.com/view/10287440/SzYXWKPi#3561b86c-9ff1-436e-8e68-ac926b7eb523  # margin

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param float [params.triggerPrice]: the price at which a trigger order is triggered at
        :param str [params.timeInForce]: *spot only* 'fok', 'ioc' or 'post_only'
        :param boolean [params.postOnly]: *spot only* True for post only orders
        :param float [params.cost]: *spot only* *market orders only* the cost of the order in the quote currency for market orders
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def cancel_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """
        cancels an open order

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#1f710d4b-75bc-4b65-ad68-006f863a3f26
        https://documenter.getpostman.com/view/10287440/SzYXWKPi#a4d0aae8-28f7-41ac-94fd-c4030130453d  # stop market
        https://documenter.getpostman.com/view/10287440/SzYXWKPi#705dfec5-2b35-4667-862b-faf54eca6209  # margin

        :param str id: order id
        :param str symbol: not used by exmo cancelOrder()
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.trigger]: True to cancel a trigger order
        :param str [params.marginMode]: set to 'cross' or 'isolated' to cancel a margin order
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """
        *spot only* fetches information on an order made by the user

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#cf27781e-28e5-4b39-a52d-3110f5d22459  # spot

        :param str id: order id
        :param str symbol: not used by exmo fetchOrder
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_order_trades(self, id: str, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetch all the trades made from a single order

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#cf27781e-28e5-4b39-a52d-3110f5d22459  # spot
        https://documenter.getpostman.com/view/10287440/SzYXWKPi#00810661-9119-46c5-aec5-55abe9cb42c7  # margin

        :param str id: order id
        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.marginMode]: set to "isolated" to fetch trades for a margin order
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...
    
    def fetch_open_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#0e135370-daa4-4689-8acd-b6876dee9ba1  # spot open orders
        https://documenter.getpostman.com/view/10287440/SzYXWKPi#a7cfd4f0-476e-4675-b33f-22a46902f245  # margin

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.marginMode]: set to "isolated" for margin orders
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def parse_status(self, status): # -> str | None:
        ...
    
    def parse_side(self, orderType): # -> str | None:
        ...
    
    def parse_order(self, order: dict, market: Market = ...) -> Order:
        ...
    
    def fetch_canceled_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetches information on multiple canceled orders made by the user

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#1d2524dd-ae6d-403a-a067-77b50d13fbe5  # margin
        https://documenter.getpostman.com/view/10287440/SzYXWKPi#a51be1d0-af5f-44e4-99d7-f7b04c6067d0  # spot canceled orders

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: timestamp in ms of the earliest order, default is None
        :param int [limit]: max number of orders to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.marginMode]: set to "isolated" for margin orders
        :returns dict: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def edit_order(self, id: str, symbol: str, type: OrderType, side: OrderSide, amount: Num = ..., price: Num = ..., params=...): # -> Order:
        """
        *margin only* edit a trade order

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#f27ee040-c75f-4b59-b608-d05bd45b7899  # margin

        :param str id: order id
        :param str symbol: unified CCXT market symbol
        :param str type: not used by exmo editOrder
        :param str side: not used by exmo editOrder
        :param float [amount]: how much of the currency you want to trade in units of the base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param float [params.triggerPrice]: stop price for stop-market and stop-limit orders
        :param str params['marginMode']: must be set to isolated

 EXCHANGE SPECIFIC PARAMETERS
        :param int [params.distance]: distance for trailing stop orders
        :param int [params.expire]: expiration timestamp in UTC timezone for the order. order will not be expired if expire is 0
        :param str [params.comment]: optional comment for order. up to 50 latin symbols, whitespaces, underscores
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def fetch_deposit_address(self, code: str, params=...) -> DepositAddress:
        """
        fetch the deposit address for a currency associated with self account

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#c8f9ced9-7ab6-4383-a6a4-bc54469ba60e

        :param str code: unified currency code
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...
    
    def get_market_from_trades(self, trades): # -> None:
        ...
    
    def withdraw(self, code: str, amount: float, address: str, tag=..., params=...) -> Transaction:
        """
        make a withdrawal

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#3ab9c34d-ad58-4f87-9c57-2e2ea88a8325

        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str tag:
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def parse_transaction_status(self, status: Str): # -> str | None:
        ...
    
    def parse_transaction(self, transaction: dict, currency: Currency = ...) -> Transaction:
        ...
    
    def fetch_deposits_withdrawals(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Transaction]:
        """
        fetch history of deposits and withdrawals

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#31e69a33-4849-4e6a-b4b4-6d574238f6a7

        :param str [code]: unified currency code for the currency of the deposit/withdrawals, default is None
        :param int [since]: timestamp in ms of the earliest deposit/withdrawal, default is None
        :param int [limit]: max number of deposit/withdrawals to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a list of `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def fetch_withdrawals(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Transaction]:
        """
        fetch all withdrawals made from an account

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#97f1becd-7aad-4e0e-babe-7bbe09e33706

        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch withdrawals for
        :param int [limit]: the maximum number of withdrawals structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def fetch_withdrawal(self, id: str, code: Str = ..., params=...): # -> Transaction:
        """
        fetch data on a currency withdrawal via the withdrawal id

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#97f1becd-7aad-4e0e-babe-7bbe09e33706

        :param str id: withdrawal id
        :param str code: unified currency code of the currency withdrawn, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def fetch_deposit(self, id=..., code: Str = ..., params=...): # -> Transaction:
        """
        fetch information on a deposit

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#97f1becd-7aad-4e0e-babe-7bbe09e33706

        :param str id: deposit id
        :param str code: unified currency code, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def fetch_deposits(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Transaction]:
        """
        fetch all deposits made to an account

        https://documenter.getpostman.com/view/10287440/SzYXWKPi#97f1becd-7aad-4e0e-babe-7bbe09e33706

        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch deposits for
        :param int [limit]: the maximum number of deposits structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def sign(self, path, api=..., method=..., params=..., headers=..., body=...): # -> dict[str, Any]:
        ...
    
    def nonce(self): # -> int:
        ...
    
    def handle_errors(self, httpCode: int, reason: str, url: str, method: str, headers: dict, body: str, response, requestHeaders, requestBody): # -> None:
        ...
    


