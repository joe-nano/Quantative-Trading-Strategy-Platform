import unittest
from strategies.backtest import Backtest
from strategies.pairs_trading import PairsTrading


class TestBacktest(unittest.TestCase):
    def setUp(self):
        self.company1 = 'AAPL'
        self.company2 = 'MSFT'
        self.start = '2020/01/01'
        self.end = '2020/06/30'
        self.pair_trader = PairsTrading(self.company1, self.company2, self.start, self.end)

    def test_init(self):
        self.assertIsNotNone(Backtest(self.pair_trader))

    def test_perform_bactest(self):
        backtest = Backtest(self.pair_trader)
        backtest.perform_backtest()
        self.assertNotEqual(0, backtest.pos)
        self.assertNotEqual(0, len(backtest.get_daily_pnl()))
        self.assertNotEqual(0, len(backtest.get_cumulative_pnl()))
        self.assertNotEqual(0, len(backtest.get_profit_per_trade()))
        self.assertNotEqual(0, len(backtest.calculate_portfolio_size()))
        self.assertNotEqual(0, len(backtest.get_cumulative_profit_per_trade()))
