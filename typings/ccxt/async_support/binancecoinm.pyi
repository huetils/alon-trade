"""
This type stub file was generated by pyright.
"""

from ccxt.abstract.binancecoinm import ImplicitAPI
from ccxt.async_support.binance import binance

class binancecoinm(binance, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
    async def transfer_in(self, code: str, amount, params=...): ...
    async def transfer_out(self, code: str, amount, params=...): ...
