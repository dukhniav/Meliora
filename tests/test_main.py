import unittest

from meliora.main import less_than


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        self.assertTrue(less_than(1,2))


if __name__ == '__main__':
    unittest.main()
