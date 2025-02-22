"""
This type stub file was generated by pyright.
"""

from enum import Enum
from typing import Any, Dict, List, Optional, TypedDict

"""
TypedDict structures for TypedData
"""

class Revision(Enum):
    """
    Enum representing the revision of the specification to be used.
    """

    V0 = ...
    V1 = ...

class ParameterDict(TypedDict):
    """
    TypedDict representing a Parameter object
    """

    name: str
    type: str
    ...

class StarkNetDomainDict(TypedDict):
    """
    TypedDict representing a domain object (both StarkNetDomain, StarknetDomain).
    """

    name: str
    version: str
    chainId: str
    revision: Optional[Revision]
    ...

class TypedDataDict(TypedDict):
    """
    TypedDict representing a TypedData object
    """

    types: Dict[str, List[ParameterDict]]
    primaryType: str
    domain: StarkNetDomainDict
    message: Dict[str, Any]
    ...
