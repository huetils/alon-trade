"""
This type stub file was generated by pyright.
"""

class UnknownCurveError(Exception): ...

def orderlen(order):  # -> int:
    ...

class Curve:
    def __init__(self, name, curve, generator, oid, openssl_name=...) -> None: ...

NIST192p = ...
NIST224p = ...
NIST256p = ...
NIST384p = ...
NIST521p = ...
SECP256k1 = ...
curves = ...

def find_curve(oid_curve):  # -> Curve:
    ...
