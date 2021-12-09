"""Types of timeframes"""
from enum import Enum


class Timeframe(Enum):
    """
    Bot running mode (backtest ...)
    can be "live", "backtest"
    """
    LIVE = "live"
    BACKTEST = "backtest"
    OTHER = "other"
