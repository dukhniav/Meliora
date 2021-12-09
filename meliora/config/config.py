# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name
"""
This module contains the configuration class
"""
import logging
import json

logger = logging.getLogger(__name__)
CREDENTIALS_PATH = './config/credentials.json'
CONFIG_PATH = './config/config.json'


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

        self.BSC_API_KEY = self.credentials['bscscan']['api_key']

        # Testing
        self.BSC_ADDRESS = self.credentials['testing']['test_bsc_address']

        # Base config
        self.INIT_MODE = self.config['base']['init_run_mode']
        self.INIT_STATE = self.config['base']['init_state']
