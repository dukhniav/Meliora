import unittest

from meliora.config.config import Configuration
from meliora.enums import RunMode
from meliora.worker import Meliora
from meliora.worker import Worker


class TestWorker(unittest.TestCase):
    def test_historic_file(self):
        """
        Test bot type
        """
        config = Configuration()
        worker = Worker(Meliora(RunMode.BACKTEST, config), RunMode.BACKTEST)
        historic_data_exists = worker.historic_data_exists("Binance US", "USDT", "BTC", "1h")
        self.assertTrue(historic_data_exists)


if __name__ == '__main__':
    unittest.main()
