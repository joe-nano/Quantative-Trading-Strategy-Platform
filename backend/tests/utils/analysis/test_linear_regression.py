import numpy as np
import unittest

from utils.analysis.linear_regression import FinanceLinearRegressionModel


class TestFinanceLinearRegressionModel(unittest.TestCase):

    def setUp(self):
        self.test_model = FinanceLinearRegressionModel()

    def test_fit(self):
        x = np.array([1, 2, 3, 4])
        y = np.array([1, 2, 3, 4])
        self.test_model.fit(x, y)

        self.assertIsNotNone(self.test_model)
        self.assertEqual(self.test_model.get_intercept(), 0.0)
        self.assertEqual(self.test_model.get_coefficient(), 1.0)

    def test_fit_with_sample_weight(self):
        x = np.array([1, 2, 3, 4])
        y = np.array([1, 2, 3, 4])
        sample_weight = np.array([1, 1, 1, 1])
        self.test_model.fit(x, y, sample_weight)

        self.assertIsNotNone(self.test_model)
        self.assertEqual(self.test_model.get_intercept(), 0.0)
        self.assertEqual(self.test_model.get_coefficient(), 1.0)

    def test_fit_returns(self):
        company_1 = 'MSFT'
        company_2 = 'AAPL'
        self.test_model.fit_returns(company_1, company_2)

        self.assertIsNotNone(self.test_model)
        self.assertIsNotNone(self.test_model.get_intercept())
        self.assertIsNotNone(self.test_model.get_coefficient())

