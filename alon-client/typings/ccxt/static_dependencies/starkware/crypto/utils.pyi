"""
This type stub file was generated by pyright.
"""

import sys
from typing import AsyncGenerator, Literal, Optional, TypeVar
from typing_extensions import Literal

if sys.version_info.minor >= 11:
    ...
else:
    ...
T = TypeVar("T")
P = ...
K = TypeVar("K")
V = TypeVar("V")
TAsyncGenerator = TypeVar("TAsyncGenerator", bound=AsyncGenerator)
NumType = TypeVar("NumType", int, float)
HASH_BYTES = ...
Endianness = Literal["big", "little"]
TComparable = TypeVar("TComparable", bound="Comparable")
def to_bytes(value: int, length: Optional[int] = ..., byte_order: Optional[Endianness] = ..., signed: Optional[bool] = ...) -> bytes:
    """
    Converts the given integer to a bytes object of given length and byte order.
    The default values are 32B width (which is the hash result width) and 'big', respectively.
    """
    ...

def from_bytes(value: bytes, byte_order: Optional[Endianness] = ..., signed: Optional[bool] = ...) -> int:
    """
    Converts the given bytes object (parsed according to the given byte order) to an integer.
    Default byte order is 'big'.
    """
    ...

