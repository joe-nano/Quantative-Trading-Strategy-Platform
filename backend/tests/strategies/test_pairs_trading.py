import unittest

from strategies.pairs_trading import PairsTrading


class TestPairsTrading(unittest.TestCase):
    def setUp(self):
        self.company1 = 'AAPL'
        self.company2 = 'MSFT'
        self.start = '2020/01/01'
        self.end = '2020/06/30'
        self.pairs_trader = PairsTrading(self.company1, self.company2, self.start, self.end)

    def test_perform_linear_regression(self):
        self.assertIsNotNone(self.pairs_trader.perform_linear_regression())

    def test_calculate_spread_from_scratch(self):
        self.assertIsNotNone(self.pairs_trader.calculate_spread())

    def test_calculate_spread_with_previous_result(self):
        self.pairs_trader.perform_linear_regression()
        self.assertIsNotNone(self.pairs_trader.calculate_spread())

    def test_generate_threshold(self):
        self.assertIsNotNone(self.pairs_trader.generate_threshold())

    def test_get_portfolio_size(self):
        self.assertIsNotNone(self.pairs_trader.get_portfolio_size())
