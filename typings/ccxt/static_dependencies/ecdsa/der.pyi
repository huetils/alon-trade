"""
This type stub file was generated by pyright.
"""

class UnexpectedDER(Exception): ...

def encode_constructed(tag, value): ...
def encode_integer(r):  # -> bytes:
    ...
def encode_bitstring(s): ...
def encode_octet_string(s): ...
def encode_oid(first, second, *pieces):  # -> bytes:
    ...
def encode_sequence(*encoded_pieces):  # -> bytes:
    ...
def encode_number(n):  # -> bytes:
    ...
def remove_constructed(string):  # -> tuple[Any | int, Any, Any]:
    ...
def remove_sequence(string):  # -> tuple[Any, Any]:
    ...
def remove_octet_string(string):  # -> tuple[Any, Any]:
    ...
def remove_object(string):  # -> tuple[tuple[Any, ...], Any]:
    ...
def remove_integer(string):  # -> tuple[int, Any]:
    ...
def read_number(string):  # -> tuple[Any | int, int]:
    ...
def encode_length(l):  # -> bytes:
    ...
def read_length(string):  # -> tuple[Any | int, Literal[1]] | tuple[int, Any | int]:
    ...
def remove_bitstring(string):  # -> tuple[Any, Any]:
    ...
def unpem(pem):  # -> bytes:
    ...
def topem(der, name):  # -> bytes:
    ...
