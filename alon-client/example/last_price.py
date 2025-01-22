import asyncio
import json
import logging
from enum import Enum
from typing import Callable, Optional, TypedDict

import okx.Account as Account
from okx.websocket.WsPublicAsync import WsPublicAsync

# Initialize API credentials
API_KEY = ""
SECRET_KEY = ""
PASSPHRASE = ""
IS_TESTNET = True  # Use True for demo, False for live trading

# Instantiate the Trade client
account_api = Account.AccountAPI(API_KEY, SECRET_KEY, PASSPHRASE, flag="0")

# WebSocket URL
WS_URL = "wss://ws.okx.com:8443/ws/v5/public"

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)

log = logging.getLogger(__name__)


# Place both long and short market orders
# def execute_market_orders(inst_id: str, qty: float):
#     try:
#         # Place a long (buy) market order
#         long_order = account_api.place_order(
#             instId=inst_id, tdMode="isolated", side="buy", ordType="market", sz=str(qty)
#         )
#         log.info("Long Order Response: %s", long_order)

#         # Place a short (sell) market order
#         short_order = account_api.place_order(
#             instId=inst_id,
#             tdMode="isolated",
#             side="sell",
#             ordType="market",
#             sz=str(qty),
#         )
#         log.info("Short Order Response: %s", short_order)
#     except Exception as e:
#         log.error("Error placing orders: %s", e)


class ArgData(TypedDict):
    channel: str
    instId: str


class TickerEntry(TypedDict):
    instType: str
    instId: str
    last: str
    lastSz: str
    askPx: str
    askSz: str
    bidPx: str
    bidSz: str
    open24h: str
    high24h: str
    low24h: str
    sodUtc0: str
    sodUtc8: str
    volCcy24h: str
    vol24h: str
    ts: str


class TickerData(TypedDict):
    arg: ArgData
    data: list[TickerEntry]


def parse_last_price(data: TickerData) -> Optional[float]:
    try:
        return float(data["data"][0]["last"])
    except (KeyError, IndexError, ValueError) as e:
        log.error(f"Error parsing last price: {e}")
        return None


# WebSocket listener
def on_message(message: str, inst_id: str):
    data = json.loads(message)
    last_price = parse_last_price(data)

    log.info("\033[H\033[J%s: %s", inst_id, last_price)


# lambda message: on_message(message, inst_id)
callback: Callable[[str, str], None] = lambda message, inst_id: on_message(
    message, inst_id
)


async def websocket_listener(inst_id: str):
    ws = WsPublicAsync(WS_URL)
    args: list[dict[str, str]] = [{"channel": "tickers", "instId": inst_id}]

    # Define the callback with a closure to include `inst_id`
    def callback(message: str):
        on_message(message, inst_id)

    await ws.start()  # type: ignore # Start the WebSocket connection
    await ws.subscribe(args, callback)  # type: ignore # Subscribe with the corrected callback

    try:
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        await ws.unsubscribe(args)  # type: ignore # Unsubscribe when stopping the listener


def set_leverage(inst_id: str, leverage: int):
    try:
        account_api.set_leverage(  # type: ignore
            instId=inst_id, lever=leverage, mgnMode="cross"
        )

        log.info("Leverage set to %s for %s", leverage, inst_id)
    except Exception as e:
        log.error("Error setting leverage: %s", e)


class PositionMode(Enum):
    LONG_SHORT_MODE = "long_short_mode"
    NET_MODE = "net_mode"


def set_position_mode(pos_mode: PositionMode = PositionMode.LONG_SHORT_MODE):
    try:
        account_api.set_position_mode(posMode=pos_mode.value)  # type: ignore

        log.info("Position mode set to %s", pos_mode.value)
    except Exception as e:
        log.error("Error setting position mode: %s", e)


async def main():
    instrument_id = "ZEREBRO-USDT-SWAP"
    leverage = 20

    # Set leverage
    set_leverage(instrument_id, leverage)

    # Set position mode
    set_position_mode(PositionMode.LONG_SHORT_MODE)

    await websocket_listener(instrument_id)


if __name__ == "__main__":
    asyncio.run(main())
