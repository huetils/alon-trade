"""
This type stub file was generated by pyright.
"""

from ..typing.abi import TypeStr

def parse_type_str(
    expected_base=..., with_arrlist=...
):  # -> Callable[..., classmethod[Any, Callable[..., Any], Any]]:
    """
    Used by BaseCoder subclasses as a convenience for implementing the
    ``from_type_str`` method required by ``ABIRegistry``.  Useful if normalizing
    then parsing a type string with an (optional) expected base is required in
    that method.
    """
    ...

def parse_tuple_type_str(
    old_from_type_str,
):  # -> classmethod[Any, Callable[..., Any], Any]:
    """
    Used by BaseCoder subclasses as a convenience for implementing the
    ``from_type_str`` method required by ``ABIRegistry``.  Useful if normalizing
    then parsing a tuple type string is required in that method.
    """
    ...

class BaseCoder:
    """
    Base class for all encoder and decoder classes.
    """

    is_dynamic = ...
    def __init__(self, **kwargs) -> None: ...
    def validate(self):  # -> None:
        ...
    @classmethod
    def from_type_str(cls, type_str: TypeStr, registry) -> BaseCoder:
        """
        Used by :any:`ABIRegistry` to get an appropriate encoder or decoder
        instance for the given type string and type registry.
        """
        ...
