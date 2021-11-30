from enum import Enum


class Payment(Enum):
    """
    Bot running mode (backtest ...)
    can be "live", "backtest"
    """
    LIVE = "live"
    BACKTEST = "backtest"
    OTHER = "other"
