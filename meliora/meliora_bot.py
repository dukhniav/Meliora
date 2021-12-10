# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring
"""
This class is the main bot and used to initialize all aspects of Meliora
"""
from logging import getLogger
from meliora.scheduler import SafeScheduler
from meliora.enums import RunMode
from meliora.config.config import Configuration

logger = getLogger(__name__)


class Meliora:
    def __init__(self, run_mode: RunMode, config: Configuration):
        self.config = config
        self.__init_modules()
        logger.info("Initial mode set to %s", run_mode)
        if run_mode == RunMode.DRY_RUN:
            self.init_dry_run()
        else:
            self.init_live_run()

    def __init_modules(self):  # pylint: disable=no-self-use
        """Initializing submodules"""
        logger.info("Initializing submodules")
        self.scheduler = SafeScheduler()

    def init_dry_run(self):  # pylint: disable=no-self-use
        """Initiating dry run"""
        logger.info("Starting bot in dry run mode")

    def init_live_run(self):  # pylint: disable=no-self-use
        """Initiating live mode"""
        logger.info("Starting bot in live mode")
