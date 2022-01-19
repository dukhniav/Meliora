# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name
"""
This module contains the configuration class
"""
import logging
import json

from meliora.enums import RunMode, State, Exchange, Fiat
from meliora.config import constants

logger = logging.getLogger(__name__)


class Configuration:
    """
    Class to read and init the bot configuration
    Reuse this class for the bot, backtesting, hyperopt and every script that required configuration
    """

    def __init__(self):
        with open(constants.CREDENTIALS_PATH, "r") as jsonfile:
            self.credentials = json.load(jsonfile)

        with open(constants.CONFIG_PATH, "r") as jsonfile:
            self.config = json.load(jsonfile)

        with open(constants.WALLETS_PATH, "r") as jsonfile:
            self.wallets = json.load(jsonfile)

        # Credentials
        self.BSC_API_KEY = self.credentials['bscscan']['api_key']

        # Testing
        self.BSC_ADDRESS = self.credentials['testing']['test_bsc_address']

        # Base config
        self.DEFAULT_MODE = self.config['base']['init_run_mode'] or RunMode.DRY_RUN
        self.DEFAULT_STATE = self.config['base']['init_state'] or State.RUNNING
        self.DEFAULT_EXCHANGE = self.config['base']['default_exchange'] or Exchange.BINANCEUS
        self.DEFAULT_FIAT = self.config['base']['default_fiat'] or Fiat.USDT
        self.DEFAULT_TIMEFRAME = self.config['base']['default_timeframe'] or '1h'
        self.NOTIFICATIONS = True if self.config['base']['notifications'] == "True" else False

        # Default functionality
        self.HEARTBEAT_INTERVAL = 3600  # seconds (1 hour)
        self.BOT_SLEEP_TIME = 1  # seconds

        # Explorer APIs
        self.ETHER_API = self.credentials['api_keys']['etherscan']
        self.BSC_API = self.credentials['api_keys']['bscscan']

        self.PORTFOLIOS = {}
        self.WALLETS = {}
        for p in self.wallets.items():
            # Portfolios
            for w in p[1].get('wallets'):
                if p[1].get('name') in self.PORTFOLIOS:
                    self.PORTFOLIOS.get(p[1].get('name')).append(p[1].get('wallets').get(w).get('name'))
                else:
                    self.PORTFOLIOS[p[1].get('name')] = [p[1].get('wallets').get(w).get('name')]
                # Wallets
                if p[1].get('wallets').get(w).get('name') in self.WALLETS:
                    self.WALLETS.get(p[1].get('wallets').get(w).get('name')).append(p[1].get('wallets').get(w).get('addr'))
                else:
                    self.WALLETS[p[1].get('wallets').get(w).get('name')] = [p[1].get('wallets').get(w).get('addr')]
