"""
This type stub file was generated by pyright.
"""

from ccxt.base.exchange import Exchange

async def initialize_exchange(
    exchange_id: str, api_key: str, api_secret: str, api_password: str
) -> Exchange:
    """
    Initialize and return a CCXT Pro exchange instance.
    """
    ...
