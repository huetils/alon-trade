"""
This type stub file was generated by pyright.
"""

import logging
from functools import cached_property
from typing import Any, Dict, Tuple, Type, TypeVar, Union

DEBUG2_LEVEL_NUM = ...
TLogger = TypeVar("TLogger", bound=logging.Logger)

class ExtendedDebugLogger(logging.Logger):
    """
    Logging class that can be used for lower level debug logging.
    """
    @cached_property
    def show_debug2(self) -> bool: ...
    def debug2(self, message: str, *args: Any, **kwargs: Any) -> None: ...
    def __reduce__(self) -> Tuple[Any, ...]: ...

def setup_DEBUG2_logging() -> None:
    """
    Installs the `DEBUG2` level logging levels to the main logging module.
    """
    ...

def get_logger(
    name: str, logger_class: Union[Type[TLogger], None] = ...
) -> TLogger: ...
def get_extended_debug_logger(name: str) -> ExtendedDebugLogger: ...

THasLoggerMeta = TypeVar("THasLoggerMeta", bound="HasLoggerMeta")

class HasLoggerMeta(type):
    """
    Assigns a logger instance to a class, derived from the import path and name.

    This metaclass uses `__qualname__` to identify a unique and meaningful name
    to use when creating the associated logger for a given class.
    """

    logger_class = logging.Logger
    def __new__(
        mcls: Type[THasLoggerMeta],
        name: str,
        bases: Tuple[Type[Any]],
        namespace: Dict[str, Any],
    ) -> THasLoggerMeta: ...
    @classmethod
    def replace_logger_class(
        mcls: Type[THasLoggerMeta], value: Type[logging.Logger]
    ) -> Type[THasLoggerMeta]: ...
    @classmethod
    def meta_compat(
        mcls: Type[THasLoggerMeta], other: Type[type]
    ) -> Type[THasLoggerMeta]: ...

class _BaseHasLogger(metaclass=HasLoggerMeta):
    logger: logging.Logger = ...

class HasLogger(_BaseHasLogger): ...

HasExtendedDebugLoggerMeta = ...

class _BaseHasExtendedDebugLogger(metaclass=HasExtendedDebugLoggerMeta):
    logger: ExtendedDebugLogger = ...

class HasExtendedDebugLogger(_BaseHasExtendedDebugLogger): ...
