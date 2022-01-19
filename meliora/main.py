# pylint: disable=broad-except
# pylint: disable=wrong-import-position
# !/usr/bin/env python3
"""
Main Meliora bot script.
"""
import argparse
import logging
import sys
from typing import Any

from meliora import __name__, __version__  # pylint: disable=redefined-builtin
from meliora.config.config import Configuration
from meliora.enums import RunMode, State, Exchange
from meliora.loggers import setup_logging_pre
from meliora.worker import  Worker

logger = logging.getLogger(__name__)


parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version", action="version", version=f"{__name__}: {__version__}")
parser.add_argument("-l", "--live", action="store_true", help="run bot in live mode")
parser.add_argument("-b", "--backtest", action="store_true", help="run bot in backtest mode")
parser.add_argument('files', nargs='*')
parser.add_argument("--e",  help="specify exchange for historical data", default=Exchange.BINANCEUS)
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()


# noinspection PyBroadException
def main() -> None:  # pylint: disable=too-many-branches
    """
    This function will initiate the bot
    :return: None
    """
    return_code: Any = 1

    try:
        setup_logging_pre()
        config = Configuration()
        # balancer.run()
        worker = Worker(config)


    except SystemExit as exception:  # pragma: no cover
        return_code = exception
    except KeyboardInterrupt:
        logger.info('SIGINT received, aborting ...')
        return_code = 0
    # except MelioraException as exception:
    #     logger.error(str(exception))
    #     return_code = 2
    except Exception:
        logger.exception('Fatal exception!')
    finally:
        sys.exit(return_code)


if __name__ == '__main__':  # pragma: no cover
    main()