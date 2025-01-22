"""
This type stub file was generated by pyright.
"""

from typing import Literal, Union

def int_from_hex(number: Union[str, int]) -> int:
    ...

def int_from_bytes(value: bytes, byte_order: Literal["big", "little"] = ..., signed: bool = ...) -> int:
    """
    Converts the given bytes object (parsed according to the given byte order) to an integer.
    """
    ...

