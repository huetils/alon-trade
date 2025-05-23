"""
This type stub file was generated by pyright.
"""

from ccxt.ace import ace
from ccxt.alpaca import alpaca
from ccxt.ascendex import ascendex
from ccxt.base import errors
from ccxt.base.decimal_to_precision import (
    DECIMAL_PLACES,
    NO_PADDING,
    PAD_WITH_ZERO,
    ROUND,
    ROUND_DOWN,
    ROUND_UP,
    SIGNIFICANT_DIGITS,
    TICK_SIZE,
    TRUNCATE,
    decimal_to_precision,
)
from ccxt.base.errors import (
    AccountNotEnabled,
    AccountSuspended,
    AddressPending,
    ArgumentsRequired,
    AuthenticationError,
    BadRequest,
    BadResponse,
    BadSymbol,
    BaseError,
    CancelPending,
    ChecksumError,
    ContractUnavailable,
    DDoSProtection,
    DuplicateOrderId,
    ExchangeClosedByUser,
    ExchangeError,
    ExchangeNotAvailable,
    InsufficientFunds,
    InvalidAddress,
    InvalidNonce,
    InvalidOrder,
    InvalidProxySettings,
    ManualInteractionNeeded,
    MarginModeAlreadySet,
    MarketClosed,
    NetworkError,
    NoChange,
    NotSupported,
    NullResponse,
    OnMaintenance,
    OperationFailed,
    OperationRejected,
    OrderImmediatelyFillable,
    OrderNotCached,
    OrderNotFillable,
    OrderNotFound,
    PermissionDenied,
    RateLimitExceeded,
    RequestTimeout,
    UnsubscribeError,
    error_hierarchy,
)
from ccxt.base.exchange import Exchange
from ccxt.base.precise import Precise
from ccxt.bequant import bequant
from ccxt.bigone import bigone
from ccxt.binance import binance
from ccxt.binancecoinm import binancecoinm
from ccxt.binanceus import binanceus
from ccxt.binanceusdm import binanceusdm
from ccxt.bingx import bingx
from ccxt.bit2c import bit2c
from ccxt.bitbank import bitbank
from ccxt.bitbns import bitbns
from ccxt.bitcoincom import bitcoincom
from ccxt.bitfinex import bitfinex
from ccxt.bitfinex1 import bitfinex1
from ccxt.bitflyer import bitflyer
from ccxt.bitget import bitget
from ccxt.bithumb import bithumb
from ccxt.bitmart import bitmart
from ccxt.bitmex import bitmex
from ccxt.bitopro import bitopro
from ccxt.bitpanda import bitpanda
from ccxt.bitrue import bitrue
from ccxt.bitso import bitso
from ccxt.bitstamp import bitstamp
from ccxt.bitteam import bitteam
from ccxt.bitvavo import bitvavo
from ccxt.bl3p import bl3p
from ccxt.blockchaincom import blockchaincom
from ccxt.blofin import blofin
from ccxt.btcalpha import btcalpha
from ccxt.btcbox import btcbox
from ccxt.btcmarkets import btcmarkets
from ccxt.btcturk import btcturk
from ccxt.bybit import bybit
from ccxt.cex import cex
from ccxt.coinbase import coinbase
from ccxt.coinbaseadvanced import coinbaseadvanced
from ccxt.coinbaseexchange import coinbaseexchange
from ccxt.coinbaseinternational import coinbaseinternational
from ccxt.coincatch import coincatch
from ccxt.coincheck import coincheck
from ccxt.coinex import coinex
from ccxt.coinlist import coinlist
from ccxt.coinmate import coinmate
from ccxt.coinmetro import coinmetro
from ccxt.coinone import coinone
from ccxt.coinsph import coinsph
from ccxt.coinspot import coinspot
from ccxt.cryptocom import cryptocom
from ccxt.currencycom import currencycom
from ccxt.defx import defx
from ccxt.delta import delta
from ccxt.deribit import deribit
from ccxt.digifinex import digifinex
from ccxt.ellipx import ellipx
from ccxt.exmo import exmo
from ccxt.fmfwio import fmfwio
from ccxt.gate import gate
from ccxt.gateio import gateio
from ccxt.gemini import gemini
from ccxt.hashkey import hashkey
from ccxt.hitbtc import hitbtc
from ccxt.hollaex import hollaex
from ccxt.htx import htx
from ccxt.huobi import huobi
from ccxt.huobijp import huobijp
from ccxt.hyperliquid import hyperliquid
from ccxt.idex import idex
from ccxt.independentreserve import independentreserve
from ccxt.indodax import indodax
from ccxt.kraken import kraken
from ccxt.krakenfutures import krakenfutures
from ccxt.kucoin import kucoin
from ccxt.kucoinfutures import kucoinfutures
from ccxt.kuna import kuna
from ccxt.latoken import latoken
from ccxt.lbank import lbank
from ccxt.luno import luno
from ccxt.lykke import lykke
from ccxt.mercado import mercado
from ccxt.mexc import mexc
from ccxt.myokx import myokx
from ccxt.ndax import ndax
from ccxt.novadax import novadax
from ccxt.oceanex import oceanex
from ccxt.okcoin import okcoin
from ccxt.okx import okx
from ccxt.onetrading import onetrading
from ccxt.oxfun import oxfun
from ccxt.p2b import p2b
from ccxt.paradex import paradex
from ccxt.paymium import paymium
from ccxt.phemex import phemex
from ccxt.poloniex import poloniex
from ccxt.poloniexfutures import poloniexfutures
from ccxt.probit import probit
from ccxt.timex import timex
from ccxt.tokocrypto import tokocrypto
from ccxt.tradeogre import tradeogre
from ccxt.upbit import upbit
from ccxt.vertex import vertex
from ccxt.wavesexchange import wavesexchange
from ccxt.wazirx import wazirx
from ccxt.whitebit import whitebit
from ccxt.woo import woo
from ccxt.woofipro import woofipro
from ccxt.xt import xt
from ccxt.yobit import yobit
from ccxt.zaif import zaif
from ccxt.zonda import zonda

"""CCXT: CryptoCurrency eXchange Trading Library"""
__version__ = ...
exchanges = ...
base = ...
__all__ = base + errors.__all__ + exchanges
