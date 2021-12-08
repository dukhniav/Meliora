from datetime import datetime
from meliora.enums.mode import RunMode
from meliora.persistance.database import session
from meliora.backtest import fetch_historical_data

from meliora import __version__, __name__

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-V", "--version", action="version",
    version=f"{__name__}: {__version__}"
)
parser.add_argument(
    "-l", "--live", help="run meliora live, default=Backtest", action="store_true", default=RunMode.BACKTEST
)
parser.add_argument('files', nargs='*')
parser.add_argument("-e", "--exchange",
                    help="specify exchange for historical data", default="binanceus")
parser.add_argument(
    "--verbose", help="increase output verbosity",
    action="store_true")
args = parser.parse_args()


def main() -> None:
    args = parser.parse_args()

    run_mode = RunMode.BACKTEST
    if args.live:
        run_mode = RunMode.LIVE

    if run_mode.BACKTEST:
        print("runmode=backtest")
        x = fetch_historical_data("binanceus", "LTC", "USD")
