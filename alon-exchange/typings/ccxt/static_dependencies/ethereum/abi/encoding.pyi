"""
This type stub file was generated by pyright.
"""

import abc
from typing import Any, Optional, Type
from .base import BaseCoder, parse_tuple_type_str, parse_type_str

class BaseEncoder(BaseCoder, metaclass=abc.ABCMeta):
    """
    Base class for all encoder classes.  Subclass this if you want to define a
    custom encoder class.  Subclasses must also implement
    :any:`BaseCoder.from_type_str`.
    """
    @abc.abstractmethod
    def encode(self, value: Any) -> bytes:
        """
        Encodes the given value as a sequence of bytes.  Should raise
        :any:`exceptions.EncodingError` if ``value`` cannot be encoded.
        """
        ...
    
    @abc.abstractmethod
    def validate_value(self, value: Any) -> None:
        """
        Checks whether or not the given value can be encoded by this encoder.
        If the given value cannot be encoded, must raise
        :any:`exceptions.EncodingError`.
        """
        ...
    
    @classmethod
    def invalidate_value(cls, value: Any, exc: Type[Exception] = ..., msg: Optional[str] = ...) -> None:
        """
        Throws a standard exception for when a value is not encodable by an
        encoder.
        """
        ...
    
    def __call__(self, value: Any) -> bytes:
        ...
    


class TupleEncoder(BaseEncoder):
    encoders = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def validate(self): # -> None:
        ...
    
    def validate_value(self, value): # -> None:
        ...
    
    def encode(self, values): # -> bytes:
        ...
    
    @parse_tuple_type_str
    def from_type_str(cls, abi_type, registry):
        ...
    


class FixedSizeEncoder(BaseEncoder):
    value_bit_size = ...
    data_byte_size = ...
    encode_fn = ...
    type_check_fn = ...
    is_big_endian = ...
    def validate(self): # -> None:
        ...
    
    def validate_value(self, value):
        ...
    
    def encode(self, value): # -> object | curry:
        ...
    


class Fixed32ByteSizeEncoder(FixedSizeEncoder):
    data_byte_size = ...


class BooleanEncoder(Fixed32ByteSizeEncoder):
    value_bit_size = ...
    is_big_endian = ...
    @classmethod
    def validate_value(cls, value): # -> None:
        ...
    
    @classmethod
    def encode_fn(cls, value): # -> Literal[b"\x01", b"\x00"]:
        ...
    
    @parse_type_str("bool")
    def from_type_str(cls, abi_type, registry):
        ...
    


class PackedBooleanEncoder(BooleanEncoder):
    data_byte_size = ...


class NumberEncoder(Fixed32ByteSizeEncoder):
    is_big_endian = ...
    bounds_fn = ...
    illegal_value_fn = ...
    type_check_fn = ...
    def validate(self): # -> None:
        ...
    
    def validate_value(self, value): # -> None:
        ...
    


class UnsignedIntegerEncoder(NumberEncoder):
    encode_fn = ...
    bounds_fn = ...
    type_check_fn = ...
    @parse_type_str("uint")
    def from_type_str(cls, abi_type, registry):
        ...
    


encode_uint_256 = ...
class PackedUnsignedIntegerEncoder(UnsignedIntegerEncoder):
    @parse_type_str("uint")
    def from_type_str(cls, abi_type, registry):
        ...
    


class SignedIntegerEncoder(NumberEncoder):
    bounds_fn = ...
    type_check_fn = ...
    def encode_fn(self, value): # -> bytes:
        ...
    
    def encode(self, value): # -> object | curry:
        ...
    
    @parse_type_str("int")
    def from_type_str(cls, abi_type, registry):
        ...
    


class PackedSignedIntegerEncoder(SignedIntegerEncoder):
    @parse_type_str("int")
    def from_type_str(cls, abi_type, registry):
        ...
    


class BaseFixedEncoder(NumberEncoder):
    frac_places = ...
    @staticmethod
    def type_check_fn(value): # -> bool:
        ...
    
    @staticmethod
    def illegal_value_fn(value): # -> bool:
        ...
    
    def validate_value(self, value): # -> None:
        ...
    
    def validate(self): # -> None:
        ...
    


class UnsignedFixedEncoder(BaseFixedEncoder):
    def bounds_fn(self, value_bit_size): # -> Tuple[Decimal, Decimal]:
        ...
    
    def encode_fn(self, value): # -> bytes:
        ...
    
    @parse_type_str("ufixed")
    def from_type_str(cls, abi_type, registry):
        ...
    


class PackedUnsignedFixedEncoder(UnsignedFixedEncoder):
    @parse_type_str("ufixed")
    def from_type_str(cls, abi_type, registry):
        ...
    


class SignedFixedEncoder(BaseFixedEncoder):
    def bounds_fn(self, value_bit_size): # -> Tuple[Decimal, Decimal]:
        ...
    
    def encode_fn(self, value): # -> bytes:
        ...
    
    def encode(self, value): # -> object | curry:
        ...
    
    @parse_type_str("fixed")
    def from_type_str(cls, abi_type, registry):
        ...
    


class PackedSignedFixedEncoder(SignedFixedEncoder):
    @parse_type_str("fixed")
    def from_type_str(cls, abi_type, registry):
        ...
    


class AddressEncoder(Fixed32ByteSizeEncoder):
    value_bit_size = ...
    encode_fn = ...
    is_big_endian = ...
    @classmethod
    def validate_value(cls, value): # -> None:
        ...
    
    def validate(self): # -> None:
        ...
    
    @parse_type_str("address")
    def from_type_str(cls, abi_type, registry):
        ...
    


class PackedAddressEncoder(AddressEncoder):
    data_byte_size = ...


class BytesEncoder(Fixed32ByteSizeEncoder):
    is_big_endian = ...
    def validate_value(self, value): # -> None:
        ...
    
    @staticmethod
    def encode_fn(value):
        ...
    
    @parse_type_str("bytes")
    def from_type_str(cls, abi_type, registry):
        ...
    


class PackedBytesEncoder(BytesEncoder):
    @parse_type_str("bytes")
    def from_type_str(cls, abi_type, registry):
        ...
    


class ByteStringEncoder(BaseEncoder):
    is_dynamic = ...
    @classmethod
    def validate_value(cls, value): # -> None:
        ...
    
    @classmethod
    def encode(cls, value): # -> bytes:
        ...
    
    @parse_type_str("bytes")
    def from_type_str(cls, abi_type, registry):
        ...
    


class PackedByteStringEncoder(ByteStringEncoder):
    is_dynamic = ...
    @classmethod
    def encode(cls, value):
        ...
    


class TextStringEncoder(BaseEncoder):
    is_dynamic = ...
    @classmethod
    def validate_value(cls, value): # -> None:
        ...
    
    @classmethod
    def encode(cls, value): # -> bytes:
        ...
    
    @parse_type_str("string")
    def from_type_str(cls, abi_type, registry):
        ...
    


class PackedTextStringEncoder(TextStringEncoder):
    is_dynamic = ...
    @classmethod
    def encode(cls, value): # -> bytes:
        ...
    


class BaseArrayEncoder(BaseEncoder):
    item_encoder = ...
    def validate(self): # -> None:
        ...
    
    def validate_value(self, value): # -> None:
        ...
    
    def encode_elements(self, value): # -> bytes:
        ...
    
    @parse_type_str(with_arrlist=True)
    def from_type_str(cls, abi_type, registry): # -> SizedArrayEncoder | DynamicArrayEncoder:
        ...
    


class PackedArrayEncoder(BaseArrayEncoder):
    array_size = ...
    def validate_value(self, value): # -> None:
        ...
    
    def encode(self, value): # -> bytes:
        ...
    
    @parse_type_str(with_arrlist=True)
    def from_type_str(cls, abi_type, registry):
        ...
    


class SizedArrayEncoder(BaseArrayEncoder):
    array_size = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def validate(self): # -> None:
        ...
    
    def validate_value(self, value): # -> None:
        ...
    
    def encode(self, value): # -> bytes:
        ...
    


class DynamicArrayEncoder(BaseArrayEncoder):
    is_dynamic = ...
    def encode(self, value): # -> bytes:
        ...
    


