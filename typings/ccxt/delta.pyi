"""
This type stub file was generated by pyright.
"""

from typing import List

from ccxt.abstract.delta import ImplicitAPI
from ccxt.base.exchange import Exchange
from ccxt.base.types import (
    Balances,
    Currencies,
    Currency,
    DepositAddress,
    FundingRate,
    FundingRates,
    Greeks,
    Int,
    LedgerEntry,
    Leverage,
    MarginMode,
    MarginModification,
    Market,
    MarketInterface,
    Num,
    Option,
    Order,
    OrderBook,
    OrderSide,
    OrderType,
    Position,
    Str,
    Strings,
    Ticker,
    Tickers,
    Trade,
)

class delta(Exchange, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    def create_expired_option_market(self, symbol: str):  # -> dict[str, Any]:
        ...
    def safe_market(
        self,
        marketId: Str = ...,
        market: Market = ...,
        delimiter: Str = ...,
        marketType: Str = ...,
    ) -> MarketInterface: ...
    def fetch_time(self, params=...):  # -> int | None:
        """
        fetches the current integer timestamp in milliseconds from the exchange server
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int: the current integer timestamp in milliseconds from the exchange server
        """
        ...

    def fetch_status(self, params=...):  # -> dict[str, Any]:
        """
        the latest known information on the availability of the exchange API
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `status structure <https://docs.ccxt.com/#/?id=exchange-status-structure>`
        """
        ...

    def fetch_currencies(self, params=...) -> Currencies:
        """
        fetches all available currencies on an exchange

        https://docs.delta.exchange/#get-list-of-all-assets

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an associative dictionary of currencies
        """
        ...

    def load_markets(self, reload=..., params=...):  # -> dict[Any, Any]:
        ...
    def index_by_stringified_numeric_id(self, input):  # -> dict[Any, Any] | None:
        ...
    def fetch_markets(self, params=...) -> List[Market]:
        """
        retrieves data on all markets for delta

        https://docs.delta.exchange/#get-list-of-products

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: an array of objects representing market data
        """
        ...

    def parse_ticker(self, ticker: dict, market: Market = ...) -> Ticker: ...
    def fetch_ticker(self, symbol: str, params=...) -> Ticker:
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

        https://docs.delta.exchange/#get-ticker-for-a-product-by-symbol

        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def fetch_tickers(self, symbols: Strings = ..., params=...) -> Tickers:
        """
        fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

        https://docs.delta.exchange/#get-tickers-for-products

        :param str[]|None symbols: unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a dictionary of `ticker structures <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        ...

    def fetch_order_book(self, symbol: str, limit: Int = ..., params=...) -> OrderBook:
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data

        https://docs.delta.exchange/#get-l2-orderbook

        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        ...

    def parse_trade(self, trade: dict, market: Market = ...) -> Trade: ...
    def fetch_trades(
        self, symbol: str, since: Int = ..., limit: Int = ..., params=...
    ) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol

        https://docs.delta.exchange/#get-public-trades

        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        ...

    def parse_ohlcv(self, ohlcv, market: Market = ...) -> list: ...
    def fetch_ohlcv(
        self, symbol: str, timeframe=..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[list]:
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

        https://docs.delta.exchange/#delta-exchange-api-v2-historical-ohlc-candles-sparklines

        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.until]: timestamp in ms of the latest candle to fetch
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        ...

    def parse_balance(self, response) -> Balances: ...
    def fetch_balance(self, params=...) -> Balances:
        """
        query for balance and get the amount of funds available for trading or funds locked in orders

        https://docs.delta.exchange/#get-wallet-balances

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        ...

    def fetch_position(self, symbol: str, params=...):  # -> dict[Any, Any]:
        """
        fetch data on a single open contract trade position

        https://docs.delta.exchange/#get-position

        :param str symbol: unified market symbol of the market the position is held in, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `position structure <https://docs.ccxt.com/#/?id=position-structure>`
        """
        ...

    def fetch_positions(
        self, symbols: Strings = ..., params=...
    ):  # -> dict[Any, Any] | list[Any]:
        """
        fetch all open positions

        https://docs.delta.exchange/#get-margined-positions

        :param str[]|None symbols: list of unified market symbols
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `position structure <https://docs.ccxt.com/#/?id=position-structure>`
        """
        ...

    def parse_position(
        self, position: dict, market: Market = ...
    ):  # -> dict[Any, Any]:
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
    ):  # -> Order:
        """
        create a trade order

        https://docs.delta.exchange/#place-order

        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param bool [params.reduceOnly]: *contract only* indicates if self order is to reduce the size of a position
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

        https://docs.delta.exchange/#edit-order

        :param str id: order id
        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of the currency you want to trade in units of the base currency
        :param float [price]: the price at which the order is to be fulfilled, in units of the quote currency
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def cancel_order(self, id: str, symbol: Str = ..., params=...):  # -> Order:
        """
        cancels an open order

        https://docs.delta.exchange/#cancel-order

        :param str id: order id
        :param str symbol: unified symbol of the market the order was made in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def cancel_all_orders(
        self, symbol: Str = ..., params=...
    ):  # -> list[OrderedDict[Any, Any] | dict[Any, Any]]:
        """
        cancel all open orders in a market

        https://docs.delta.exchange/#cancel-all-open-orders

        :param str symbol: unified market symbol of the market to cancel orders in
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_open_orders(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[Order]:
        """
        fetch all unfilled currently open orders

        https://docs.delta.exchange/#get-active-orders

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

        https://docs.delta.exchange/#get-order-history-cancelled-and-closed

        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Order[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        ...

    def fetch_orders_with_method(
        self, method, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        ...
    def fetch_my_trades(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        fetch all trades made by the user

        https://docs.delta.exchange/#get-user-fills-by-filters

        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch trades for
        :param int [limit]: the maximum number of trades structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns Trade[]: a list of `trade structures <https://docs.ccxt.com/#/?id=trade-structure>`
        """
        ...

    def fetch_ledger(
        self, code: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ) -> List[LedgerEntry]:
        """
        fetch the history of changes, actions done by the user or operations that altered the balance of the user

        https://docs.delta.exchange/#get-wallet-transactions

        :param str [code]: unified currency code, default is None
        :param int [since]: timestamp in ms of the earliest ledger entry, default is None
        :param int [limit]: max number of ledger entries to return, default is None
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ledger structure <https://docs.ccxt.com/#/?id=ledger>`
        """
        ...

    def parse_ledger_entry_type(self, type):  # -> str | None:
        ...
    def parse_ledger_entry(
        self, item: dict, currency: Currency = ...
    ) -> LedgerEntry: ...
    def fetch_deposit_address(self, code: str, params=...) -> DepositAddress:
        """
        fetch the deposit address for a currency associated with self account
        :param str code: unified currency code
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param str [params.network]: unified network code
        :returns dict: an `address structure <https://docs.ccxt.com/#/?id=address-structure>`
        """
        ...

    def parse_deposit_address(
        self, depositAddress, currency: Currency = ...
    ) -> DepositAddress: ...
    def fetch_funding_rate(self, symbol: str, params=...) -> FundingRate:
        """
        fetch the current funding rate

        https://docs.delta.exchange/#get-ticker-for-a-product-by-symbol

        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `funding rate structure <https://docs.ccxt.com/#/?id=funding-rate-structure>`
        """
        ...

    def fetch_funding_rates(self, symbols: Strings = ..., params=...) -> FundingRates:
        """
        fetch the funding rate for multiple markets

        https://docs.delta.exchange/#get-tickers-for-products

        :param str[]|None symbols: list of unified market symbols
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `funding rate structures <https://docs.ccxt.com/#/?id=funding-rates-structure>`, indexed by market symbols
        """
        ...

    def parse_funding_rate(self, contract, market: Market = ...) -> FundingRate: ...
    def add_margin(self, symbol: str, amount: float, params=...) -> MarginModification:
        """
        add margin

        https://docs.delta.exchange/#add-remove-position-margin

        :param str symbol: unified market symbol
        :param float amount: amount of margin to add
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `margin structure <https://docs.ccxt.com/#/?id=add-margin-structure>`
        """
        ...

    def reduce_margin(
        self, symbol: str, amount: float, params=...
    ) -> MarginModification:
        """
        remove margin from a position

        https://docs.delta.exchange/#add-remove-position-margin

        :param str symbol: unified market symbol
        :param float amount: the amount of margin to remove
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `margin structure <https://docs.ccxt.com/#/?id=reduce-margin-structure>`
        """
        ...

    def modify_margin_helper(
        self, symbol: str, amount, type, params=...
    ) -> MarginModification: ...
    def parse_margin_modification(
        self, data: dict, market: Market = ...
    ) -> MarginModification: ...
    def fetch_open_interest(
        self, symbol: str, params=...
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        """
        retrieves the open interest of a derivative market

        https://docs.delta.exchange/#get-ticker-for-a-product-by-symbol

        :param str symbol: unified market symbol
        :param dict [params]: exchange specific parameters
        :returns dict} an open interest structure{@link https://docs.ccxt.com/#/?id=open-interest-structure:
        """
        ...

    def parse_open_interest(
        self, interest, market: Market = ...
    ):  # -> OrderedDict[Any, Any] | dict[Any, Any]:
        ...
    def fetch_leverage(self, symbol: str, params=...) -> Leverage:
        """
        fetch the set leverage for a market

        https://docs.delta.exchange/#get-order-leverage

        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `leverage structure <https://docs.ccxt.com/#/?id=leverage-structure>`
        """
        ...

    def parse_leverage(self, leverage: dict, market: Market = ...) -> Leverage: ...
    def set_leverage(self, leverage: Int, symbol: Str = ..., params=...):  # -> Any:
        """
        set the level of leverage for a market

        https://docs.delta.exchange/#change-order-leverage

        :param float leverage: the rate of leverage
        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: response from the exchange
        """
        ...

    def fetch_settlement_history(
        self, symbol: Str = ..., since: Int = ..., limit: Int = ..., params=...
    ):  # -> list[Any] | list[object]:
        """
        fetches historical settlement records

        https://docs.delta.exchange/#get-product-settlement-prices

        :param str symbol: unified market symbol of the settlement history
        :param int [since]: timestamp in ms
        :param int [limit]: number of records
        :param dict [params]: exchange specific params
        :returns dict[]: a list of `settlement history objects <https://docs.ccxt.com/#/?id=settlement-history-structure>`
        """
        ...

    def parse_settlement(self, settlement, market):  # -> dict[str, Any]:
        ...
    def parse_settlements(self, settlements, market):  # -> list[Any]:
        ...
    def fetch_greeks(self, symbol: str, params=...) -> Greeks:
        """
        fetches an option contracts greeks, financial metrics used to measure the factors that affect the price of an options contract

        https://docs.delta.exchange/#get-ticker-for-a-product-by-symbol

        :param str symbol: unified symbol of the market to fetch greeks for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `greeks structure <https://docs.ccxt.com/#/?id=greeks-structure>`
        """
        ...

    def parse_greeks(self, greeks: dict, market: Market = ...) -> Greeks: ...
    def close_all_positions(self, params=...) -> List[Position]:
        """
        closes all open positions for a market type

        https://docs.delta.exchange/#close-all-positions

        :param dict [params]: extra parameters specific to the exchange API endpoint
        :param int [params.user_id]: the users id
        :returns dict[]: A list of `position structures <https://docs.ccxt.com/#/?id=position-structure>`
        """
        ...

    def fetch_margin_mode(self, symbol: str, params=...) -> MarginMode:
        """
        fetches the margin mode of a trading pair

        https://docs.delta.exchange/#get-user

        :param str symbol: unified symbol of the market to fetch the margin mode for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `margin mode structure <https://docs.ccxt.com/#/?id=margin-mode-structure>`
        """
        ...

    def parse_margin_mode(self, marginMode: dict, market=...) -> MarginMode: ...
    def fetch_option(self, symbol: str, params=...) -> Option:
        """
        fetches option data that is commonly found in an option chain

        https://docs.delta.exchange/#get-ticker-for-a-product-by-symbol

        :param str symbol: unified market symbol
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: an `option chain structure <https://docs.ccxt.com/#/?id=option-chain-structure>`
        """
        ...

    def parse_option(
        self, chain: dict, currency: Currency = ..., market: Market = ...
    ) -> Option: ...
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
