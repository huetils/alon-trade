"""
This type stub file was generated by pyright.
"""

from typing import Any, Iterable, Tuple
from ..typing.abi import Decodable, TypeStr
from .decoding import ContextFramesBytesIO
from .registry import ABIRegistry

class BaseABICoder:
    """
    Base class for porcelain coding APIs.  These are classes which wrap
    instances of :class:`~.registry.ABIRegistry` to provide last-mile
    coding functionality.
    """
    def __init__(self, registry: ABIRegistry) -> None:
        """
        Constructor.

        :param registry: The registry providing the encoders to be used when
            encoding values.
        """
        ...
    


class ABIEncoder(BaseABICoder):
    """
    Wraps a registry to provide last-mile encoding functionality.
    """
    def encode_single(self, typ: TypeStr, arg: Any) -> bytes:
        """
        Encodes the python value ``arg`` as a binary value of the ABI type
        ``typ``.

        :param typ: The string representation of the ABI type that will be used
            for encoding e.g. ``'uint256'``, ``'bytes[]'``, ``'(int,int)'``,
            etc.
        :param arg: The python value to be encoded.

        :returns: The binary representation of the python value ``arg`` as a
            value of the ABI type ``typ``.
        """
        ...
    
    def encode_abi(self, types: Iterable[TypeStr], args: Iterable[Any]) -> bytes:
        """
        Encodes the python values in ``args`` as a sequence of binary values of
        the ABI types in ``types`` via the head-tail mechanism.

        :param types: An iterable of string representations of the ABI types
            that will be used for encoding e.g.  ``('uint256', 'bytes[]',
            '(int,int)')``
        :param args: An iterable of python values to be encoded.

        :returns: The head-tail encoded binary representation of the python
            values in ``args`` as values of the ABI types in ``types``.
        """
        ...
    
    def encode(self, types, args): # -> bytes:
        ...
    
    def is_encodable(self, typ: TypeStr, arg: Any) -> bool:
        """
        Determines if the python value ``arg`` is encodable as a value of the
        ABI type ``typ``.

        :param typ: A string representation for the ABI type against which the
            python value ``arg`` will be checked e.g. ``'uint256'``,
            ``'bytes[]'``, ``'(int,int)'``, etc.
        :param arg: The python value whose encodability should be checked.

        :returns: ``True`` if ``arg`` is encodable as a value of the ABI type
            ``typ``.  Otherwise, ``False``.
        """
        ...
    
    def is_encodable_type(self, typ: TypeStr) -> bool:
        """
        Returns ``True`` if values for the ABI type ``typ`` can be encoded by
        this codec.

        :param typ: A string representation for the ABI type that will be
            checked for encodability e.g. ``'uint256'``, ``'bytes[]'``,
            ``'(int,int)'``, etc.

        :returns: ``True`` if values for ``typ`` can be encoded by this codec.
            Otherwise, ``False``.
        """
        ...
    


class ABIDecoder(BaseABICoder):
    """
    Wraps a registry to provide last-mile decoding functionality.
    """
    stream_class = ContextFramesBytesIO
    def decode_single(self, typ: TypeStr, data: Decodable) -> Any:
        """
        Decodes the binary value ``data`` of the ABI type ``typ`` into its
        equivalent python value.

        :param typ: The string representation of the ABI type that will be used for
            decoding e.g. ``'uint256'``, ``'bytes[]'``, ``'(int,int)'``, etc.
        :param data: The binary value to be decoded.

        :returns: The equivalent python value of the ABI value represented in
            ``data``.
        """
        ...
    
    def decode_abi(self, types: Iterable[TypeStr], data: Decodable) -> Tuple[Any, ...]:
        """
        Decodes the binary value ``data`` as a sequence of values of the ABI types
        in ``types`` via the head-tail mechanism into a tuple of equivalent python
        values.

        :param types: An iterable of string representations of the ABI types that
            will be used for decoding e.g. ``('uint256', 'bytes[]', '(int,int)')``
        :param data: The binary value to be decoded.

        :returns: A tuple of equivalent python values for the ABI values
            represented in ``data``.
        """
        ...
    
    def decode(self, types, data): # -> Any:
        ...
    


class ABICodec(ABIEncoder, ABIDecoder):
    ...


