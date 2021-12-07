from meliora.enums.mode import RunMode
from meliora.persistance.models import Coin
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
parser.add_argument("-e", "--exchange", help="specify exchange for historical data", default="binanceus")
parser.add_argument(
    "--verbose", help="increase output verbosity",
    action="store_true")
args = parser.parse_args()


def main() -> None:
    args = parser.parse_args()

    run_mode =  RunMode.BACKTEST
    if args.live:
        run_mode = RunMode.LIVE

    if run_mode.BACKTEST:
        print("runmode=backtest")
        x = fetch_historical_data("binanceus","LTC","USD")

    # if not args.files:
    #     output_sha1sum(process_stdin())
    # for file in args.files:
    #     if file == "-":
    #         output_sha1sum(process_stdin(), "-")
    #         continue
    #     try:
    #         output_sha1sum(process_file(file), file)
    #     except (FileNotFoundError, IsADirectoryError) as err:
    #         print(f"{sys.argv[0]}: {file}: {err.strerror}", file=sys.stderr)

    print("sup foo")


def less_than(a, b):
    if a < b:
        return True
    return False

    # coin = Coin(
    #     symbol="shib",
    #     price=0.223
    # )

    # session.add(coin)  # Add the user
    # session.commit()  # Commit the change
    # print("works??!?!?!??")
