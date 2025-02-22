import datetime
import threading
import time
from typing import Any, Dict, List

import plotext as plt


class CandlestickChart:
    def __init__(
        self, timeframe: str = "15m", max_candles: int = 50, refresh_rate: float = 1.0
    ) -> None:
        """
        Initializes the real-time candlestick chart.

        :param timeframe: The candle timeframe (e.g., "15m"). Currently supports minutes (e.g., "15m").
        :param max_candles: Maximum number of candles to display.
        :param refresh_rate: How frequently (in seconds) to update the chart.
        """
        self.refresh_rate: float = refresh_rate
        self.max_candles: int = max_candles
        self.candles: List[Dict[str, Any]] = []  # List of candle dictionaries
        self._lock: threading.Lock = threading.Lock()

        # Parse timeframe (assumes format like "15m")
        if timeframe.endswith("m"):
            self.timeframe_seconds: int = int(timeframe[:-1]) * 60
        else:
            raise ValueError("Unsupported timeframe format. Use minutes, e.g., '15m'.")

        # Start background thread for updating the chart
        self._stop_event: threading.Event = threading.Event()
        self._thread: threading.Thread = threading.Thread(
            target=self._refresh_loop, daemon=True
        )
        self._thread.start()

    def _get_candle_start(self, dt: datetime.datetime) -> datetime.datetime:
        """
        Given a datetime, compute the start time of the candle (flooring to the timeframe).
        """
        epoch: datetime.datetime = datetime.datetime(
            1970, 1, 1, tzinfo=datetime.timezone.utc
        )
        seconds: float = (dt - epoch).total_seconds()
        candle_start_seconds: float = seconds - (seconds % self.timeframe_seconds)
        return datetime.datetime.fromtimestamp(
            candle_start_seconds, tz=datetime.timezone.utc
        )

    def update_ohlcv(self, ohlcv: List[float]) -> None:
        """
        Updates the internal state with new OHLCV data.

        The expected format for ohlcv is:
          [timestamp, open, high, low, close, volume]
        where timestamp is in milliseconds.
        """
        # Convert timestamp to UTC datetime
        ts: float = ohlcv[0] / 1000.0
        dt: datetime.datetime = datetime.datetime.fromtimestamp(
            ts, tz=datetime.timezone.utc
        )
        candle_start: datetime.datetime = self._get_candle_start(dt)

        with self._lock:
            # If we already have a candle for this period, update it
            if self.candles and self.candles[-1]["timestamp"] == candle_start:
                current: Dict[str, Any] = self.candles[-1]
                current["high"] = max(current["high"], ohlcv[2])
                current["low"] = min(current["low"], ohlcv[3])
                current["close"] = ohlcv[4]
                current["volume"] += ohlcv[5]
            else:
                # Create a new candle
                new_candle: Dict[str, Any] = {
                    "timestamp": candle_start,
                    "open": ohlcv[1],
                    "high": ohlcv[2],
                    "low": ohlcv[3],
                    "close": ohlcv[4],
                    "volume": ohlcv[5],
                }
                self.candles.append(new_candle)
                # Keep only the most recent max_candles
                if len(self.candles) > self.max_candles:
                    self.candles.pop(0)

    def _refresh_loop(self) -> None:
        """
        Background loop that refreshes the chart.
        """
        while not self._stop_event.is_set():
            self._draw_chart()
            time.sleep(self.refresh_rate)

    def _draw_chart(self) -> None:
        with self._lock:
            if not self.candles:
                return

            # Convert timestamps to Unix time (seconds)
            timestamps: List[float] = [
                candle["timestamp"].timestamp() for candle in self.candles
            ]
            opens: List[float] = [candle["open"] for candle in self.candles]
            highs: List[float] = [candle["high"] for candle in self.candles]
            lows: List[float] = [candle["low"] for candle in self.candles]
            closes: List[float] = [candle["close"] for candle in self.candles]

        # Package the OHLC data into a dictionary as required by Plotext
        ohlc_data: Dict[str, List[float]] = {
            "Open": opens,
            "High": highs,
            "Low": lows,
            "Close": closes,
        }

        plt.clear_figure()  # type: ignore
        plt.date_form("unix")  # type: ignore
        plt.candlestick(timestamps, ohlc_data)  # type: ignore
        plt.title("Real-Time Candlestick Chart (15m) UTC")  # type: ignore
        plt.show()  # type: ignore
        plt.sleep(0.1)  # type: ignore

    def stop(self) -> None:
        """
        Stops the background refresh thread.
        """
        self._stop_event.set()
        self._thread.join()


# Example usage:
if __name__ == "__main__":
    import random

    chart = CandlestickChart(timeframe="15m", max_candles=20, refresh_rate=1.0)

    try:
        while True:
            # Simulate receiving OHLCV data.
            # In a real scenario, you would call chart.update_ohlcv(new_data)
            current_time_ms = int(time.time() * 1000)
            # Generate random values for demonstration
            ohlcv: list[float] = [
                current_time_ms,  # timestamp
                random.uniform(100, 110),  # open
                random.uniform(110, 120),  # high
                random.uniform(90, 100),  # low
                random.uniform(100, 110),  # close
                random.uniform(1000, 2000),  # volume
            ]
            chart.update_ohlcv(ohlcv)
            time.sleep(1)
    except KeyboardInterrupt:
        chart.stop()
