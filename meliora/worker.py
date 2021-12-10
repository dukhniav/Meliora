# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring
"""
This class is used to control main aspects of Meliora bot
"""
from logging import getLogger
from schedule import Scheduler
from meliora.enums import RunMode
from meliora.config import constants
from meliora.persistance import models
from meliora.backtest import Backtest
from meliora.meliora_bot import Meliora

logger = getLogger(__name__)


class Worker:
    """
    This class is used to control main aspects of Meliora bot
    """

    def __init__(self, bot, run_mode: RunMode):
        if type(bot) is Backtest:
            self.bot: Backtest = bot
        else:
            self.bot: Meliora = bot
        logger.debug(f"Worker utilizing {type(bot)} class")
        self.run_mode = run_mode
        self.config = self.bot.config
        self.scheduler: Scheduler = bot.scheduler

        models.init_db(run_mode)
        # run bot
        self.run_backtest() if run_mode == RunMode.BACKTEST else self.run()

    def msg_run(self):  # pylint: disable=no-self-use
        """Running message"""
        logger.warning("Meliora bot is running")

    def msg_stop(self):  # pylint: disable=no-self-use
        """Stopped message"""
        logger.warning("Meliora bot is stopped")

    def run(self):  # pylint: disable=no-self-use
        """Perform all bot functions"""
        # logger.info("Running worker")

    def run_backtest(self):  # pylint: disable=no-self-use
        """Perform backtesting functions"""
        # self.coins =
        with open(constants.COIN_LIST) as file:
            for coin in file:
                if '\n' in coin:
                    coin = coin[0:len(coin) - 1]
                self.download_historical_data(coin)
        # TODO: load data back from files
        # TODO: process data
        # TODO: display results

    def download_historical_data(self, symbol: str):
        """Used to fetch coin data"""
        bot: Backtest = self.bot
        exchange = self.config.DEFAULT_EXCHANGE
        fiat = self.config.DEFAULT_FIAT
        timeframe = self.config.DEFAULT_TIMEFRAME
        bot.fetch_historical_data(exchange, symbol, fiat, timeframe)
