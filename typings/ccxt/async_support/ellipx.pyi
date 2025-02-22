"""
This type stub file was generated by pyright.
"""

from ccxt.async_support.base.exchange import Exchange
from ccxt.abstract.ellipx import ImplicitAPI
from ccxt.base.types import Balances, Currencies, Currency, DepositAddress, Int, Market, Num, Order, OrderBook, OrderSide, OrderType, Str, Ticker, Trade, TradingFeeInterface, Transaction
from typing import List

class ellipx(Exchange, ImplicitAPI):
    def describe(self): # -> dict[Any, Any] | None:
        ...
    
    def sign(self, path, api=..., method=..., params=..., headers=..., body=...): # -> dict[str, Any]:
        ...
    
    def calculate_mod(self, a, b):
        ...
    
    async def fetch_markets(self, params=...) -> List[Market]:
        """
        Fetches market information from the exchange.

        https://docs.ccxt.com/en/latest/manual.html#markets
        https://docs.google.com/document/d/1ZXzTQYffKE_EglTaKptxGQERRnunuLHEMmar7VC9syM/edit?tab=t.0#heading=h.1a1t05wpgfof

        :param dict [params]: - Extra parameters specific to the exchange API endpoint
        :returns Promise<Market[]>: An array of market structures.
        """
        ...
    
    def parse_market(self, market: dict) -> Market:
        ...
    
    async def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://docs.google.com/document/d/1ZXzTQYffKE_EglTaKptxGQERRnunuLHEMmar7VC9syM/edit?tab=t.0#heading=h.d2jylz4u6pmu

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker:
        ...
    
    async def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://docs.google.com/document/d/1ZXzTQYffKE_EglTaKptxGQERRnunuLHEMmar7VC9syM/edit?tab=t.0#heading=h.bqmucewhkpdz

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return the exchange not supported yet.
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...
    
    async def fetch_ohlcv(self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market, default will return the last 24h period.

        https://docs.google.com/document/d/1ZXzTQYffKE_EglTaKptxGQERRnunuLHEMmar7VC9syM/edit?tab=t.0#heading=h.w65baeuhxwt8

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the API endpoint
        :param int [params.until]: timestamp in ms of the earliest candle to fetch
        :returns OHLCV[]: A list of candles ordered, open, high, low, close, volume
        """
        ...
    
    def parse_ohlcv(self, ohlcv, market: Market = ...) -> list:
        ...
    
    async def fetch_currencies(self, params=...) -> Currencies:
        """
        fetches information on all currencies from the exchange, including deposit/withdrawal details and available chains

        https://docs.google.com/document/d/1ZXzTQYffKE_EglTaKptxGQERRnunuLHEMmar7VC9syM/edit?tab=t.0#heading=h.x65f9s9j74jf

        :param dict [params]: extra parameters specific to the ellipx API endpoint
        :param str [params.Can_Deposit]: filter currencies by deposit availability, Y for available
        :param number [params.results_per_page]: number of results per page, default 100
        :param str [params._expand]: additional fields to expand in response, default '/Crypto_Token,/Crypto_Chain'
        :returns Promise<Currencies>: An object of currency structures indexed by currency codes
        """
        ...
    
    def parse_currency(self, currency) -> Currency:
        ...
    
    async def fetch_trades(self, symbol: str, since: Int = ..., limit: Int = ..., params=...) -> List[Trade]:
        """
        fetches all completed trades for a particular market/symbol
        :param str symbol: unified market symbol(e.g. 'BTC/USDT')
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the EllipX API endpoint
        :param str [params.before]: get trades before the given trade ID
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...
    
    def parse_trade(self, trade, market=...) -> Trade:
        ...
    
    async def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://docs.google.com/document/d/1ZXzTQYffKE_EglTaKptxGQERRnunuLHEMmar7VC9syM/edit?tab=t.0#heading=h.ihrjov144txg

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...
    
    async def create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = ..., params=...): # -> Order:
        """
        create a new order in a market

        https://docs.google.com/document/d/1ZXzTQYffKE_EglTaKptxGQERRnunuLHEMmar7VC9syM/edit?tab=t.0#heading=h.yzfak2n2bwpo

        :param str symbol: unified market symbol(e.g. 'BTC/USDT')
        :param str type: order type - the exchange automatically sets type to 'limit' if price defined, 'market' if None
        :param str side: 'buy' or 'sell'
        :param float [amount]: amount of base currency to trade(can be None if using Spend_Limit)
        :param float [price]: price per unit of base currency for limit orders
        :param dict [params]: extra parameters specific to the EllipX API endpoint
        :param float [params.cost]: maximum amount to spend in quote currency(required for market orders if amount None)
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_order(self, id: str, symbol: Str = ..., params=...) -> Order:
        """
        fetches information on an order made by the user
        :param str id: the order ID by createOrder or fetchOrders
        :param str|None symbol: not used by ellipx.fetchOrder
        :param dict [params]: extra parameters specific to the EllipX API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_orders_by_status(self, status, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetches a list of orders placed on the exchange

        https://docs.google.com/document/d/1ZXzTQYffKE_EglTaKptxGQERRnunuLHEMmar7VC9syM/edit?tab=t.0#heading=h.5z2nh2b5s81n

        :param str status: 'open' or 'closed', omit for all orders
        :param str symbol: unified market symbol
        :param int [since]: timestamp in ms of the earliest order
        :param int [limit]: the maximum amount of orders to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetches information on multiple orders made by the user

        https://docs.google.com/document/d/1ZXzTQYffKE_EglTaKptxGQERRnunuLHEMmar7VC9syM/edit?tab=t.0#heading=h.5z2nh2b5s81n

        :param str symbol: unified market symbol of the market orders were made in
        :param int|None since: timestamp in ms of the earliest order
        :param int|None limit: the maximum amount of orders to fetch
        :param dict params: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_open_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """
        fetches information on open orders made by the user

        https://docs.google.com/document/d/1ZXzTQYffKE_EglTaKptxGQERRnunuLHEMmar7VC9syM/edit?tab=t.0#heading=h.5z2nh2b5s81n

        :param str symbol: unified market symbol of the market orders were made in
        :param int|None since: timestamp in ms of the earliest order
        :param int|None limit: the maximum amount of orders to fetch
        :param dict params: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def parse_order(self, order, market=...) -> Order:
        ...
    
    async def cancel_order(self, id: str, symbol: Str = ..., params=...) -> Order:
        """
        Cancels an open order on the exchange

        https://docs.google.com/document/d/1ZXzTQYffKE_EglTaKptxGQERRnunuLHEMmar7VC9syM/edit?tab=t.0#heading=h.f1qu1pb1rebn

        :param str id: - The order ID to cancel(format: mktor-xxxxx-xxxx-xxxx-xxxx-xxxxxxxx)
        :param str [symbol]: - ellipx.cancelOrder does not use the symbol parameter
        :param dict [params]: - Extra parameters specific to the exchange API
        :returns Promise<dict>: A Promise that resolves to the canceled order info
        """
        ...
    
    async def fetch_order_trades(self, id: str, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Trade]:
        """
        fetch all the trades made from a single order
        :param str id: order id
        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...
    
    async def fetch_deposit_address(self, code: str, params=...) -> DepositAddress:
        """
        fetches a crypto deposit address for a specific currency

        https://docs.google.com/document/d/1ZXzTQYffKE_EglTaKptxGQERRnunuLHEMmar7VC9syM/edit?tab=t.0#heading=h.k7qe5aricayh

        :param str code: unified currency code(e.g. "BTC", "ETH", "USDT")
        :param dict [params]: extra parameters specific to the EllipX API endpoint
        :returns dict: an address structure {
     'currency': string,  # unified currency code
     'address': string,  # the address for deposits
     'tag': string|None,  # tag/memo for deposits if needed
     'network': object,  # network object from currency info
     'info': object  # raw response from exchange
}
        :throws ExchangeError if: currency does not support deposits
        """
        ...
    
    async def fetch_trading_fee(self, symbol: str = ..., params=...) -> TradingFeeInterface:
        """
        Fetches the current trading fees(maker and taker) applicable to the user.

        https://docs.google.com/document/d/1ZXzTQYffKE_EglTaKptxGQERRnunuLHEMmar7VC9syM/edit?tab=t.0#heading=h.kki5jay2c8it

        :param str [symbol]: Not used by EllipX are not symbol-specific.
        :param dict [params]: Extra parameters specific to the EllipX API endpoint.
        :returns Promise<dict>: A promise resolving to a unified trading fee structure:
 {
     'info': object,        # the raw response from the exchange
     'symbol': None,   # symbol is not used for self exchange
     'maker': number,       # maker fee rate in decimal form
     'taker': number,       # taker fee rate in decimal form
     'percentage': True,    # indicates fees are in percentage
     'tierBased': False,    # indicates fees do not vary by volume tiers
}
        """
        ...
    
    async def withdraw(self, code: str, amount: float, address: str, tag=..., params=...) -> Transaction:
        """
        Make a withdrawal request

        https://docs.google.com/document/d/1ZXzTQYffKE_EglTaKptxGQERRnunuLHEMmar7VC9syM/edit?tab=t.0#heading=h.zegupoa8g4t9

        :param str code: Currency code
        :param number amount: Amount to withdraw
        :param str address: Destination wallet address
        :param str [tag]: Additional tag/memo for currencies that require it
        :param dict params: Extra parameters specific to the EllipX API endpoint(Crypto_Chain__, Unit__)
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def parse_transaction_status(self, status: str) -> str:
        ...
    
    def parse_order_status(self, status): # -> str | None:
        ...
    
    def parse_amount(self, amount) -> Str:
        ...
    
    def to_amount(self, amount: float, precision: float) -> dict:
        ...
    
    def handle_errors(self, code: int, reason: str, url: str, method: str, headers: dict, body: str, response, requestHeaders, requestBody): # -> None:
        ...
    


