"""
This type stub file was generated by pyright.
"""

from typing import List

CairoData = List[int]
MAX_UINT256 = ...
MIN_UINT256 = ...

def uint256_range_check(value: int):  # -> None:
    ...

MIN_FELT = ...
MAX_FELT = ...

def is_in_felt_range(value: int) -> bool: ...
def cairo_vm_range_check(value: int):  # -> None:
    ...
def encode_shortstring(text: str) -> int:
    """
    A function which encodes short string value (at most 31 characters) into cairo felt (MSB as first character)

    :param text: A short string value in python
    :return: Short string value encoded into felt
    """
    ...

def decode_shortstring(value: int) -> str:
    """
    A function which decodes a felt value to short string (at most 31 characters)

    :param value: A felt value
    :return: Decoded string which is corresponds to that felt
    """
    ...
