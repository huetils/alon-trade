"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Tuple
from ccxt.base.exchange import Exchange

@dataclass
class FundingRate:
    exchange: str
    symbol: str
    funding_rate: Decimal
    timestamp: datetime
    ...


@dataclass
class Position:
    long_exchange: str
    short_exchange: str
    symbol: str
    funding_time: datetime
    ...


latest_funding_rates: Dict[Tuple[str, str], FundingRate] = ...
open_positions: Dict[str, Position] = ...
async def funding_rate_collector(exchange: Exchange, market: str) -> None:
    """
    Collects funding rates from a specific exchange and updates the latest_funding_rates dictionary.
    """
    ...

async def funding_rate_analyzer() -> None:
    """
    Identifies arbitrage opportunities by comparing funding rates across exchanges.
    """
    ...

async def funding_rate_arbitrage(exchanges_config: List[Dict[str, Any]]) -> None:
    """
    Initializes multiple exchanges, starts funding rate collectors, and runs arbitrage strategy.
    """
    ...

