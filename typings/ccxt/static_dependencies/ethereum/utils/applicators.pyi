"""
This type stub file was generated by pyright.
"""

from typing import Any, Callable, Dict, Generator, List, Tuple

from .decorators import return_arg_type
from .functional import to_dict

Formatters = Callable[[List[Any]], List[Any]]

@return_arg_type(2)
def apply_formatter_at_index(
    formatter: Callable[..., Any], at_index: int, value: List[Any]
) -> Generator[List[Any], None, None]: ...
def combine_argument_formatters(
    *formatters: List[Callable[..., Any]],
) -> Formatters: ...
@return_arg_type(1)
def apply_formatters_to_sequence(
    formatters: List[Any], sequence: List[Any]
) -> Generator[List[Any], None, None]: ...
def apply_formatter_if(
    condition: Callable[..., bool], formatter: Callable[..., Any], value: Any
) -> Any: ...
@to_dict
def apply_formatters_to_dict(
    formatters: Dict[Any, Any], value: Dict[Any, Any]
) -> Generator[Tuple[Any, Any], None, None]: ...
@return_arg_type(1)
def apply_formatter_to_array(
    formatter: Callable[..., Any], value: List[Any]
) -> Generator[List[Any], None, None]: ...
def apply_one_of_formatters(
    formatter_condition_pairs: Tuple[Tuple[Callable[..., Any], Callable[..., Any]]],
    value: Any,
) -> Any: ...
@to_dict
def apply_key_map(
    key_mappings: Dict[Any, Any], value: Dict[Any, Any]
) -> Generator[Tuple[Any, Any], None, None]: ...
