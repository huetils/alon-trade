"""
This type stub file was generated by pyright.
"""

import decimal
import numbers
from abc import ABC, abstractmethod
from typing import Any, TypeVar, Union

class Comparable(ABC):
    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...
    @abstractmethod
    def __gt__(self, other: Any) -> bool: ...

TComparable = Union[Comparable, numbers.Real, int, float, decimal.Decimal]
TValue = TypeVar("TValue", bound=TComparable)

def clamp(lower_bound: TValue, upper_bound: TValue, value: TValue) -> TValue: ...
