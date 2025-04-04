"""
This type stub file was generated by pyright.
"""

from typing import Union

def to_bytes(val: Union[bool, bytearray, bytes, int, str, memoryview]) -> bytes:
    """
    Equivalent to: `eth_utils.hexstr_if_str(eth_utils.to_bytes, val)` .

    Convert a hex string, integer, or bool, to a bytes representation.
    Alternatively, pass through bytes or bytearray as a bytes value.
    """
    ...

def hexstr_to_bytes(hexstr: str) -> bytes: ...
