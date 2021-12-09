# pylint: disable=broad-except
# pylint: disable=wrong-import-position
#!/usr/bin/env python3
"""
Main Meliora bot script.
Read the documentation to know what cli arguments you need.
"""
import logging
import sys
import argparse
from typing import Any
from time import sleep
from meliora.backtest import Backtest
from meliora.utils.exceptions import MelioraException
from meliora.utils.loggers import setup_logging_pre
from meliora.enums import RunMode, State
from meliora.meliora_bot import Meliora
from meliora.config.config import Configuration
from meliora.worker import Worker
from meliora import __name__, __version__ #pylint: disable=redefined-builtin

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version", action="version",
                    version=f"{__name__}: {__version__}")
parser.add_argument("-m", "--mode", help="meliora runmode",
                    default=RunMode.DRY_RUN)
parser.add_argument('files', nargs='*')
parser.add_argument("-e", "--exchange",
                    help="specify exchange for historical data", default="binanceus")
parser.add_argument(
    "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()


def main() -> None: # pylint: disable=too-many-branches
    """
    This function will initiate the bot and start the trading loop.
    :return: None
    """
    return_code: Any = 1

    try:
        setup_logging_pre()
        run_mode = args.mode
        config = Configuration()
        state = State.NEW

        while state is not State.EXIT:
            if state == State.STOP:
                logger.info("Meliora bot is stopped")
                sleep(60)
            elif state == State.RELOAD:
                logger.info("Reloading config")
                config = Configuration()
                state = State.NEW
            elif state == State.NEW:
                if run_mode == RunMode.BACKTEST:
                    bot = Backtest(config)
                else:
                    bot = Meliora(run_mode, config)
                worker = get_worker(bot)
                state = State.RUN
            else:
                worker.run()
            sleep(1)
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


def get_worker(bot):
    """Get worker object"""
    return Worker(bot)


if __name__ == '__main__':  # pragma: no cover
    main()
