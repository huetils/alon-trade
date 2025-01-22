"""
This type stub file was generated by pyright.
"""

from ccxt.async_support.base.exchange import Exchange
from ccxt.abstract.coinbaseinternational import ImplicitAPI
from ccxt.base.types import Balances, Currencies, Currency, Int, Market, Order, OrderSide, OrderType, Position, Str, Strings, Ticker, Tickers, Trade, Transaction, TransferEntry
from typing import Any, List

class coinbaseinternational(Exchange, ImplicitAPI):
    def describe(self): # -> dict[Any, Any] | None:
        ...
    
    async def handle_portfolio_and_params(self, methodName: str, params=...): # -> list[Any]:
        ...
    
    async def handle_network_id_and_params(self, currencyCode: str, methodName: str, params): # -> list[Any]:
        ...
    
    async def fetch_accounts(self, params=...): # -> list[Any]:
        """
        fetch all the accounts associated with a profile

        https://docs.cloud.coinbase.com/intx/reference/getportfolios

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `account structures <https://docs.ccxt.com/#/?id=account-structure>` indexed by the account type
        """
        ...
    
    def parse_account(self, account): # -> dict[str, Any]:
        ...
    
    async def fetch_ohlcv(self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...) -> List[list]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://docs.cdp.coinbase.com/intx/reference/getinstrumentcandles

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
    
    async def fetch_funding_rate_history(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetches historical funding rate prices

        https://docs.cloud.coinbase.com/intx/reference/getinstrumentfunding

        :param str symbol: unified symbol of the market to fetch the funding rate history for
        :param int [since]: timestamp in ms of the earliest funding rate to fetch
        :param int [limit]: the maximum amount of `funding rate structures <https://docs.ccxt.com/#/?id=funding-rate-history-structure>` to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns dict[]: a list of `funding rate structures <https://docs.ccxt.com/#/?id=funding-rate-history-structure>`
        """
        ...
    
    def parse_funding_rate_history(self, info, market: Market = ...): # -> dict[str, Any]:
        ...
    
    def parse_funding_rate(self, contract, market: Market = ...): # -> dict[str, Any]:
        ...
    
    async def fetch_funding_history(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetch the history of funding payments paid and received on self account

        https://docs.cdp.coinbase.com/intx/reference/gettransfers

        :param str [symbol]: unified market symbol
        :param int [since]: the earliest time in ms to fetch funding history for
        :param int [limit]: the maximum number of funding history structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `funding history structure <https://docs.ccxt.com/#/?id=funding-history-structure>`
        """
        ...
    
    def parse_income(self, income, market: Market = ...): # -> dict[str, Any]:
        ...
    
    async def fetch_transfers(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[TransferEntry]:
        """
        fetch a history of internal transfers made on an account

        https://docs.cdp.coinbase.com/intx/reference/gettransfers

        :param str code: unified currency code of the currency transferred
        :param int [since]: the earliest time in ms to fetch transfers for
        :param int [limit]: the maximum number of  transfers structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transfer structures <https://docs.ccxt.com/#/?id=transfer-structure>`
        """
        ...
    
    def parse_transfer(self, transfer: dict, currency: Currency = ...) -> TransferEntry:
        ...
    
    def parse_transfer_status(self, status: Str) -> Str:
        ...
    
    async def create_deposit_address(self, code: str, params=...): # -> dict[str, Any]:
        """
        create a currency deposit address

        https://docs.cloud.coinbase.com/intx/reference/createaddress
        https://docs.cloud.coinbase.com/intx/reference/createcounterpartyid

        :param str code: unified currency code of the currency for the deposit address
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.network_arn_id]: Identifies the blockchain network(e.g., networks/ethereum-mainnet/assets/313ef8a9-ae5a-5f2f-8a56-572c0e2a4d5a) if not provided will pick default
        :param str [params.network]: unified network code to identify the blockchain network
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...
    
    def find_default_network(self, networks):
        ...
    
    async def load_currency_networks(self, code, params=...): # -> None:
        ...
    
    def parse_networks(self, networks, params=...): # -> dict[Any, Any]:
        ...
    
    def parse_network(self, network, params=...): # -> dict[str, Any]:
        ...
    
    async def set_margin(self, symbol: str, amount: float, params=...) -> Any:
        """
        Either adds or reduces margin in order to set the margin to a specific value

        https://docs.cloud.coinbase.com/intx/reference/setportfoliomarginoverride

        :param str symbol: unified market symbol of the market to set margin in
        :param float amount: the amount to set the margin to
        :param dict [params]: parameters specific to the exchange API endpoint
        :returns dict: A `margin structure <https://github.com/ccxt/ccxt/wiki/Manual#add-margin-structure>`
        """
        ...
    
    async def fetch_deposits_withdrawals(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Transaction]:
        """
        fetch history of deposits and withdrawals

        https://docs.cloud.coinbase.com/intx/reference/gettransfers

        :param str [code]: unified currency code for the currency of the deposit/withdrawals, default is None
        :param int [since]: timestamp in ms of the earliest deposit/withdrawal, default is None
        :param int [limit]: max number of deposit/withdrawals to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.portfolios]: Identifies the portfolios by UUID(e.g., 892e8c7c-e979-4cad-b61b-55a197932cf1) or portfolio ID(e.g., 5189861793641175). Can provide single or multiple portfolios to filter by or fetches transfers for all portfolios if none are provided.
        :param int [params.until]: Only find transfers updated before self time. Use timestamp format
        :param str [params.status]: The current status of transfer. Possible values: [PROCESSED, NEW, FAILED, STARTED]
        :param str [params.type]: The type of transfer Possible values: [DEPOSIT, WITHDRAW, REBATE, STIPEND, INTERNAL, FUNDING]
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns dict: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    async def fetch_position(self, symbol: str, params=...): # -> dict[Any, Any]:
        """

        https://docs.cloud.coinbase.com/intx/reference/getportfolioposition

        fetch data on an open position
        :param str symbol: unified market symbol of the market the position is held in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `position structure <https://docs.ccxt.com/#/?id=position-structure>`
        """
        ...
    
    def parse_position(self, position: dict, market: Market = ...): # -> dict[Any, Any]:
        ...
    
    async def fetch_positions(self, symbols: Strings = ..., params=...) -> List[Position]:
        """

        https://docs.cloud.coinbase.com/intx/reference/getportfoliopositions

        fetch all open positions
        :param str[] [symbols]: list of unified market symbols
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `position structure <https://docs.ccxt.com/#/?id=position-structure>`
        """
        ...
    
    async def fetch_withdrawals(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Transaction]:
        """
        fetch all withdrawals made from an account

        https://docs.cloud.coinbase.com/intx/reference/gettransfers

        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch withdrawals for
        :param int [limit]: the maximum number of withdrawals structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.portfolios]: Identifies the portfolios by UUID(e.g., 892e8c7c-e979-4cad-b61b-55a197932cf1) or portfolio ID(e.g., 5189861793641175). Can provide single or multiple portfolios to filter by or fetches transfers for all portfolios if none are provided.
        :param int [params.until]: Only find transfers updated before self time. Use timestamp format
        :param str [params.status]: The current status of transfer. Possible values: [PROCESSED, NEW, FAILED, STARTED]
        :param str [params.type]: The type of transfer Possible values: [DEPOSIT, WITHDRAW, REBATE, STIPEND, INTERNAL, FUNDING]
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    async def fetch_deposits(self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Transaction]:
        """
        fetch all deposits made to an account
        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch deposits for
        :param int [limit]: the maximum number of deposits structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.portfolios]: Identifies the portfolios by UUID(e.g., 892e8c7c-e979-4cad-b61b-55a197932cf1) or portfolio ID(e.g., 5189861793641175). Can provide single or multiple portfolios to filter by or fetches transfers for all portfolios if none are provided.
        :param int [params.until]: Only find transfers updated before self time. Use timestamp format
        :param str [params.status]: The current status of transfer. Possible values: [PROCESSED, NEW, FAILED, STARTED]
        :param str [params.type]: The type of transfer Possible values: [DEPOSIT, WITHDRAW, REBATE, STIPEND, INTERNAL, FUNDING]
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def parse_transaction_status(self, status: Str): # -> str | None:
        ...
    
    def parse_transaction(self, transaction: dict, currency: Currency = ...) -> Transaction:
        ...
    
    def parse_trade(self, trade: dict, market: Market = ...) -> Trade:
        ...
    
    async def fetch_markets(self, params=...) -> List[Market]:
        """

        https://docs.cloud.coinbase.com/intx/reference/getinstruments

        retrieves data on all markets for coinbaseinternational
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...
    
    def parse_market(self, market: dict) -> Market:
        ...
    
    async def fetch_currencies(self, params=...) -> Currencies:
        """
        fetches all available currencies on an exchange

        https://docs.cloud.coinbase.com/intx/reference/getassets

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an associative dictionary of currencies
        """
        ...
    
    def parse_currency(self, currency: dict) -> Currency:
        ...
    
    async def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://docs.cloud.coinbase.com/intx/reference/getinstruments

        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    async def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://docs.cloud.coinbase.com/intx/reference/getinstrumentquote

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...
    
    def parse_ticker(self, ticker: object, market: Market = ...) -> Ticker:
        ...
    
    async def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://docs.cloud.coinbase.com/intx/reference/getportfoliobalances

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.v3]: default False, set True to use v3 api endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...
    
    def parse_balance(self, response) -> Balances:
        ...
    
    async def transfer(self, code: str, amount: float, fromAccount: str, toAccount: str, params=...) -> TransferEntry:
        """
        Transfer an amount of asset from one portfolio to another.

        https://docs.cloud.coinbase.com/intx/reference/createportfolioassettransfer

        :param str code: unified currency code
        :param float amount: amount to transfer
        :param str fromAccount: account to transfer from
        :param str toAccount: account to transfer to
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transfer structure <https://github.com/ccxt/ccxt/wiki/Manual#transfer-structure>`
        """
        ...
    
    async def create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: float = ..., params=...): # -> Order:
        """
        create a trade order

        https://docs.cloud.coinbase.com/intx/reference/createorder

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much you want to trade in units of the base currency, quote currency for 'market' 'buy' orders
        :param float [price]: the price to fulfill the order, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param float [params.stopPrice]: alias for triggerPrice
        :param float [params.triggerPrice]: price to trigger stop orders
        :param float [params.stopLossPrice]: price to trigger stop-loss orders
        :param bool [params.postOnly]: True or False
        :param str [params.tif]: 'GTC', 'IOC', 'GTD' default is 'GTC' for limit orders and 'IOC' for market orders
        :param str [params.expire_time]: The expiration time required for orders with the time in force set to GTT. Must not go beyond 30 days of the current time. Uses ISO-8601 format(e.g., 2023-03-16T23:59:53Z)
        :param str [params.stp_mode]: Possible values: [NONE, AGGRESSING, BOTH] Specifies the behavior for self match handling. None disables the functionality, new cancels the newest order, and both cancels both orders.
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    def parse_order(self, order: dict, market: Market = ...) -> Order:
        ...
    
    def parse_order_status(self, status: Str): # -> str | None:
        ...
    
    def parse_order_type(self, type: Str): # -> str | None:
        ...
    
    async def cancel_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """
        cancels an open order

        https://docs.cloud.coinbase.com/intx/reference/cancelorder

        :param str id: order id
        :param str symbol: not used by coinbaseinternational cancelOrder()
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def cancel_all_orders(self, symbol: str = ..., params=...): # -> list[Any] | list[object]:
        """
        cancel all open orders
        :param str symbol: unified market symbol, only orders in the market of self symbol are cancelled when symbol is not None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def edit_order(self, id: str, symbol: str, type: OrderType, side: OrderSide, amount: float = ..., price: float = ..., params=...): # -> Order:
        """
        edit a trade order

        https://docs.cloud.coinbase.com/intx/reference/modifyorder

        :param str id: cancel order id
        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str params['clientOrderId']: client order id
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_order(self, id: str, symbol: Str = ..., params=...): # -> Order:
        """
        fetches information on an order made by the user

        https://docs.cloud.coinbase.com/intx/reference/modifyorder

        :param str id: the order id
        :param str symbol: unified market symbol that the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_open_orders(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...) -> List[Order]:
        """
        fetches information on all currently open orders

        https://docs.cloud.coinbase.com/intx/reference/getorders

        :param str symbol: unified market symbol of the orders
        :param int [since]: timestamp in ms of the earliest order, default is None
        :param int [limit]: the maximum number of open order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :param int [params.offset]: offset
        :param str [params.event_type]: The most recent type of event that happened to the order. Allowed values: NEW, TRADE, REPLACED
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...
    
    async def fetch_my_trades(self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...): # -> list[Any] | list[object]:
        """
        fetch all trades made by the user

        https://docs.cloud.coinbase.com/intx/reference/getmultiportfoliofills

        :param str symbol: unified market symbol of the trades
        :param int [since]: timestamp in ms of the earliest order, default is None
        :param int [limit]: the maximum number of trade structures to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: the latest time in ms to fetch trades for
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...
    
    async def withdraw(self, code: str, amount: float, address: str, tag=..., params=...) -> Transaction:
        """
        make a withdrawal

        https://docs.cloud.coinbase.com/intx/reference/withdraw
        https://docs.cloud.coinbase.com/intx/reference/counterpartywithdraw

        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str [tag]: an optional tag for the withdrawal
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.add_network_fee_to_total]: if True, deducts network fee from the portfolio, otherwise deduct fee from the withdrawal
        :param str [params.network_arn_id]: Identifies the blockchain network(e.g., networks/ethereum-mainnet/assets/313ef8a9-ae5a-5f2f-8a56-572c0e2a4d5a)
        :param str [params.nonce]: a unique integer representing the withdrawal request
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...
    
    def safe_network(self, network): # -> dict[str, Any]:
        ...
    
    def sign(self, path, api=..., method=..., params=..., headers=..., body=...): # -> dict[str, Any]:
        ...
    
    def handle_errors(self, code: int, reason: str, url: str, method: str, headers: dict, body: str, response, requestHeaders, requestBody): # -> None:
        ...
    


