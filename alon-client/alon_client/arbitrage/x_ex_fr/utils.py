import asyncio
from dataclasses import dataclass
from datetime import datetime, timezone

from ccxt.base.exchange import Exchange

from alon_client.arbitrage.x_ex_fr.config import configurations
from alon_client.arbitrage.x_ex_fr.logger import logger


@dataclass
class Position:
    symbol: str
    direction: str
    size: float
    funding_time: str


open_positions: dict[str, Position] = {}


async def robust_fetch_balance(exchange: Exchange) -> float:
    """
    Fetches the free balance for USDT with retry logic.
    """
    attempts = 0
    while attempts < configurations["FETCH_BALANCE_MAX_RETRIES"]:
        try:
            balance = await exchange.fetch_balance()  # type: ignore
            return balance["free"].get(configurations["CURRENCY"], 0.0)  # type: ignore
        except Exception as e:
            logger.error(f"[robust_fetch_balance] Error fetching balance: {e}")
            attempts += 1
            await asyncio.sleep(2**attempts)
    return 0.0


async def try_open_position(exchange: Exchange, symbol: str, direction: str) -> None:
    """
    Opens a position using a market order.
    """
    if symbol in open_positions:
        logger.info(f"[{symbol}] Position already open. Skipping...")
        return

    try:
        free_balance = await robust_fetch_balance(exchange)
        trade_amount: float = (
            configurations["TRADE_AMOUNT_PERCENT"] / 100.0
        ) * free_balance

        if trade_amount <= 0:
            logger.error(f"[{symbol}] Insufficient balance to open a position.")
            return

        side = "buy" if direction == "long" else "sell"
        await exchange.create_market_order(  # type: ignore
            symbol, side, trade_amount, params={"reduceOnly": False}
        )

        open_positions[symbol] = Position(
            symbol=symbol,
            direction=direction,
            size=trade_amount,
            funding_time=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        )

        logger.info(
            f"[{symbol}] Opened {direction.upper()} position of {trade_amount}."
        )

    except Exception as e:
        logger.exception(f"[{symbol}] Error opening position: {e}")


async def close_position(exchange: Exchange, symbol: str) -> None:
    """
    Closes an open position with a market order.
    """
    if symbol not in open_positions:
        logger.info(f"[{symbol}] No open position to close.")
        return

    try:
        position = open_positions[symbol]
        side = "sell" if position.direction == "long" else "buy"

        await exchange.create_market_order(  # type: ignore
            symbol, side, position.size, params={"reduceOnly": True}
        )

        del open_positions[symbol]
        logger.info(f"[{symbol}] Position closed.")

    except Exception as e:
        logger.exception(f"[{symbol}] Error closing position: {e}")
