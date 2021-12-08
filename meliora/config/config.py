"""
This module contains the configuration class
"""
import logging
import json

from meliora import constants
from meliora.enums import REAL_MODES, RunMode
from meliora.utils.exceptions import OperationalException

logger = logging.getLogger(__name__)
CREDENTIALS_PATH = './data/credentials.json'
CONFIG_PATH = './data/config.json'


class Configuration:
    """
    Class to read and init the bot configuration
    Reuse this class for the bot, backtesting, hyperopt and every script that required configuration
    """
    def __init__(self):
        with open(CREDENTIALS_PATH, "r") as jsonfile:
            self.credentials = json.load(jsonfile)

        with open(CONFIG_PATH, "r") as jsonfile:
            self.config = json.load(jsonfile)

        self.bsc_api = self.credentials['bscscan']['api_key']

        # Testing
        self.bsc_address = self.config['testing']['test_bsc_address']


