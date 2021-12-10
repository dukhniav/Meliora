# pylint: disable=too-few-public-methods
"""
Will transform into a class for backtesting
"""
from logging import getLogger

import ccxt
import pandas as pd
from ccxt import binanceus
from meliora.config.config import Configuration
from meliora.enums import Chain, Exchange, Fiat, RunMode
from meliora.config.config import Configuration
from meliora.utils.exceptions import ExchangeError

from meliora.meliora_bot import Meliora
from meliora.scheduler import SafeScheduler
from meliora.config import constants
from meliora.persistance.database import Database

logger = getLogger(__name__)


class Backtest:
    """
    Class to perform backtesting functionality
    """
    def __init__(self, run_mode: RunMode, config: Configuration):
        logger.info("Starting bot in backtest mode")
        self.config = config
        self.run_mode = run_mode
        self.__init_modules()
        self.db = self.init_db()

    def init_db(self):
        db_path = ""
        match self.run_mode:
            case RunMode.DRY_RUN:
                db_path = constants.DRY_DB_PATH
            case RunMode.LIVE:
                db_path = constants.LIVE_DB_PATH
            case _:
                db_path = constants.TESTING_DB_PATH
        return Database(db_path)

    def __init_modules(self):  # pylint: disable=no-self-use
        """Initializing submodules"""
        logger.info("Initializing submodules")
        self.scheduler = SafeScheduler()

    def fetch_historical_data(self, exchange: Exchange, target: str, fiat: Fiat, timeframe: str):  # pylint: disable=no-self-use
        """
        Method to retrieve historical data
        """
        if exchange.upper() == Exchange.BINANCEUS.name:
            exchange = binanceus()

            try:
                trading_pair = target + '/' + fiat
                data = exchange.fetch_ohlcv(trading_pair, timeframe)
                # Get data
                header = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
                dataframe = pd.DataFrame(data, columns=header).set_index('Timestamp')
                logger.info(f"Downloaded {trading_pair} - 1h - {data.__sizeof__()} kB")
                filename = './data/historical_data/{}-{}-{}-{}.csv'.format(exchange, target, fiat, timeframe)
                dataframe.to_csv(filename)
            except ccxt.BadSymbol:
                pass
        else:
            logger.warning(f"{exchange} not yet implemented")
