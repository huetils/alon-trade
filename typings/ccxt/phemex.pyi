"""
This type stub file was generated by pyright.
"""

from typing import List

from ccxt.abstract.phemex import ImplicitAPI
from ccxt.base.exchange import Exchange
from ccxt.base.types import (
    Balances,
    Currencies,
    Currency,
    DepositAddress,
    FundingRate,
    Int,
    LeverageTier,
    LeverageTiers,
    MarginModification,
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
    Transaction,
    TransferEntry,
)

class phemex(Exchange, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    def parse_safe_number(self, value=...):  # -> None:
        ...
    def parse_swap_market(
        self, market: dict
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
    def parse_spot_market(
        self, market: dict
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
    def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for phemex

        https://phemex-docs.github.io/#query-product-information-3

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...

    def fetch_currencies(self, params=...) -> Currencies:
        """
        fetches all available currencies on an exchange
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an associative dictionary of currencies
        """
        ...

    def custom_parse_bid_ask(
        self, bidask, priceKey=..., amountKey=..., market: Market = ...
    ):  # -> list[Any | None]:
        ...
    def custom_parse_order_book(
        self,
        orderbook,
        symbol,
        timestamp=...,
        bidsKey=...,
        asksKey=...,
        priceKey=...,
        amountKey=...,
        market: Market = ...,
    ):  # -> dict[Any, Any]:
        ...
    def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://github.com/phemex/phemex-api-docs/blob/master/Public-Hedged-Perpetual-API.md#queryorderbook

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def to_en(self, n, scale):  # -> int:
        ...
    def to_ev(self, amount, market: Market = ...):  # -> int:
        ...
    def to_ep(self, price, market: Market = ...):  # -> int:
        ...
    def from_en(self, en, scale):  # -> str | None:
        ...
    def from_ep(self, ep, market: Market = ...):  # -> str | None:
        ...
    def from_ev(self, ev, market: Market = ...):  # -> str | None:
        ...
    def from_er(self, er, market: Market = ...):  # -> str | None:
        ...
    def parse_ohlcv(self, ohlcv, market: Market = ...) -> list: ...
    def fetch_ohlcv(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[list]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://github.com/phemex/phemex-api-docs/blob/master/Public-Hedged-Perpetual-API.md#querykline
        https://github.com/phemex/phemex-api-docs/blob/master/Public-Contract-API-en.md#query-kline

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: *only used for USDT settled contracts, otherwise is emulated and not supported by the exchange* timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.until]: *USDT settled/ linear swaps only* end time in ms
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...

    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker: ...
    def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://github.com/phemex/phemex-api-docs/blob/master/Public-Hedged-Perpetual-API.md#query24hrsticker

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://phemex-docs.github.io/#query-24-hours-ticker-for-all-symbols-2     # spot
        https://phemex-docs.github.io/#query-24-ticker-for-all-symbols             # linear
        https://phemex-docs.github.io/#query-24-hours-ticker-for-all-symbols       # inverse

        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def fetch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://github.com/phemex/phemex-api-docs/blob/master/Public-Hedged-Perpetual-API.md#querytrades

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    def parse_trade(self, trade: dict, market: Market = ...) -> Trade: ...
    def parse_spot_balance(self, response):  # -> dict[Any, Any]:
        ...
    def parse_swap_balance(self, response):  # -> dict[Any, Any]:
        ...
    def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://phemex-docs.github.io/#query-wallets
        https://github.com/phemex/phemex-api-docs/blob/master/Public-Hedged-Perpetual-API.md#query-account-positions
        https://phemex-docs.github.io/#query-trading-account-and-positions

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.type]: spot or swap
        :param str [params.code]: *swap only* currency code of the balance to query(USD, USDT, etc), default is USDT
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    def parse_order_status(self, status: Str):  # -> str | None:
        ...
    def parse_order_type(self, type: Str):  # -> str | None:
        ...
    def parse_time_in_force(self, timeInForce: Str):  # -> str | None:
        ...
    def parse_spot_order(
        self, order: dict, market: Market = ...
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
    def parse_order_side(self, side):  # -> str | None:
        ...
    def parse_swap_order(
        self, order, market: Market = ...
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
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
    ):  # -> Order:
        """
        create a trade order

        https://github.com/phemex/phemex-api-docs/blob/master/Public-Hedged-Perpetual-API.md#place-order
        https://phemex-docs.github.io/#place-order-http-put-prefered-3

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param float [params.trigger]: trigger price for conditional orders
        :param dict [params.takeProfit]: *swap only* *takeProfit object in params* containing the triggerPrice at which the attached take profit order will be triggered(perpetual swap markets only)
        :param float [params.takeProfit.triggerPrice]: take profit trigger price
        :param dict [params.stopLoss]: *swap only* *stopLoss object in params* containing the triggerPrice at which the attached stop loss order will be triggered(perpetual swap markets only)
        :param float [params.stopLoss.triggerPrice]: stop loss trigger price
        :param str [params.posSide]: *swap only* "Merged" for one way mode, "Long" for buy side of hedged mode, "Short" for sell side of hedged mode
        :param bool [params.hedged]: *swap only* True for hedged mode, False for one way mode, default is False
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def edit_order(
        self,
        id: str,
        symbol: str,
        type: OrderType = ...,
        side: OrderSide = ...,
        amount: Num = ...,
        price: Num = ...,
        params=...,
    ):  # -> Order:
        """
        edit a trade order

        https://github.com/phemex/phemex-api-docs/blob/master/Public-Hedged-Perpetual-API.md#amend-order-by-orderid

        :param str id: cancel order id
        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.posSide]: either 'Merged' or 'Long' or 'Short'
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def cancel_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """
        cancels an open order

        https://github.com/phemex/phemex-api-docs/blob/master/Public-Hedged-Perpetual-API.md#cancel-single-order-by-orderid

        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.posSide]: either 'Merged' or 'Long' or 'Short'
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def cancel_all_orders(
        self, symbol: Str = ..., params=...
    ):  # -> list[OrderedDict[Any, Any] | dict[Any, Any]]:
        """
        cancel all open orders in a market

        https://github.com/phemex/phemex-api-docs/blob/master/Public-Hedged-Perpetual-API.md#cancelall

        :param str symbol: unified market symbol of the market to cancel orders in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """

        https://phemex-docs.github.io/#query-orders-by-ids

        fetches information on an order made by the user
        :param str id: the order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetches information on multiple orders made by the user

        https://github.com/phemex/phemex-api-docs/blob/master/Public-Hedged-Perpetual-API.md#queryorder

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_open_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://github.com/phemex/phemex-api-docs/blob/master/Public-Hedged-Perpetual-API.md#queryopenorder
        https://github.com/phemex/phemex-api-docs/blob/master/Public-Contract-API-en.md
        https://github.com/phemex/phemex-api-docs/blob/master/Public-Spot-API-en.md#spotListAllOpenOrder

        :param str symbol: unified market symbol
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

        https://github.com/phemex/phemex-api-docs/blob/master/Public-Hedged-Perpetual-API.md#queryorder
        https://github.com/phemex/phemex-api-docs/blob/master/Public-Contract-API-en.md#queryorder
        https://github.com/phemex/phemex-api-docs/blob/master/Public-Hedgedd-Perpetual-API.md#query-closed-orders-by-symbol
        https://github.com/phemex/phemex-api-docs/blob/master/Public-Spot-API-en.md#spotDataOrdersByIds

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.settle]: the settlement currency to fetch orders for
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        fetch all trades made by the user

        https://github.com/phemex/phemex-api-docs/blob/master/Public-Contract-API-en.md#query-user-trade
        https://github.com/phemex/phemex-api-docs/blob/master/Public-Hedged-Perpetual-API.md#query-user-trade
        https://github.com/phemex/phemex-api-docs/blob/master/Public-Spot-API-en.md#spotDataTradesHist

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
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

    def fetch_deposits(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
        fetch all deposits made to an account
        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch deposits for
        :param int [limit]: the maximum number of deposits structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def fetch_withdrawals(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Transaction]:
        """
        fetch all withdrawals made from an account
        :param str code: unified currency code
        :param int [since]: the earliest time in ms to fetch withdrawals for
        :param int [limit]: the maximum number of withdrawals structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transaction structures <https://docs.ccxt.com/#/?id=transaction-structure>`
        """
        ...

    def parse_transaction_status(self, status: Str):  # -> str | None:
        ...
    def parse_transaction(
        self, transaction: dict, currency: Currency = ...
    ) -> Transaction: ...
    def fetch_positions(
        self, symbols: Strings = ..., params=...
    ):  # -> dict[Any, Any] | list[Any]:
        """
        fetch all open positions

        https://github.com/phemex/phemex-api-docs/blob/master/Public-Contract-API-en.md#query-trading-account-and-positions
        https://github.com/phemex/phemex-api-docs/blob/master/Public-Hedged-Perpetual-API.md#query-account-positions
        https://phemex-docs.github.io/#query-account-positions-with-unrealized-pnl

        :param str[] [symbols]: list of unified market symbols
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.code]: the currency code to fetch positions for, USD, BTC or USDT, USD is the default
        :param str [params.method]: *USDT contracts only* 'privateGetGAccountsAccountPositions' or 'privateGetAccountsPositions' default is 'privateGetGAccountsAccountPositions'
        :returns dict[]: a list of `position structure <https://docs.ccxt.com/#/?id=position-structure>`
        """
        ...

    def parse_position(
        self, position: dict, market: Market = ...
    ):  # -> dict[Any, Any]:
        ...
    def fetch_funding_history(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any]:
        """
        fetch the history of funding payments paid and received on self account

        https://github.com/phemex/phemex-api-docs/blob/master/Public-Hedged-Perpetual-API.md#futureDataFundingFeesHist

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch funding history for
        :param int [limit]: the maximum number of funding history structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `funding history structure <https://docs.ccxt.com/#/?id=funding-history-structure>`
        """
        ...

    def parse_funding_fee_to_precision(
        self, value, market: Market = ..., currencyCode: Str = ...
    ):  # -> str | None:
        ...
    def fetch_funding_rate(self, symbol: str, params=...) -> FundingRate:
        """
        fetch the current funding rate
        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `funding rate structure <https://docs.ccxt.com/#/?id=funding-rate-structure>`
        """
        ...

    def parse_funding_rate(self, contract, market: Market = ...) -> FundingRate: ...
    def set_margin(self, symbol: str, amount: float, params=...) -> MarginModification:
        """
        Either adds or reduces margin in an isolated position in order to set the margin to a specific value

        https://github.com/phemex/phemex-api-docs/blob/master/Public-Contract-API-en.md#assign-position-balance-in-isolated-marign-mode

        :param str symbol: unified market symbol of the market to set margin in
        :param float amount: the amount to set the margin to
        :param dict [params]: parameters specific to the exchange API endpoint
        :returns dict: A `margin structure <https://docs.ccxt.com/#/?id=add-margin-structure>`
        """
        ...

    def parse_margin_status(self, status):  # -> str | None:
        ...
    def parse_margin_modification(
        self, data: dict, market: Market = ...
    ) -> MarginModification: ...
    def set_margin_mode(
        self, marginMode: str, symbol: Str = ..., params=...
    ):  # -> Any:
        """
        set margin mode to 'cross' or 'isolated'

        https://phemex-docs.github.io/#set-leverage

        :param str marginMode: 'cross' or 'isolated'
        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: response from the exchange
        """
        ...

    def set_position_mode(self, hedged: bool, symbol: Str = ..., params=...):  # -> Any:
        """
        set hedged to True or False for a market

        https://github.com/phemex/phemex-api-docs/blob/master/Public-Hedged-Perpetual-API.md#switch-position-mode-synchronously

        :param bool hedged: set to True to use dualSidePosition
        :param str symbol: not used by binance setPositionMode()
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: response from the exchange
        """
        ...

    def fetch_leverage_tiers(self, symbols: Strings = ..., params=...) -> LeverageTiers:
        """
        retrieve information on the maximum leverage, and maintenance margin for trades of varying trade sizes
        :param str[]|None symbols: list of unified market symbols
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `leverage tiers structures <https://docs.ccxt.com/#/?id=leverage-tiers-structure>`, indexed by market symbols
        """
        ...

    def parse_market_leverage_tiers(
        self, info, market: Market = ...
    ) -> List[LeverageTier]:
        """
        :param dict info: Exchange market response for 1 market
        :param dict market: CCXT market
        """
        ...

    def sign(
        self, path, api=..., method=..., params=..., headers=..., body=...
    ):  # -> dict[str, Any]:
        ...
    def set_leverage(self, leverage: Int, symbol: Str = ..., params=...):  # -> Any:
        """
        set the level of leverage for a market

        https://github.com/phemex/phemex-api-docs/blob/master/Public-Hedged-Perpetual-API.md#set-leverage

        :param float leverage: the rate of leverage, 100 > leverage > -100 excluding numbers between -1 to 1
        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param bool [params.hedged]: set to True if hedged position mode is enabled(by default long and short leverage are set to the same value)
        :param float [params.longLeverageRr]: *hedged mode only* set the leverage for long positions
        :param float [params.shortLeverageRr]: *hedged mode only* set the leverage for short positions
        :returns dict: response from the exchange
        """
        ...

    def transfer(
        self, code: str, amount: float, fromAccount: str, toAccount: str, params=...
    ) -> TransferEntry:
        """
        transfer currency internally between wallets on the same account

        https://phemex-docs.github.io/#transfer-between-spot-and-futures
        https://phemex-docs.github.io/#universal-transfer-main-account-only-transfer-between-sub-to-main-main-to-sub-or-sub-to-sub

        :param str code: unified currency code
        :param float amount: amount to transfer
        :param str fromAccount: account to transfer from
        :param str toAccount: account to transfer to
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.bizType]: for transferring between main and sub-acounts either 'SPOT' or 'PERPETUAL' default is 'SPOT'
        :returns dict: a `transfer structure <https://docs.ccxt.com/#/?id=transfer-structure>`
        """
        ...

    def fetch_transfers(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[TransferEntry]:
        """
        fetch a history of internal transfers made on an account

        https://phemex-docs.github.io/#query-transfer-history

        :param str code: unified currency code of the currency transferred
        :param int [since]: the earliest time in ms to fetch transfers for
        :param int [limit]: the maximum number of  transfers structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `transfer structures <https://docs.ccxt.com/#/?id=transfer-structure>`
        """
        ...

    def parse_transfer(
        self, transfer: dict, currency: Currency = ...
    ) -> TransferEntry: ...
    def parse_transfer_status(self, status: Str) -> Str: ...
    def fetch_funding_rate_history(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        fetches historical funding rate prices

        https://phemex-docs.github.io/#query-funding-rate-history-2

        :param str symbol: unified symbol of the market to fetch the funding rate history for
        :param int [since]: timestamp in ms of the earliest funding rate to fetch
        :param int [limit]: the maximum amount of `funding rate structures <https://docs.ccxt.com/#/?id=funding-rate-history-structure>` to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param boolean [params.paginate]: default False, when True will automatically paginate by calling self endpoint multiple times. See in the docs all the [availble parameters](https://github.com/ccxt/ccxt/wiki/Manual#pagination-params)
        :param int [params.until]: timestamp in ms of the latest funding rate
        :returns dict[]: a list of `funding rate structures <https://docs.ccxt.com/#/?id=funding-rate-history-structure>`
        """
        ...

    def withdraw(
        self, code: str, amount: float, address: str, tag=..., params=...
    ) -> Transaction:
        """
        make a withdrawal

        https://phemex-docs.github.io/#create-withdraw-request

        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str tag:
        :param dict [params]: extra parameters specific to the phemex api endpoint
        :param str [params.network]: unified network code
        :returns dict: a `transaction structure <https://github.com/ccxt/ccxt/wiki/Manual#transaction-structure>`
        """
        ...

    def fetch_open_interest(
        self, symbol: str, params=...
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        """
        retrieves the open interest of a trading pair

        https://phemex-docs.github.io/#query-24-hours-ticker

        :param str symbol: unified CCXT market symbol
        :param dict [params]: exchange specific parameters
        :returns dict} an open interest structure{@link https://docs.ccxt.com/#/?id=open-interest-structure:
        """
        ...

    def parse_open_interest(
        self, interest, market: Market = ...
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
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
