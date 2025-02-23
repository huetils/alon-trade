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
            "id": "okx",
            "api_key": os.getenv("OKX_API_KEY", ""),
            "api_secret": os.getenv("OKX_API_SECRET", ""),
            "api_password": os.getenv("OKX_API_PASSWORD", ""),
        }
    ],
    "ORDER_FILL_TIMEOUT_SEC": 5,
    "MAX_RETRIES": 3,
    "MIN_ABS_FUNDING_RATE": 0.001,
    "TRADE_AMOUNT_PERCENT": 1.0,
    "LEVERAGE_LIMIT": 10,
    "TOP_OPPORTUNITIES": 5,
    "CURRENCY": "USDT",
    "FUNDING_INTERVAL_HOURS": 8,
    "CHECK_INTERVAL": 10,
    "TIME_TO_FUNDING_THRESHOLD": 5,
    "FETCH_BALANCE_MAX_RETRIES": 3,
}

config = load_config()
configurations = {
    key: type(defaults[key])(os.getenv(key, config.get(key, defaults[key])))
    for key in defaults
}
