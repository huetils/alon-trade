"""
This type stub file was generated by pyright.
"""

from ccxt.abstract.coinbaseadvanced import ImplicitAPI
from ccxt.async_support.coinbase import coinbase

class coinbaseadvanced(coinbase, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
