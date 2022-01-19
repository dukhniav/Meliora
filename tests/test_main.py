# import unittest
#
# from meliora.worker import Worker
# from meliora.worker import Meliora
# from meliora.backtest import Backtest
# from meliora.enums import RunMode
# from meliora.main import get_worker
# from meliora.config.config import Configuration
#
#
# class TestGetWorker(unittest.TestCase):
#     def test_backtest(self):
#         """
#         Test bot type
#         """
#         self.assertTrue(type(get_worker(Worker(Backtest(RunMode.BACKTEST, Configuration()), RunMode.BACKTEST),RunMode.BACKTEST)) == Backtest)
#
#
#     def test_meliora(self):
#         """
#         Test that it can sum a list of integers
#         """
#         self.assertTrue(type(get_worker(Worker(Meliora(RunMode.DRY_RUN, Configuration()), RunMode.DRY_RUN),RunMode.DRY_RUN)) == Meliora)
#
#
# if __name__ == '__main__':
#     unittest.main()
