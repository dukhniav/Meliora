# pylint: disable=too-few-public-methods
"""
Will transform into a class for backtesting
"""
from logging import getLogger
import pandas as pd
from ccxt import binanceus
from meliora.config.config import Configuration

logger = getLogger(__name__)


class Backtest:
    """
    Class to perform backtesting functionality
    """

    def __init__(self, config: Configuration):
        self.config = config
        logger.info("Running in backtest mode...")

    def fetch_historical_data(self, exchange: str, target: str, fiat: str):  # pylint: disable=no-self-use
        """Method to retrieve historical data"""
        if exchange == 'binanceus':
            exchange = binanceus()

            trading_pair = target + '/' + fiat
            data = exchange.fetch_ohlcv(trading_pair, '1h')

            # Get data
            header = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
            dataframe = pd.DataFrame(
                data, columns=header).set_index('Timestamp')
            print(f"Downloaded {trading_pair} - 1h")
            filename = './data/historical_data/{}-{}-{}.csv'.format(
                exchange, target, "1h")
            dataframe.to_csv(filename)
