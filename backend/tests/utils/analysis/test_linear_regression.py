import numpy as np
import unittest

from utils.analysis.linear_regression import FinanceLinearRegressionModel


class TestFinanceLinearRegressionModel(unittest.TestCase):

    def setUp(self):
        self.test_model = FinanceLinearRegressionModel()

    def test_fit(self):
        x = np.array([1, 2, 3, 4])
        y = np.array([1, 2, 3, 4])
        result = self.test_model.fit(x, y)

        self.assertIsNotNone(result)
        self.assertEqual(result.intercept_, 0.0)
        self.assertEqual(result.coef_, 1.0)

