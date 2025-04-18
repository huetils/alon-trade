"""
This type stub file was generated by pyright.
"""

from typing import List

from ccxt.abstract.blofin import ImplicitAPI
from ccxt.base.exchange import Exchange
from ccxt.base.types import (
    Balances,
    Currency,
    FundingRate,
    Int,
    LedgerEntry,
    Leverage,
    Leverages,
    MarginMode,
    Market,
    Num,
    Order,
    OrderBook,
    OrderRequest,
    OrderSide,
    OrderType,
    Position,
    Str,
    Strings,
    Ticker,
    Tickers,
    Trade,
    TradingFeeInterface,
    Transaction,
    TransferEntry,
)

class blofin(Exchange, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for blofin

        https://blofin.com/docs#get-instruments

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...

    def parse_market(self, market: dict) -> Market: ...
    def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://blofin.com/docs#get-order-book

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker: ...
    def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://blofin.com/docs#get-tickers

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def fetch_mark_price(self, symbol: str, params=...) -> Ticker:
        """
        fetches mark price for the market

        https://docs.blofin.com/index.html#get-mark-price

        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.subType]: "linear" or "inverse"
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://blofin.com/docs#get-tickers

        :param str[] [symbols]: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def parse_trade(self, trade: dict, market: Market = ...) -> Trade: ...
    def fetch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://blofin.com/docs#get-trades

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.paginate]: *only applies to publicGetMarketHistoryTrades* default False, when True will automatically paginate by calling self endpoint multiple times
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    def parse_ohlcv(self, ohlcv, market: Market = ...) -> list: ...
    def fetch_ohlcv(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[list]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://blofin.com/docs#get-candlesticks

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: timestamp in ms of the latest candle to fetch
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...

    def fetch_funding_rate_history(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        fetches historical funding rate prices

        https://blofin.com/docs#get-funding-rate-history

        :param str symbol: unified symbol of the market to fetch the funding rate history for
        :param int [since]: timestamp in ms of the earliest funding rate to fetch
        :param int [limit]: the maximum amount of `funding rate structures <https://docs.ccxt.com/#/?id=funding-rate-history-structure>` to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns dict[]: a list of `funding rate structures <https://docs.ccxt.com/#/?id=funding-rate-history-structure>`
        """
        ...

    def parse_funding_rate(self, contract, market: Market = ...) -> FundingRate: ...
    def fetch_funding_rate(self, symbol: str, params=...) -> FundingRate:
        """
        fetch the current funding rate

        https://blofin.com/docs#get-funding-rate

        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `funding rate structure <https://docs.ccxt.com/#/?id=funding-rate-structure>`
        """
        ...

    def parse_balance_by_type(self, response):  # -> dict[Any, Any]:
        ...
    def parse_balance(self, response):  # -> dict[Any, Any]:
        ...
    def parse_funding_balance(self, response):  # -> dict[Any, Any]:
        ...
    def parse_trading_fee(
        self, fee: dict, market: Market = ...
    ) -> TradingFeeInterface: ...
    def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://blofin.com/docs#get-balance
        https://blofin.com/docs#get-futures-account-balance

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.accountType]: the type of account to fetch the balance for, either 'funding' or 'futures'  or 'copy_trading' or 'earn'
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    def create_order_request(
        self,
        symbol: str,
        type: OrderType,
        side: OrderSide,
        amount: float,
        price: Num = ...,
        params=...,
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
    def parse_order_status(self, status: Str):  # -> str | None:
        ...
    def parse_order(self, order: dict, market: Market = ...) -> Order: ...
    def create_order(
        self,
        symbol: str,
        type: OrderType,
        side: OrderSide,
        amount: float,
        price: Num = ...,
        params=...,
    ) -> Order:
        """
        create a trade order

        https://blofin.com/docs#place-order
        https://blofin.com/docs#place-tpsl-order

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit' or 'post_only' or 'ioc' or 'fok'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param bool [params.reduceOnly]: a mark to reduce the position size for margin, swap and future orders
        :param bool [params.postOnly]: True to place a post only order
        :param str [params.marginMode]: 'cross' or 'isolated', default is 'cross'
        :param float [params.stopLossPrice]: stop loss trigger price(will use privatePostTradeOrderTpsl)
        :param float [params.takeProfitPrice]: take profit trigger price(will use privatePostTradeOrderTpsl)
        :param str [params.positionSide]: *stopLossPrice/takeProfitPrice orders only* 'long' or 'short' or 'net' default is 'net'
        :param str [params.clientOrderId]: a unique id for the order
        :param dict [params.takeProfit]: *takeProfit object in params* containing the triggerPrice at which the attached take profit order will be triggered
        :param float [params.takeProfit.triggerPrice]: take profit trigger price
        :param float [params.takeProfit.price]: take profit order price(if not provided the order will be a market order)
        :param dict [params.stopLoss]: *stopLoss object in params* containing the triggerPrice at which the attached stop loss order will be triggered
        :param float [params.stopLoss.triggerPrice]: stop loss trigger price
        :param float [params.stopLoss.price]: stop loss order price(if not provided the order will be a market order)
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def create_tpsl_order_request(
        self,
        symbol: str,
        type: OrderType,
        side: OrderSide,
        amount: Num = ...,
        price: Num = ...,
        params=...,
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
    def cancel_order(
        self, id: str, symbol: Str = ..., params=...
    ):  # -> dict[Any, Any] | Order:
        """
        cancels an open order

        https://blofin.com/docs#cancel-order
        https://blofin.com/docs#cancel-tpsl-order

        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.trigger]: True if cancelling a trigger/conditional order/tp sl orders
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def create_orders(self, orders: List[OrderRequest], params=...) -> List[Order]:
        """
        create a list of trade orders

        https://blofin.com/docs#place-multiple-orders

        :param Array orders: list of orders to create, each object should contain the parameters required by createOrder, namely symbol, type, side, amount, price and params
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_open_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        Fetch orders that are still open

        https://blofin.com/docs#get-active-orders
        https://blofin.com/docs#get-active-tpsl-orders

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param bool [params.trigger]: True if fetching trigger or conditional orders
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        fetch all trades made by the user

        https://blofin.com/docs#get-trade-history

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: Timestamp in ms of the latest time to retrieve trades for
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    def fetch_deposits(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
        fetch all deposits made to an account

        https://blofin.com/docs#get-deposite-history

        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch deposits for
        :param int [limit]: the maximum number of deposits structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: the latest time in ms to fetch entries for
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def fetch_withdrawals(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
        fetch all withdrawals made from an account

        https://blofin.com/docs#get-withdraw-history

        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch withdrawals for
        :param int [limit]: the maximum number of withdrawals structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: the latest time in ms to fetch entries for
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def fetch_ledger(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[LedgerEntry]:
        """
        fetch the history of changes, actions done by the user or operations that altered the balance of the user

        https://blofin.com/docs#get-funds-transfer-history

        :param str [code]: unified currency code, default is None
        :param int [since]: timestamp in ms of the earliest ledger entry, default is None
        :param int [limit]: max number of ledger entries to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.marginMode]: 'cross' or 'isolated'
        :param int [params.until]: the latest time in ms to fetch entries for
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [available parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns dict: a `ledger structure <https://docs.ccxt.com/#/?id=ledger>`
        """
        ...

    def parse_transaction(
        self, transaction: dict, currency: Currency = ...
    ) -> Transaction: ...
    def parse_transaction_status(self, status: Str):  # -> str | None:
        ...
    def parse_ledger_entry_type(self, type):  # -> str | None:
        ...
    def parse_ledger_entry(
        self, item: dict, currency: Currency = ...
    ) -> LedgerEntry: ...
    def parse_ids(self, ids):  # -> list[str]:
        """
        @ignore
               :param string[]|str ids: order ids
               :returns str[]: list of order ids
        """
        ...

    def cancel_orders(
        self, ids, symbol: Str = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        cancel multiple orders

        https://blofin.com/docs#cancel-multiple-orders

        :param str[] ids: order ids
        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.trigger]: whether the order is a stop/trigger order
        :returns dict: an list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def transfer(
        self, code: str, amount: float, fromAccount: str, toAccount: str, params=...
    ) -> TransferEntry:
        """
        transfer currency internally between wallets on the same account

        https://blofin.com/docs#funds-transfer

        :param str code: unified currency code
        :param float amount: amount to transfer
        :param str fromAccount: account to transfer from(funding, swap, copy_trading, earn)
        :param str toAccount: account to transfer to(funding, swap, copy_trading, earn)
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `transfer structure <https://docs.ccxt.com/#/?id=transfer-structure>`
        """
        ...

    def parse_transfer(
        self, transfer: dict, currency: Currency = ...
    ) -> TransferEntry: ...
    def fetch_position(self, symbol: str, params=...) -> Position:
        """
        fetch data on a single open contract trade position

        https://blofin.com/docs#get-positions

        :param str symbol: unified market symbol of the market the position is held in, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.instType]: MARGIN, SWAP, FUTURES, OPTION
        :returns dict: a `position structure <https://docs.ccxt.com/#/?id=position-structure>`
        """
        ...

    def fetch_positions(self, symbols: Strings = ..., params=...) -> List[Position]:
        """
        fetch data on a single open contract trade position

        https://blofin.com/docs#get-positions

        :param str[] [symbols]: list of unified market symbols
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.instType]: MARGIN, SWAP, FUTURES, OPTION
        :returns dict: a `position structure <https://docs.ccxt.com/#/?id=position-structure>`
        """
        ...

    def parse_position(
        self, position: dict, market: Market = ...
    ):  # -> dict[Any, Any]:
        ...
    def fetch_leverages(self, symbols: Strings = ..., params=...) -> Leverages:
        """
        fetch the set leverage for all contract markets

        https://docs.blofin.com/index.html#get-multiple-leverage

        :param str[] symbols: a list of unified market symbols, required on blofin
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.marginMode]: 'cross' or 'isolated'
        :returns dict: a list of `leverage structures <https://docs.ccxt.com/#/?id=leverage-structure>`
        """
        ...

    def fetch_leverage(self, symbol: str, params=...) -> Leverage:
        """
        fetch the set leverage for a market

        https://docs.blofin.com/index.html#get-leverage

        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.marginMode]: 'cross' or 'isolated'
        :returns dict: a `leverage structure <https://docs.ccxt.com/#/?id=leverage-structure>`
        """
        ...

    def parse_leverage(self, leverage: dict, market: Market = ...) -> Leverage: ...
    def set_leverage(self, leverage: Int, symbol: Str = ..., params=...):  # -> Any:
        """
        set the level of leverage for a market

        https://blofin.com/docs#set-leverage

        :param int leverage: the rate of leverage
        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.marginMode]: 'cross' or 'isolated'
        :returns dict: response from the exchange
        """
        ...

    def close_position(self, symbol: str, side: OrderSide = ..., params=...) -> Order:
        """
               closes open positions for a market

               https://blofin.com/docs#close-positions

               :param str symbol: Unified CCXT market symbol
               :param str [side]: 'buy' or 'sell', leave in net mode
               :param dict [params]: extra parameters specific to the blofin api endpoint
               :param str [params.clientOrderId]: a unique identifier for the order
               :param str [params.marginMode]: 'cross' or 'isolated', default is 'cross
               :param str [params.code]: *required in the case of closing cross MARGIN position for Single-currency margin* margin currency

        EXCHANGE SPECIFIC PARAMETERS
               :param boolean [params.autoCxl]: whether any pending orders for closing out needs to be automatically canceled when close position via a market order. False or True, the default is False
               :param str [params.tag]: order tag a combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters
               :returns dict[]: `A list of position structures <https://docs.ccxt.com/#/?id=position-structure>`
        """
        ...

    def fetch_closed_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetches information on multiple closed orders made by the user

        https://blofin.com/docs#get-order-history
        https://blofin.com/docs#get-tpsl-order-history

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of  orde structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param bool [params.trigger]: True if fetching trigger or conditional orders
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_margin_mode(self, symbol: str, params=...) -> MarginMode:
        """
        fetches the margin mode of a trading pair

        https://docs.blofin.com/index.html#get-margin-mode

        :param str symbol: unified symbol of the market to fetch the margin mode for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `margin mode structure <https://docs.ccxt.com/#/?id=margin-mode-structure>`
        """
        ...

    def parse_margin_mode(self, marginMode: dict, market=...) -> MarginMode: ...
    def handle_errors(
        self,
        httpCode: int,
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
    def sign(
        self, path, api=..., method=..., params=..., headers=..., body=...
    ):  # -> dict[str, Any]:
        ...
