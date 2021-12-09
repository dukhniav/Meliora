"""Types of run modes"""

from enum import Enum


class RunMode(Enum):
    """
    Bot running mode (backtest, hyperopt, ...)
    can be "live", "dry-run", "backtest", "edge", "hyperopt".
    """
    LIVE = "live"
    DRY_RUN = "dry_run"
    BACKTEST = "backtest"
    OTHER = "other"


REAL_MODES = [RunMode.LIVE, RunMode.DRY_RUN]
