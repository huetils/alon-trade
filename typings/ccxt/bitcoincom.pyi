"""
This type stub file was generated by pyright.
"""

from ccxt.abstract.bitcoincom import ImplicitAPI
from ccxt.fmfwio import fmfwio

class bitcoincom(fmfwio, ImplicitAPI):
    def describe(self):  # -> dict[Any, Any] | None:
        ...
