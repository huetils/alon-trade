"""
This type stub file was generated by pyright.
"""

from typing import List

from ccxt.abstract.whitebit import ImplicitAPI
from ccxt.base.exchange import Exchange
from ccxt.base.types import (
    Balances,
    BorrowInterest,
    Currencies,
    Currency,
    DepositAddress,
    FundingRate,
    FundingRates,
    Int,
    Market,
    Num,
    Order,
    OrderBook,
    OrderSide,
    OrderType,
    Str,
    Strings,
    Ticker,
    Tickers,
    Trade,
    TradingFees,
    Transaction,
    TransferEntry,
)

class whitebit(Exchange, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for whitebit

        https://docs.whitebit.com/public/http-v4/#market-info

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...

    def parse_market(self, market: dict) -> Market: ...
    def fetch_currencies(self, params=...) -> Currencies:
        """
        fetches all available currencies on an exchange

        https://docs.whitebit.com/public/http-v4/#asset-status-list

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an associative dictionary of currencies
        """
        ...

    def fetch_transaction_fees(
        self, codes: Strings = ..., params=...
    ):  # -> dict[str, Any]:
        """
        @deprecated
               please use fetchDepositWithdrawFees instead

               https://docs.whitebit.com/public/http-v4/#fee

               :param str[]|None codes: not used by fetchTransactionFees()
               :param dict [params]: extra parameters specific to the exchange API endpoint
               :returns dict: a list of `fee structures <https://docs.ccxt.com/#/?id=fee-structure>`
        """
        ...

    def fetch_deposit_withdraw_fees(
        self, codes: Strings = ..., params=...
    ):  # -> dict[Any, Any]:
        """
        fetch deposit and withdraw fees

        https://docs.whitebit.com/public/http-v4/#fee

        :param str[]|None codes: not used by fetchDepositWithdrawFees()
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a list of `fee structures <https://docs.ccxt.com/#/?id=fee-structure>`
        """
        ...

    def parse_deposit_withdraw_fees(
        self, response, codes=..., currencyIdKey=...
    ):  # -> dict[Any, Any]:
        ...
    def fetch_trading_fees(self, params=...) -> TradingFees:
        """
        fetch the trading fees for multiple markets

        https://docs.whitebit.com/public/http-v4/#asset-status-list

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `fee structures <https://docs.ccxt.com/#/?id=fee-structure>` indexed by market symbols
        """
        ...

    def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://docs.whitebit.com/public/http-v4/#market-activity

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker: ...
    def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://docs.whitebit.com/public/http-v4/#market-activity

        :param str[] [symbols]: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.method]: either v2PublicGetTicker or v4PublicGetTicker default is v4PublicGetTicker
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://docs.whitebit.com/public/http-v4/#orderbook

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def fetch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://docs.whitebit.com/public/http-v4/#recent-trades

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    def fetch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        fetch all trades made by the user

        https://docs.whitebit.com/private/http-trade-v4/#query-executed-order-history

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    def parse_trade(self, trade: dict, market: Market = ...) -> Trade: ...
    def fetch_ohlcv(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[list]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://docs.whitebit.com/public/http-v1/#kline

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...

    def parse_ohlcv(self, ohlcv, market: Market = ...) -> list: ...
    def fetch_status(self, params=...):  # -> dict[str, Any]:
        """
        the latest known information on the availability of the exchange API

        https://docs.whitebit.com/public/http-v4/#server-status

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `status structure <https://docs.ccxt.com/#/?id=exchange-status-structure>`
        """
        ...

    def fetch_time(self, params=...):  # -> int | None:
        """
        fetches the current integer timestamp in milliseconds from the exchange server

        https://docs.whitebit.com/public/http-v4/#server-time

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int: the current integer timestamp in milliseconds from the exchange server
        """
        ...

    def create_market_order_with_cost(
        self, symbol: str, side: OrderSide, cost: float, params=...
    ):  # -> Order:
        """
        create a market order by providing the symbol, side and cost
        :param str symbol: unified symbol of the market to create an order in
        :param str side: 'buy' or 'sell'
        :param float cost: how much you want to trade in units of the quote currency
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def create_market_buy_order_with_cost(
        self, symbol: str, cost: float, params=...
    ) -> Order:
        """
        create a market buy order by providing the symbol and cost
        :param str symbol: unified symbol of the market to create an order in
        :param float cost: how much you want to trade in units of the quote currency
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def create_order(
        self,
        symbol: str,
        type: OrderType,
        side: OrderSide,
        amount: float,
        price: Num = ...,
        params=...,
    ):  # -> Order:
        """
        create a trade order

        https://docs.whitebit.com/private/http-trade-v4/#create-limit-order
        https://docs.whitebit.com/private/http-trade-v4/#create-market-order
        https://docs.whitebit.com/private/http-trade-v4/#create-buy-stock-market-order
        https://docs.whitebit.com/private/http-trade-v4/#create-stop-limit-order
        https://docs.whitebit.com/private/http-trade-v4/#create-stop-market-order

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param float [params.cost]: *market orders only* the cost of the order in units of the base currency
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def edit_order(
        self,
        id: str,
        symbol: str,
        type: OrderType,
        side: OrderSide,
        amount: Num = ...,
        price: Num = ...,
        params=...,
    ):  # -> Order:
        """
        edit a trade order

        https://docs.whitebit.com/private/http-trade-v4/#modify-order

        :param str id: cancel order id
        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float price: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def cancel_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """
        cancels an open order

        https://docs.whitebit.com/private/http-trade-v4/#cancel-order

        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def cancel_all_orders(
        self, symbol: Str = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        cancel all open orders

        https://docs.whitebit.com/private/http-trade-v4/#cancel-all-orders

        :param str symbol: unified market symbol, only orders in the market of self symbol are cancelled when symbol is not None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.type]: market type, ['swap', 'spot']
        :param boolean [params.isMargin]: cancel all margin orders
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def cancel_all_orders_after(self, timeout: Int, params=...):  # -> Any:
        """
        dead man's switch, cancel all orders after the given timeout

        https://docs.whitebit.com/private/http-trade-v4/#sync-kill-switch-timer

        :param number timeout: time in milliseconds, 0 represents cancel the timer
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.types]: Order types value. Example: "spot", "margin", "futures" or None
        :param str [params.symbol]: symbol unified symbol of the market the order was made in
        :returns dict: the api result
        """
        ...

    def parse_balance(self, response) -> Balances: ...
    def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://docs.whitebit.com/private/http-main-v4/#main-balance
        https://docs.whitebit.com/private/http-trade-v4/#trading-balance

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    def fetch_open_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://docs.whitebit.com/private/http-trade-v4/#query-unexecutedactive-orders

        :param str [symbol]: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of open order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_closed_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetches information on multiple closed orders made by the user

        https://docs.whitebit.com/private/http-trade-v4/#query-executed-orders

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def parse_order_type(self, type: Str):  # -> str | None:
        ...
    def parse_order(self, order: dict, market: Market = ...) -> Order: ...
    def fetch_order_trades(
        self, id: str, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        fetch all the trades made from a single order

        https://docs.whitebit.com/private/http-trade-v4/#query-executed-order-deals

        :param str id: order id
        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    def fetch_deposit_address(self, code: str, params=...) -> DepositAddress:
        """
        fetch the deposit address for a currency associated with self account

        https://docs.whitebit.com/private/http-main-v4/#get-fiat-deposit-address
        https://docs.whitebit.com/private/http-main-v4/#get-cryptocurrency-deposit-address

        :param str code: unified currency code
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...

    def set_leverage(self, leverage: Int, symbol: Str = ..., params=...):  # -> Any:
        """
        set the level of leverage for a market

        https://docs.whitebit.com/private/http-trade-v4/#change-collateral-account-leverage

        :param float leverage: the rate of leverage
        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: response from the exchange
        """
        ...

    def transfer(
        self, code: str, amount: float, fromAccount: str, toAccount: str, params=...
    ) -> TransferEntry:
        """
        transfer currency internally between wallets on the same account

        https://docs.whitebit.com/private/http-main-v4/#transfer-between-main-and-trade-balances

        :param str code: unified currency code
        :param float amount: amount to transfer
        :param str fromAccount: account to transfer from - main, spot, collateral
        :param str toAccount: account to transfer to - main, spot, collateral
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transfer structure <https://docs.ccxt.com/#/?id=transfer-structure>`
        """
        ...

    def parse_transfer(
        self, transfer: dict, currency: Currency = ...
    ) -> TransferEntry: ...
    def withdraw(
        self, code: str, amount: float, address: str, tag=..., params=...
    ) -> Transaction:
        """
        make a withdrawal

        https://docs.whitebit.com/private/http-main-v4/#create-withdraw-request

        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str tag:
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def parse_transaction(
        self, transaction: dict, currency: Currency = ...
    ) -> Transaction: ...
    def parse_transaction_status(self, status: Str):  # -> str | None:
        ...
    def fetch_deposit(self, id: str, code: Str = ..., params=...):  # -> Transaction:
        """
        fetch information on a deposit

        https://docs.whitebit.com/private/http-main-v4/#get-depositwithdraw-history

        :param str id: deposit id
        :param str code: not used by whitebit fetchDeposit()
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def fetch_deposits(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
        fetch all deposits made to an account

        https://docs.whitebit.com/private/http-main-v4/#get-depositwithdraw-history

        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch deposits for
        :param int [limit]: the maximum number of deposits structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def fetch_borrow_interest(
        self,
        code: Str = ...,
        symbol: Str = ...,
        since: Int = ...,
        limit: Int = ...,
        params=...,
    ) -> List[BorrowInterest]:
        """
        fetch the interest owed by the user for borrowing currency for margin trading

        https://docs.whitebit.com/private/http-trade-v4/#open-positions

        :param str code: unified currency code
        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch borrrow interest for
        :param int [limit]: the maximum number of structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `borrow interest structures <https://docs.ccxt.com/#/?id=borrow-interest-structure>`
        """
        ...

    def parse_borrow_interest(
        self, info: dict, market: Market = ...
    ) -> BorrowInterest: ...
    def fetch_funding_rate(self, symbol: str, params=...) -> FundingRate:
        """
        fetch the current funding rate

        https://docs.whitebit.com/public/http-v4/#available-futures-markets-list

        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `funding rate structure <https://docs.ccxt.com/#/?id=funding-rate-structure>`
        """
        ...

    def fetch_funding_rates(self, symbols: Strings = ..., params=...) -> FundingRates:
        """
        fetch the funding rate for multiple markets

        https://docs.whitebit.com/public/http-v4/#available-futures-markets-list

        :param str[]|None symbols: list of unified market symbols
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `funding rate structures <https://docs.ccxt.com/#/?id=funding-rates-structure>`, indexed by market symbols
        """
        ...

    def parse_funding_rate(self, contract, market: Market = ...) -> FundingRate: ...
    def fetch_deposits_withdrawals(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
               fetch history of deposits and withdrawals

               https://github.com/whitebit-exchange/api-docs/blob/main/pages/private/http-main-v4.md#get-depositwithdraw-history

               :param str [code]: unified currency code for the currency of the deposit/withdrawals, default is None
               :param int [since]: timestamp in ms of the earliest deposit/withdrawal, default is None
               :param int [limit]: max number of deposit/withdrawals to return, default = 50, Min: 1, Max: 100
               :param dict [params]: extra parameters specific to the exchange API endpoint

        EXCHANGE SPECIFIC PARAMETERS
               :param number [params.transactionMethod]: Method. Example: 1 to display deposits / 2 to display withdraws. Do not send self parameter in order to receive both deposits and withdraws.
               :param str [params.address]: Can be used for filtering transactions by specific address or memo.
               :param str[] [params.addresses]: Can be used for filtering transactions by specific addresses or memos(max: 20).
               :param str [params.uniqueId]: Can be used for filtering transactions by specific unique id
               :param int [params.offset]: If you want the request to return entries starting from a particular line, you can use OFFSET clause to tell it where it should start. Default: 0, Min: 0, Max: 10000
               :param str[] [params.status]: Can be used for filtering transactions by status codes. Caution: You must use self parameter with appropriate transactionMethod and use valid status codes for self method. You can find them below. Example: "status": [3,7]
               :returns dict: a list of `transaction structure <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def is_fiat(self, currency: str) -> bool: ...
    def nonce(self):  # -> int:
        ...
    def sign(
        self, path, api=..., method=..., params=..., headers=..., body=...
    ):  # -> dict[str, Any]:
        ...
    def handle_errors(
        self,
        code: int,
        reason: str,
        url: str,
        method: str,
        headers: dict,
        body: str,
        response,
        requestHeaders,
        requestBody,
    ):  # -> None:
        ...
