import numpy as np
import pandas as pd

from dataytpes.linear_regression_plot_properties import LinearRegressionPlotProperties
from utils.data import stock_price_data
from utils.analysis.linear_regression import FinanceLinearRegressionModel


class PairsTrading:
    def __int__(self, company1: str, company2: str, start: str, end: str):
        """
        Constructor for Pairs trading

        :param company1: company 1 code
        :type company1: str
        :param company2: company 2 code
        :type company2: str
        :param start: start date
        :type start: str
        :param end: end date
        :type end: str
        """
        self.company1, self.company2 = company1, company2
        self.start, self.end = start, end

        self.train_test_split_index = -500

        self.lm = FinanceLinearRegressionModel()

        self.closing_prices = stock_price_data.get_stocks_data_for_period(
            [self.company1, self.company2], start, end)

        self.closing_prices_1 = self.closing_prices[self.company1]
        self.closing_prices_2 = self.closing_prices[self.company2]

        self.threshold_multiplier = 0.5  # acceptance value for trading signal
        self.linear_regression_properties = None

    def create_train_test_split(self, data: pd.DataFrame, split_index: int=None) -> (np.array, np.array):
        return data[:-self.train_test_split_index], data[-self.train_test_split_index:] if split_index is None else \
            data[:-split_index], data[-split_index:]

    def perform_linear_regression(self):
        x = self.create_train_test_split(self.closing_prices_1)
        y = self.create_train_test_split(self.closing_prices_2)
        self.lm = self.lm.fit(x, y)
        a = self.lm.get_intercept()
        beta = self.lm.get_coefficient()

        xx = np.linspace(min(x), max(x), 200)
        yy = a + beta * xx
        self.linear_regression_properties = LinearRegressionPlotProperties(xx=xx, yy=yy, a=a, beta=beta)
        return self.linear_regression_properties

    def calculate_spread(self) -> np.array:
        """
        Calculate spread between the two companies

        :return: spread values
        :rtype: np.array
        """
        if not self.linear_regression_properties:
            self.linear_regression_properties = self.perform_linear_regression()
        return self.closing_prices_2 - self.linear_regression_properties.get_hedge_ratio()\
               * self.closing_prices_1 - self.linear_regression_properties.a

    def generate_threshold(self) -> float:
        """
        Generate threshold value for a trading signal

        :return: threshold value
        :rtype: float
        """
        return np.std(self.calculate_spread()) * self.threshold_multiplier

    def get_portfolio_size(self) -> float:
        """
        Calculate portfolio size

        :return: portfolio size
        :rtype: float
        """
        return self.closing_prices_2[0] + self.linear_regression_properties.get_hedge_ratio() * self.closing_prices_1[0]
