# pylint: disable=broad-except
# pylint: disable=wrong-import-position
# !/usr/bin/env python3
"""
Main Meliora bot script.
Read the documentation to know what cli arguments you need.
"""
import argparse
import logging
import sys
import time
from os import getpid
from time import sleep
from typing import Any

from meliora import __name__, __version__  # pylint: disable=redefined-builtin
from meliora.backtest import Backtest
from meliora.config.config import Configuration
from meliora.enums import RunMode, State, Exchange
from meliora.meliora_bot import Meliora
from meliora.utils.exceptions import MelioraException
from meliora.utils.loggers import setup_logging_pre
from meliora.worker import Worker

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
    This function will initiate the bot and start the trading loop.
    :return: None
    """
    return_code: Any = 1

    try:
        setup_logging_pre()
        config = Configuration()
        run_mode = RunMode.LIVE if args.live else RunMode.BACKTEST if args.backtest else config.DEFAULT_MODE
        if args.verbose:
            logger.setLevel(2)

        state = State.NEW
        _heartbeat_interval = config.HEARTBEAT_INTERVAL
        _heartbeat_msg = 0

        while state is not State.EXIT:
            if state == State.STOPPED:
                logger.info("Meliora bot is stopped")
                sleep(60)
            elif state == State.RELOAD:
                logger.info("Reloading config")
                config = Configuration()
                state = State.NEW
            elif state == State.NEW:
                if run_mode == RunMode.BACKTEST:
                    bot = Backtest(run_mode, config)
                else:
                    bot = Meliora(run_mode, config)
                worker = get_worker(bot, run_mode)
                state = config.DEFAULT_STATE
            else:
                worker.run()
                if _heartbeat_interval:
                    now = time.time()
                    if (now - _heartbeat_msg) > _heartbeat_interval:
                        logger.info(
                            f"Bot heartbeat. PID={getpid()}, "
                            f"version='{__version__}', state='{state}'"
                        )
                        _heartbeat_msg = now
                worker.scheduler.run_pending()
                time.sleep(config.BOT_SLEEP_TIME)
    except SystemExit as exception:  # pragma: no cover
        return_code = exception
    except KeyboardInterrupt:
        logger.info('SIGINT received, aborting ...')
        return_code = 0
    except MelioraException as exception:
        logger.error(str(exception))
        return_code = 2
    except Exception:
        logger.exception('Fatal exception!')
    finally:
        sys.exit(return_code)


def get_worker(bot, run_mode):
    """Get worker object"""
    return Worker(bot, run_mode)


if __name__ == '__main__':  # pragma: no cover
    main()

