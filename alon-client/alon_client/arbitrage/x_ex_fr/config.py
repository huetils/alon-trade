import os
from typing import Any

import yaml

DEFAULT_CONFIG_FILE = "config.yaml"


def load_config(config_file: str = DEFAULT_CONFIG_FILE) -> dict[str, Any]:
    try:
        with open(config_file, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Config file '{config_file}' not found. Using environment variables.")
        return {}


defaults: dict[str, Any] = {
    "EXCHANGES": [
        {
            "exchange_id": "okx",
            "api_key": os.getenv("OKX_API_KEY", ""),
            "api_secret": os.getenv("OKX_API_SECRET", ""),
            "api_password": os.getenv("OKX_API_PASSWORD", ""),
        },
        {
            "exchange_id": "bybit",
            "api_key": os.getenv("BYBIT_API_KEY", ""),
            "api_secret": os.getenv("BYBIT_API_SECRET", ""),
            "api_password": os.getenv("BYBIT_API_PASSWORD", ""),
        },
    ],
    "ORDER_FILL_TIMEOUT_SEC": 5,  # Maximum time (seconds) to wait for order fulfillment
    "MAX_RETRIES": 3,  # Maximum number of retries for failed operations
    "MIN_ARBITRAGE_THRESHOLD": 0.0005,  # Minimum funding rate difference required to open arbitrage positions
    "MIN_ABS_FUNDING_RATE": 0.001,  # Minimum absolute funding rate to consider a trade
    "TRADE_AMOUNT_PERCENT": 1.0,  # Percentage of balance allocated per trade
    "LEVERAGE_LIMIT": 10,  # Maximum leverage allowed for trades
    "TOP_OPPORTUNITIES": 5,  # Number of top arbitrage opportunities to consider
    "CURRENCY": "USDT",  # Base currency for balance monitoring and transfers
    "FUNDING_INTERVAL_HOURS": 8,  # Interval (hours) for funding rate updates
    "CHECK_INTERVAL": 1,  # Interval (seconds) for monitoring funding rates
    "TIME_TO_FUNDING_THRESHOLD": 5,  # Minimum hours before funding payout to consider a trade
    "FETCH_BALANCE_MAX_RETRIES": 3,  # Maximum retries for fetching balances
    "MIN_BALANCE_THRESHOLD": 50,  # Minimum required balance on an exchange before triggering a transfer
    "TRANSFER_THRESHOLD": 500,  # Balance threshold above which funds are transferred to other exchanges
    "BALANCE_CHECK_INTERVAL": 60,  # Time interval (seconds) for checking and rebalancing account balances
}

config = load_config()
configurations = {
    key: type(defaults[key])(os.getenv(key, config.get(key, defaults[key])))
    for key in defaults
}
