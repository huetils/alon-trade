"""
This type stub file was generated by pyright.
"""

from decimal import Decimal
from ccxt.base.exchange import Exchange

async def fetch_balance(exchange: Exchange, currency: str) -> Decimal:
    """
    Fetch the free balance of the specified currency from the exchange.
    """
    ...

async def transfer_funds(source_exchange: Exchange, dest_exchange: Exchange, currency: str, amount: Decimal) -> bool:
    """
    Transfer funds from one exchange to another.
    """
    ...

async def balance_monitor(exchanges: dict[str, Exchange]) -> None:
    """
    Monitor and balance funds across exchanges to prevent liquidation.
    """
    ...

async def start_balance_manager(exchanges_config: list[dict[str, str]]) -> None:
    """
    Initialize exchanges and start balance monitoring.
    """
    ...

if __name__ == "__main__":
    ...
