import asyncio
import logging
import os
from datetime import datetime, timedelta, timezone
from logging.handlers import RotatingFileHandler
from typing import Any, Dict, cast

import ccxt
import ccxt.async_support
import ccxt.async_support.okx
import ccxt.pro as ccxtpro
import yaml

###############################################################################
#                           CONFIG & GLOBALS
###############################################################################

API_KEY = os.getenv("OKX_API_KEY", "")
API_SECRET = os.getenv("OKX_API_SECRET", "")
API_PASSWORD = os.getenv("OKX_API_PASSWORD", "")

# We'll store open positions here (one position per symbol)
open_positions: Dict[str, Dict[str, Any]] = {}

# We’ll also store the *latest* funding rate info for each symbol
latest_funding_rates: Dict[str, Dict[str, Any]] = {}

# Default config file name
DEFAULT_CONFIG_FILE = "config.yaml"


###############################################################################
#                          CONFIG & LOGGING
###############################################################################


def load_config(config_file: str = DEFAULT_CONFIG_FILE) -> dict[str, Any]:
    try:
        with open(config_file, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Config file '{config_file}' not found. Using environment variables.")
        return {}


def setup_logger():
    logger = logging.getLogger("FundingRateArbitrage")
    logger.setLevel(logging.DEBUG)

    file_handler = RotatingFileHandler(
        "arbitrage.log", maxBytes=5 * 1024 * 1024, backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


logger = setup_logger()
config = load_config()

# Override with config/env if available
defaults: Dict[str, Any] = {
    "ORDER_FILL_TIMEOUT_SEC": 5,
    "MAX_RETRIES": 2,
    "SLIPPAGE_FACTOR": 0.0002,
    "MIN_ABS_FUNDING_RATE": 0.001,
    "STOP_LOSS_PERCENT": 2.0,
    "TRADE_AMOUNT_PERCENT": 1.0,
    "LEVERAGE_LIMIT": 10,
    "TOP_OPPORTUNITIES": 5,
    "CURRENCY": "USDT",
    "FUNDING_INTERVAL_HOURS": 8,
    "CHECK_INTERVAL": 10,
    "RANK_SIZE": 3,
    "TIME_TO_FUNDING_THRESHOLD": 5,
    "FETCH_BALANCE_MAX_RETRIES": 3,
}

# Load configuration from environment variables or use defaults
configurations = {
    key: type(defaults[key])(os.getenv(key, config.get(key, defaults[key])))
    for key in defaults
}

###############################################################################
#                          MAIN LOGIC
###############################################################################


async def funding_rate_arbitrage():
    """
    Main entry for the strategy:
      1) Initialize OKX ccxt.pro client
      2) Load markets
      3) Spawn tasks
         - 'collector' tasks: gather funding rates for each symbol
         - 'analyzer': ranks and decides which trades to open
         - 'manage_positions': handles lifecycle (close after funding, etc.)
    Includes improved error handling with retries and logging.
    """
    exchange: Any = ccxtpro.okx(  # type: ignore
        {
            "apiKey": API_KEY,
            "secret": API_SECRET,
            "password": API_PASSWORD,
            "enableRateLimit": True,
        }
    )

    try:
        # Attempt to load markets with some error handling
        try:
            await exchange.load_markets()
            logger.info("Markets loaded successfully.")
        except Exception as e:
            logger.exception(
                "Failed to load markets. Check API credentials or network."
            )
            return  # If we can't load markets, we cannot proceed

        # Filter only swap markets
        all_swap_markets = [
            m for m in exchange.markets if exchange.markets[m]["type"] == "swap"
        ]

        # Take top N or filter further by our logic
        selected_markets = all_swap_markets[: configurations["TOP_OPPORTUNITIES"]]
        logger.info(f"Selected swap markets: {selected_markets}")

        # Create tasks
        collector_tasks = [
            asyncio.create_task(funding_rate_collector(exchange, m))
            for m in selected_markets
        ]
        analyzer_task = asyncio.create_task(funding_rate_analyzer(exchange))
        manage_task = asyncio.create_task(manage_positions(exchange))

        # Run them concurrently
        await asyncio.gather(*collector_tasks, analyzer_task, manage_task)

    except Exception as e:
        logger.exception("Critical error in funding_rate_arbitrage loop:", exc_info=e)
    finally:
        await exchange.close()
        logger.info("Exchange connection closed.")


async def funding_rate_collector(exchange: ccxt.async_support.okx.okx, market: str):
    """
    Continuously collects the latest funding rate for a single market
    and stores it in 'latest_funding_rates'. We do NOT open positions here.
    Improved error handling: if watch_funding_rate fails repeatedly,
    we do a short sleep between attempts.
    """
    consecutive_errors = 0
    MAX_CONSECUTIVE_ERRORS = 10  # If we keep failing, eventually stop

    while True:
        try:
            fr_info = cast(
                "Dict[str, Any]",
                await exchange.watch_funding_rate(market),  # type: ignore
            )

            symbol = fr_info.get("symbol")
            if symbol is None:
                logger.warning(
                    f"Received funding rate info without a symbol: {fr_info}"
                )
                continue

            funding_rate = fr_info.get("fundingRate")
            mark_price = fr_info.get("markPrice")
            next_funding_time = fr_info.get("nextFundingTime", None)

            # Store the data
            latest_funding_rates[symbol] = {
                "symbol": symbol,
                "funding_rate": funding_rate,
                "mark_price": mark_price,
                "timestamp": datetime.now(timezone.utc),
                "next_funding_time": next_funding_time,
            }

            # Reset error counter on success
            consecutive_errors = 0

        except Exception as e:
            consecutive_errors += 1
            logger.exception(
                f"[{market}] watch_funding_rate error (#{consecutive_errors}): {e}"
            )
            if consecutive_errors >= MAX_CONSECUTIVE_ERRORS:
                logger.critical(
                    f"[{market}] Too many consecutive watch_funding_rate errors. Stopping collector task."
                )
                return  # We stop this task. Or we could break, or reconnect the exchange, etc.

            # Wait a bit before retrying
            await asyncio.sleep(5)


async def funding_rate_analyzer(exchange: Any):
    """
    Periodically checks the latest funding rates for all tracked symbols, ranks them,
    and decides which to open positions on. Enhanced logging & potential error checks.
    """
    while True:
        try:
            if not latest_funding_rates:
                logger.debug("[ANALYZER] No funding rates collected yet, waiting.")
                await asyncio.sleep(configurations["CHECK_INTERVAL"])
                continue

            rates_list = list(latest_funding_rates.values())
            # Filter out too-small rates
            candidates = [
                r
                for r in rates_list
                if abs(r["funding_rate"]) >= configurations["MIN_ABS_FUNDING_RATE"]
            ]

            if not candidates:
                logger.debug("[ANALYZER] No candidates meet MIN_ABS_FUNDING_RATE.")
                await asyncio.sleep(configurations["CHECK_INTERVAL"])
                continue

            # Sort by absolute funding rate, descending
            candidates.sort(key=lambda x: abs(x["funding_rate"]), reverse=True)
            # Take top RANK_SIZE
            top_candidates = candidates[: configurations["RANK_SIZE"]]

            logger.info(
                f"[ANALYZER] Top {len(top_candidates)} by abs(funding_rate): "
                f"{[(c['symbol'], c['funding_rate']) for c in top_candidates]}"
            )

            # For each candidate
            for info in top_candidates:
                symbol = info["symbol"]
                fr = info["funding_rate"]
                mark_price = info["mark_price"]
                nxt_ft = info.get("next_funding_time", None)

                # Optional: check if near next funding
                if nxt_ft:
                    nft_dt = parse_next_funding_time(nxt_ft)
                    now = datetime.now(timezone.utc)
                    if nft_dt > now:
                        minutes_to_funding = (nft_dt - now).total_seconds() / 60.0
                        logger.debug(
                            f"[ANALYZER] {symbol} is ~{minutes_to_funding:.1f} min to next funding."
                        )
                        if (
                            minutes_to_funding
                            > configurations["TIME_TO_FUNDING_THRESHOLD"]
                        ):
                            logger.debug(
                                f"[ANALYZER] {symbol} not within threshold; skipping."
                            )
                            continue

                # If FR > 0 => short, else long
                if fr > 0:
                    await try_open_position(exchange, symbol, "short", mark_price, fr)
                else:
                    await try_open_position(exchange, symbol, "long", mark_price, fr)

            await asyncio.sleep(configurations["CHECK_INTERVAL"])

        except Exception as e:
            logger.exception(f"[ANALYZER] Unexpected error: {e}")
            await asyncio.sleep(2)


def parse_next_funding_time(nft_data: Any) -> datetime:
    """
    Parse 'nextFundingTime' from the exchange data if it's an int/float or a string.
    """
    if isinstance(nft_data, (int, float)):
        if nft_data > 1e10:  # likely milliseconds
            nft_data /= 1000.0
        return datetime.fromtimestamp(nft_data, tz=timezone.utc)
    elif isinstance(nft_data, str):
        return datetime.fromisoformat(nft_data.replace("Z", "+00:00"))

    return datetime.now(timezone.utc) + timedelta(
        hours=configurations["FUNDING_INTERVAL_HOURS"]
    )


###############################################################################
#                     POSITION LIFECYCLE & RISK MANAGEMENT
###############################################################################


async def try_open_position(
    exchange: Any, symbol: str, direction: str, price: float, funding_rate: float
):
    """
    Attempts to open a new position if not already open. Includes better logging
    and a separate retry for fetching balances.
    """
    if symbol in open_positions:
        logger.debug(
            f"[try_open_position] Position already open for {symbol}; skipping."
        )
        return

    logger.info(
        f"[TRY_OPEN] {direction.upper()} on {symbol} @ price={price}, FR={funding_rate}"
    )

    try:
        free_balance = await robust_fetch_balance(exchange, configurations["CURRENCY"])
        if free_balance <= 0:
            logger.warning(
                f"[try_open_position] No free {configurations["CURRENCY"]} to open {symbol}."
            )
            return

        # Calculate trade size
        trade_amount = (configurations["TRADE_AMOUNT_PERCENT"] / 100.0) * free_balance
        trade_amount = round(trade_amount, 8)
        if trade_amount <= 0:
            logger.warning(
                f"[try_open_position] Calculated trade amount=0 for {symbol}; skipping."
            )
            return

        # Set leverage
        try:
            await exchange.set_leverage(configurations["LEVERAGE_LIMIT"], symbol)
            logger.info(
                f"[try_open_position] Set leverage={configurations["LEVERAGE_LIMIT"]} for {symbol}"
            )
        except Exception as e:
            logger.exception(f"Failed to set leverage for {symbol}: {e}")
            return

        side = "buy" if direction == "long" else "sell"
        if direction == "long":
            limit_price = price * (1 + configurations["SLIPPAGE_FACTOR"])
        else:
            limit_price = price * (1 - configurations["SLIPPAGE_FACTOR"])
        limit_price = float(f"{limit_price:.2f}")

        logger.info(
            f"[CREATE LIMIT] {symbol}, side={side}, amount={trade_amount}, limitPrice={limit_price}"
        )
        order = await exchange.create_limit_order(
            symbol, side, trade_amount, limit_price, params={"reduceOnly": False}
        )
        order_id = order["id"]

        filled_amount = 0.0
        start_time = datetime.now(timezone.utc)
        remaining_amount = trade_amount
        retries = 0

        while True:
            await asyncio.sleep(1)
            current_order = await exchange.fetch_order(order_id, symbol)
            status = current_order.get("status")
            filled = current_order.get("filled", 0.0)
            remaining = current_order.get("remaining", trade_amount - filled)

            logger.debug(
                f"[ORDER STATUS] {symbol}, ID={order_id}, status={status}, "
                f"filled={filled}, remaining={remaining}"
            )

            if status == "closed" or remaining <= 0:
                filled_amount = filled
                logger.info(
                    f"[ORDER FILLED] {symbol}, {order_id} fully filled => {filled_amount}"
                )
                break

            elapsed = (datetime.now(timezone.utc) - start_time).total_seconds()
            if elapsed > configurations["ORDER_FILL_TIMEOUT_SEC"]:
                retries += 1
                logger.info(
                    f"[ORDER TIMEOUT] {symbol}, {order_id} not filled in {configurations["ORDER_FILL_TIMEOUT_SEC"]}s. "
                    f"filled={filled}, remaining={remaining}, retry={retries}"
                )
                # Cancel + reprice or fallback
                if retries > configurations["MAX_RETRIES"]:
                    # fallback to market
                    await safe_cancel_order(exchange, symbol, order_id)
                    if remaining > 0:
                        logger.info(
                            f"[FALLBACK MARKET] for {symbol}, remaining={remaining}"
                        )
                        try:
                            fallback_order = await exchange.create_market_order(
                                symbol, side, remaining, params={"reduceOnly": False}
                            )

                            logger.debug(f"[FALLBACK MARKET ORDER] {fallback_order}")

                            filled_amount = filled + remaining
                            logger.info(
                                f"[MARKET FILL] {symbol}, filled remainder={remaining}"
                            )
                        except Exception as e:
                            logger.exception(
                                f"[MARKET FILL] Failed fallback for {symbol}: {e}"
                            )
                    break
                else:
                    # Cancel and re-price limit
                    await safe_cancel_order(exchange, symbol, order_id)
                    if direction == "long":
                        limit_price *= 1 + configurations["SLIPPAGE_FACTOR"]
                    else:
                        limit_price *= 1 - configurations["SLIPPAGE_FACTOR"]
                    limit_price = float(f"{limit_price:.2f}")

                    remaining_amount = remaining
                    try:
                        order = await exchange.create_limit_order(
                            symbol,
                            side,
                            remaining_amount,
                            limit_price,
                            params={"reduceOnly": False},
                        )
                        order_id = order["id"]
                        start_time = datetime.now(timezone.utc)
                        logger.info(
                            f"[REPRICE LIMIT] {symbol}, side={side}, newPrice={limit_price}"
                        )
                    except Exception as e:
                        logger.exception(f"[REPRICE LIMIT] Failed for {symbol}: {e}")
                        break  # break out and do not open a position

        if filled_amount <= 0:
            logger.warning(f"[NO FILLS] {symbol}, no position opened.")
            return

        # Place stop-loss
        stop_order_id = await place_stop_loss(
            exchange, symbol, direction, price, filled_amount
        )
        # Estimate next funding time
        next_funding_dt = datetime.now(timezone.utc) + timedelta(
            hours=configurations["FUNDING_INTERVAL_HOURS"]
        )

        open_positions[symbol] = {
            "symbol": symbol,
            "direction": direction,
            "size": filled_amount,
            "entry_price": limit_price,  # or an avg fill price if we have it
            "stop_loss": None,  # optional if we want to store the SL param
            "open_time": datetime.now(timezone.utc),
            "futures_order_id": order_id,
            "stop_order_id": stop_order_id,
            "funding_time": next_funding_dt,
        }
        logger.info(f"[POSITION OPENED] {open_positions[symbol]}")

    except Exception as e:
        logger.exception(f"[try_open_position] Unexpected error for {symbol}: {e}")


async def robust_fetch_balance(exchange: Any, currency: str) -> float:
    """
    Safely fetch the free balance for a given currency, with limited retries and logging.
    """
    attempts = 0
    while attempts < configurations["FETCH_BALANCE_MAX_RETRIES"]:
        try:
            balance = await exchange.fetch_balance()
            return balance["free"].get(currency, 0.0)
        except Exception as e:
            attempts += 1
            logger.exception(
                f"[robust_fetch_balance] Attempt #{attempts} failed for currency={currency}: {e}"
            )
            await asyncio.sleep(2 * attempts)  # exponential-ish backoff

    logger.error(
        f"[robust_fetch_balance] Exceeded {configurations["FETCH_BALANCE_MAX_RETRIES"]} attempts for {currency}. Returning 0."
    )
    return 0.0


async def place_stop_loss(
    exchange: Any, symbol: str, direction: str, entry_price: float, size: float
) -> str | None:
    """
    Attempt to place a stop-loss order. Returns the stop_order_id if successful, else None.
    Error handling with logs. Adjust param keys for OKX if needed.
    """
    try:
        if direction == "long":
            stop_loss_px = entry_price * (
                1 - configurations["STOP_LOSS_PERCENT"] / 100.0
            )
            stop_side = "sell"
        else:
            stop_loss_px = entry_price * (
                1 + configurations["STOP_LOSS_PERCENT"] / 100.0
            )
            stop_side = "buy"

        stop_loss_px = float(f"{stop_loss_px:.4f}")
        logger.info(
            f"[STOP LOSS] Creating SL for {symbol} at {stop_loss_px}, side={stop_side}, size={size}"
        )

        stop_order = await exchange.create_order(
            symbol,
            type="stopMarket",  # or "stopLoss" / "trigger" depending on OKX
            side=stop_side,
            amount=size,
            price=None,
            params={"stopLossPrice": stop_loss_px},
        )
        stop_order_id = stop_order.get("id")
        logger.info(f"[STOP LOSS] Created for {symbol}, ID={stop_order_id}")
        return stop_order_id
    except Exception as e:
        logger.exception(f"[STOP LOSS] Failed to place SL for {symbol}: {e}")
        return None


async def safe_cancel_order(exchange: Any, symbol: str, order_id: str):
    """
    Attempts to cancel an order, with logging. If it fails, we log the exception but continue.
    """
    try:
        logger.debug(f"[CANCEL ORDER] symbol={symbol}, order_id={order_id}")
        result = await exchange.cancel_order(order_id, symbol)
        logger.debug(f"[CANCEL ORDER] result={result}")
    except Exception as e:
        logger.exception(
            f"[CANCEL ORDER] Unable to cancel order {order_id} for {symbol}: {e}"
        )


###############################################################################
#                         POSITION MANAGEMENT TASK
###############################################################################


async def manage_positions(exchange: Any):
    """
    Periodic task that checks open positions, closes them after funding, etc.
    with improved logging and potential recovery from errors.
    """
    while True:
        try:
            # Convert to list(...) for safe iteration
            for sym in list(open_positions.keys()):
                pos = open_positions[sym]
                # If we've passed 'funding_time', close the position
                if datetime.now(timezone.utc) >= pos["funding_time"]:
                    logger.info(
                        f"[manage_positions] Funding time reached for {sym}. Closing position."
                    )
                    await close_position(exchange, sym)

        except Exception as e:
            logger.exception(f"[manage_positions] Unexpected error: {e}")

        await asyncio.sleep(5)


async def close_position(exchange: Any, symbol: str):
    """
    Closes an open position by placing a market order in the opposite direction.
    Removes it from open_positions. Logs success/failure.
    """
    if symbol not in open_positions:
        logger.warning(f"[close_position] No open position found for {symbol}.")
        return

    pos = open_positions[symbol]
    direction = pos["direction"]
    size = pos["size"]
    close_side = "sell" if direction == "long" else "buy"

    logger.info(f"[close_position] Closing {symbol}, side={close_side}, size={size}")

    try:
        close_order = await exchange.create_market_order(
            symbol, close_side, size, params={"reduceOnly": True}
        )
        logger.info(f"[close_position] Market close OK for {symbol}: {close_order}")
    except Exception as e:
        logger.exception(f"[close_position] Error closing position on {symbol}: {e}")
    finally:
        # Remove from dictionary in any case
        if symbol in open_positions:
            del open_positions[symbol]
            logger.info(f"[close_position] Removed {symbol} from open_positions.")


###############################################################################
#                               ENTRY POINT
###############################################################################

if __name__ == "__main__":
    asyncio.run(funding_rate_arbitrage())
