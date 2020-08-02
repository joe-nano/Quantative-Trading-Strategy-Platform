import unittest
import pytest

from datatypes.exceptions.data import DataRetrievalException
from utils.data.stock_price_data import *
from utils.datetime.helpers import get_number_of_days_between_two_dates


class TestStockPriceData(unittest.TestCase):
    def setUp(self):
        self.company = 'AMZN'
        self.companies = ['AAPL', 'AMZN']
        self.non_exist_company = 'NON_EXIST'
        self.non_exist_companies = ['NON_EXIST']
        self.start_date = '2020-01-02'
        self.end_date = '2020-01-03'
        self.default_pandas_data_reader_number_of_columns = 6

    def test_get_stock_data(self):
        self.assertIsNotNone(get_stock_data(self.company))

    def test_get_stock_data_with_exception(self):
        with pytest.raises(DataRetrievalException):
            self.assertIsNotNone(get_stock_data(self.non_exist_company))

    def test_get_stocks_data(self):
        self.assertIsNotNone(get_stocks_data(self.companies))

    def test_get_stocks_data_with_exception(self):
        with pytest.raises(DataRetrievalException):
            self.assertIsNotNone(get_stocks_data(self.non_exist_companies))

    def test_get_stock_data_for_period(self):
        result = get_stock_data_for_period(self.company, self.start_date, self.end_date)
        expected_size = get_number_of_days_between_two_dates(self.start_date, self.end_date)

        self.assertIsNotNone(result)
        self.assertEqual(result.shape, (expected_size, self.default_pandas_data_reader_number_of_columns))

    def test_get_stock_data_for_period_with_exception(self):
        with pytest.raises(DataRetrievalException):
            get_stock_data_for_period(self.non_exist_company, self.start_date, self.end_date)

    def test_get_stocks_data_for_period(self):
        result = get_stocks_data_for_period(self.companies, self.start_date, self.end_date)
        expected_size = get_number_of_days_between_two_dates(self.start_date, self.end_date)

        self.assertIsNotNone(result)
        self.assertEqual(result.shape,
                         (expected_size, len(self.companies)*self.default_pandas_data_reader_number_of_columns))

    def test_get_stocks_data_for_period_with_exception(self):
        with pytest.raises(DataRetrievalException):
            get_stocks_data_for_period(self.non_exist_companies, self.start_date, self.end_date)

    def test_get_stock_data_adjusted_closing_price(self):
        result = get_stock_data_adjusted_closing_price(self.company)

        self.assertIsNotNone(result)

    def test_get_stocks_data_adjusted_closing_price(self):
        result = get_stocks_data_adjusted_closing_price(self.companies)

        self.assertIsNotNone(result)

    def test_get_stock_data_adjusted_closing_price_for_period(self):
        result = get_stock_data_adjusted_closing_price_for_period(self.company, self.start_date, self.end_date)
        expected_size = get_number_of_days_between_two_dates(self.start_date, self.end_date)

        self.assertIsNotNone(result)
        self.assertEqual(result.shape[0], expected_size)

    def test_get_stocks_data_adjusted_closing_price_for_period(self):
        result = get_stocks_data_adjusted_closing_price_for_period(self.companies, self.start_date, self.end_date)
        expected_size = get_number_of_days_between_two_dates(self.start_date, self.end_date)

        self.assertIsNotNone(result)
        self.assertEqual(result.shape[0], expected_size)