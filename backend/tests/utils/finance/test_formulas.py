import unittest
import pytest

from utils.finance.formulas import *


class TestFormulas(unittest.TestCase):

    def setUp(self):
        self.company_index = 'CBA.AX';

    def test_calculate_volume_weighed_average_price(self):
        closing_prices = [1, 2, 3, 4, 5]
        volumes = [10, 10, 10, 10, 10]

        result = calculate_volume_weighed_average_price(closing_prices=closing_prices,
                                                        volumes=volumes)

        self.assertEqual(result, 3)

    def test_calculate_volume_weighed_average_price_different_length_exception(self):
        closing_prices = [1, 2, 3, 4, 5, 10]
        volumes = [10, 10, 10, 10, 10]

        with pytest.raises(Exception):
            calculate_volume_weighed_average_price(closing_prices=closing_prices,
                                                   volumes=volumes)

    def test_calculate_returns_daily(self):
        self.assertIsNotNone(calculate_returns_daily(self.company_index))

    def test_calculate_returns_weekly(self):
        self.assertIsNotNone(calculate_returns_weekly(self.company_index))

    def test_calculate_returns_monthly(self):
        self.assertIsNotNone(calculate_returns_monthly(self.company_index))

    def test_calculate_cumulative_returns(self):
        self.assertIsNotNone(calculate_cumulative_returns(self.company_index))

    def test_calculate_volatility(self):
        self.assertIsNotNone(calculate_volatility(self.company_index))

    def test_calculate_annualised_volatility_for_daily_data(self):
        self.assertIsNotNone(calculate_annualised_volatility_for_daily_data(self.company_index, 100))

    def test_calculate_annualised_volatility_for_hourly_data(self):
        self.assertIsNotNone(calculate_annualised_volatility_for_hourly_data(self.company_index, 100))

    def test_calculate_percentage_change_based_on_adjusted_closing_price(self):
        self.assertIsNotNone(calculate_percentage_change_based_on_adjusted_closing_price(self.company_index))

    def test_calculate_percentage_changes_based_on_adjusted_closing_price(self):
        self.assertIsNotNone(calculate_percentage_changes_based_on_adjusted_closing_price([self.company_index]))

    def test_calculate_correlation(self):
        self.assertIsNotNone(calculate_correlation([self.company_index]))

    def test_calculate_correlation_over_time(self):
        self.assertIsNotNone(calculate_correlation_over_time([self.company_index], 500))

    def test_calculate_correlation_a_year(self):
        self.assertIsNotNone(calculate_correlation_over_a_year([self.company_index]))

    def test_calculate_correlation_over_time_period_between_two_companies(self):
        self.assertIsNotNone(calculate_correlation_over_time_period_between_two_companies(
            self.company_index, self.company_index, 5))

    def test_calculate_correlation_over_a_year_between_two_companies(self):
        self.assertIsNotNone(calculate_correlation_over_a_year_between_two_companies(
            self.company_index, self.company_index))
