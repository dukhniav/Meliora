# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring
"""
This class is used to control main aspects of Meliora bot
"""
from logging import getLogger
from schedule import Scheduler

logger = getLogger(__name__)


class Worker:
    """
    This class is used to control main aspects of Meliora bot
    """
    def __init__(self, bot):
        self.bot = bot
        self.config = self.bot.config
        self.scheduler: Scheduler = bot.scheduler

    def msg_run(self): # pylint: disable=no-self-use
        """Running message"""
        logger.warning("Meliora bot is running")

    def msg_stop(self): # pylint: disable=no-self-use
        """Stopped message"""
        logger.warning("Meliora bot is stopped")

    def run(self): # pylint: disable=no-self-use
        """Perform all bot functions"""
        logger.info("Running worker")
