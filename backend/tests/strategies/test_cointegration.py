import unittest
import pytest
from strategies.cointegration import Cointegration
from datatypes.cointegration_result import CointegrationResult


class TestCointegration(unittest.TestCase):
    def setUp(self):
        self.company1 = 'AAPL'
        self.company2 = 'CBA.AX'
        self.companies = [self.company1, self.company2]
        self.cointegration = Cointegration(self.companies)

    def test_perform_cointegration(self):
        result = self.cointegration.perform_cointegration(self.company1, self.company2)
        self.assertIsInstance(result, CointegrationResult)
        self.assertTrue(result.pvalue > 0)
        self.assertTrue(result.coint_t > 0)
        self.assertTrue(len(result.crit) == 3)

    def test_perform_cointegration_raise_value_error_on_invalid_input(self):
        with pytest.raises(ValueError):
            self.cointegration.perform_cointegration('AMZN', self.company2)
