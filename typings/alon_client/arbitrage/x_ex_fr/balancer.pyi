"""
This type stub file was generated by pyright.
"""

from decimal import Decimal
from typing import Any, Callable, Dict

from ccxt.base.exchange import Exchange

class BalanceManager:
    def __init__(
        self,
        exchanges_config: list[dict[str, str]],
        fetch_balance: Callable[[Exchange, str], Any],
        transfer_funds: Callable[[Exchange, Exchange, str, Decimal], Any],
        config: Dict[str, Any],
    ) -> None:
        """
        Initializes the BalanceManager class.

        Args:
            exchanges_config: List of exchange configurations.
            fetch_balance: Function to fetch balance from an exchange.
            transfer_funds: Function to transfer funds between exchanges.
            config: Configuration settings.
        """
        ...

    async def run(self) -> None:
        """Initialize exchanges and start balance monitoring."""
        ...

if __name__ == "__main__":
    async def mock_fetch_balance(exchange: Exchange, currency: str) -> Decimal: ...
    async def mock_transfer_funds(
        source_exchange: Exchange,
        dest_exchange: Exchange,
        currency: str,
        amount: Decimal,
    ) -> bool: ...

    exchanges_config = ...
    config: dict[str, str | int] = ...
    balance_manager = ...
