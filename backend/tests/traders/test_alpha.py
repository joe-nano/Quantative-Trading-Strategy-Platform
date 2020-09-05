import unittest
import numpy as np
import pytest

from traders.alpha.alpha import TraderAlpha


class TestTraderAlpha(unittest.TestCase):
    def setUp(self):
        self.companies = ['AAPL', 'AMZN']

    def test_init(self):
        self.assertIsNotNone(TraderAlpha(self.companies))

    def test_compute_correlation_pairs_for_trading_strategy(self):
        trader = TraderAlpha(self.companies)
        trader.correlation_threshold = 0
        self.assertEqual(1, len(trader.compute_correlation_pairs_for_trading_strategy()))

    def test_set_benchmark(self):
        trader = TraderAlpha(self.companies)
        trader.set_benchmark()
        old_benchmark = trader.benchmark_returns
        trader.set_benchmark('MSFT')

        self.assertFalse((old_benchmark == trader.benchmark_returns).all())

    def test_calculate_sharpe_ratio(self):
        daily_returns = np.array([1, 1, 1, 1, 2])
        result = TraderAlpha.calculate_sharpe_ratio(daily_returns)
        self.assertTrue(result > 0)

    def test_calculate_shortino_ratio(self):
        daily_returns = np.array([1, -11, 10, -1, 2])
        result = TraderAlpha.calculate_shortino_ratio(daily_returns)
        self.assertTrue(result > 0)

    def test_calculate_shortino_ratio_no_negative_return(self):
        daily_returns = np.array([1, 11, 10, 1, 2])
        result = TraderAlpha.calculate_shortino_ratio(daily_returns)
        self.assertEqual(0, result)

    def test_calculate_VaR(self):
        daily_returns = np.array([1, 1, 1, 1, 2, 10, 100])
        result = TraderAlpha.calculate_VaR(5000, 0.95, 2, daily_returns)
        self.assertTrue(result > 0)

    def test_calculate_VaR_invalid_confidence_interval(self):
        daily_returns = np.array([1, 1, 1, 1, 2, 10, 100])
        with pytest.raises(ValueError):
            TraderAlpha.calculate_VaR(5000, 110, 2, daily_returns)
