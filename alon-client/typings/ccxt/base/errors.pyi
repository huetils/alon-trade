"""
This type stub file was generated by pyright.
"""

error_hierarchy = ...
class BaseError(Exception):
    ...


class ExchangeError(BaseError):
    ...


class AuthenticationError(ExchangeError):
    ...


class PermissionDenied(AuthenticationError):
    ...


class AccountNotEnabled(PermissionDenied):
    ...


class AccountSuspended(AuthenticationError):
    ...


class ArgumentsRequired(ExchangeError):
    ...


class BadRequest(ExchangeError):
    ...


class BadSymbol(BadRequest):
    ...


class OperationRejected(ExchangeError):
    ...


class NoChange(OperationRejected):
    ...


class MarginModeAlreadySet(NoChange):
    ...


class MarketClosed(OperationRejected):
    ...


class ManualInteractionNeeded(OperationRejected):
    ...


class InsufficientFunds(ExchangeError):
    ...


class InvalidAddress(ExchangeError):
    ...


class AddressPending(InvalidAddress):
    ...


class InvalidOrder(ExchangeError):
    ...


class OrderNotFound(InvalidOrder):
    ...


class OrderNotCached(InvalidOrder):
    ...


class OrderImmediatelyFillable(InvalidOrder):
    ...


class OrderNotFillable(InvalidOrder):
    ...


class DuplicateOrderId(InvalidOrder):
    ...


class ContractUnavailable(InvalidOrder):
    ...


class NotSupported(ExchangeError):
    ...


class InvalidProxySettings(ExchangeError):
    ...


class ExchangeClosedByUser(ExchangeError):
    ...


class OperationFailed(BaseError):
    ...


class NetworkError(OperationFailed):
    ...


class DDoSProtection(NetworkError):
    ...


class RateLimitExceeded(NetworkError):
    ...


class ExchangeNotAvailable(NetworkError):
    ...


class OnMaintenance(ExchangeNotAvailable):
    ...


class InvalidNonce(NetworkError):
    ...


class ChecksumError(InvalidNonce):
    ...


class RequestTimeout(NetworkError):
    ...


class BadResponse(OperationFailed):
    ...


class NullResponse(BadResponse):
    ...


class CancelPending(OperationFailed):
    ...


class UnsubscribeError(BaseError):
    ...


__all__ = ['error_hierarchy', 'BaseError', 'ExchangeError', 'AuthenticationError', 'PermissionDenied', 'AccountNotEnabled', 'AccountSuspended', 'ArgumentsRequired', 'BadRequest', 'BadSymbol', 'OperationRejected', 'NoChange', 'MarginModeAlreadySet', 'MarketClosed', 'ManualInteractionNeeded', 'InsufficientFunds', 'InvalidAddress', 'AddressPending', 'InvalidOrder', 'OrderNotFound', 'OrderNotCached', 'OrderImmediatelyFillable', 'OrderNotFillable', 'DuplicateOrderId', 'ContractUnavailable', 'NotSupported', 'InvalidProxySettings', 'ExchangeClosedByUser', 'OperationFailed', 'NetworkError', 'DDoSProtection', 'RateLimitExceeded', 'ExchangeNotAvailable', 'OnMaintenance', 'InvalidNonce', 'ChecksumError', 'RequestTimeout', 'BadResponse', 'NullResponse', 'CancelPending', 'UnsubscribeError']
