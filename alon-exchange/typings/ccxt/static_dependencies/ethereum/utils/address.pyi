"""
This type stub file was generated by pyright.
"""

from typing import Any, Union
from ..typing import Address, AnyAddress, ChecksumAddress, HexAddress

_HEX_ADDRESS_REGEXP = ...
def is_hex_address(value: Any) -> bool:
    """
    Checks if the given string of text type is an address in hexadecimal encoded form.
    """
    ...

def is_binary_address(value: Any) -> bool:
    """
    Checks if the given string is an address in raw bytes form.
    """
    ...

def is_address(value: Any) -> bool:
    """
    Is the given string an address in any of the known formats?
    """
    ...

def to_normalized_address(value: Union[AnyAddress, str, bytes]) -> HexAddress:
    """
    Converts an address to its normalized hexadecimal representation.
    """
    ...

def is_normalized_address(value: Any) -> bool:
    """
    Returns whether the provided value is an address in its normalized form.
    """
    ...

def to_canonical_address(address: Union[AnyAddress, str, bytes]) -> Address:
    """
    Convert a valid address to its canonical form (20-length bytes).
    """
    ...

def is_canonical_address(address: Any) -> bool:
    """
    Returns `True` if the `value` is an address in its canonical form.
    """
    ...

def is_same_address(left: AnyAddress, right: AnyAddress) -> bool:
    """
    Checks if both addresses are same or not.
    """
    ...

def to_checksum_address(value: Union[AnyAddress, str, bytes]) -> ChecksumAddress:
    """
    Makes a checksum address given a supported format.
    """
    ...

def is_checksum_address(value: Any) -> bool:
    ...

def is_checksum_formatted_address(value: Any) -> bool:
    ...

