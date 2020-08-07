import numpy as np
import pandas as pd

from datatypes.linear_regression_plot_properties import LinearRegressionPlotProperties
from utils.data import stock_price_data
from utils.analysis.linear_regression import FinanceLinearRegressionModel

from configs.logger import Logger

logger = Logger(__name__).log


class PairsTrading(object):
    def __init__(self, company1: str, company2: str, start: str, end: str):
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

        self.lm = FinanceLinearRegressionModel()

        self.closing_prices = stock_price_data.get_stocks_data_adjusted_closing_price_for_period(
            [self.company1, self.company2], start, end)

        self.closing_prices_1 = self.closing_prices[self.company1]
        self.closing_prices_2 = self.closing_prices[self.company2]

        self.train_test_split_index = int(((len(self.closing_prices_1) + len(self.closing_prices_2)) // 2) * 0.7)

        self.threshold_multiplier = 0.5  # acceptance value for trading signal
        self.linear_regression_properties = None

    def _create_train_test_split(self, data: pd.DataFrame, split_index: int=None) -> (np.array, np.array):
        logger.info("Creating train test split with split index: {} and data:\n{}".format(split_index, data))
        data.dropna(inplace=True)
        if split_index is None:
            return data[:-self.train_test_split_index], data[-self.train_test_split_index:]
        else:
            return data[:-split_index], data[-split_index:]

    def perform_linear_regression(self):
        """
        Performs linear regression

        :return: linear regression plot properties
        :rtype: LinearRegressionPlotProperties
        """
        x_train, x_test = self._create_train_test_split(self.closing_prices_1)
        y_train, y_test = self._create_train_test_split(self.closing_prices_2)
        self.lm = self.lm.fit(x_train, y_train)
        a = self.lm.get_intercept()
        beta = self.lm.get_coefficient()

        xx = np.linspace(min(x_train), max(x_train), 200)
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
        if not self.linear_regression_properties:
            self.linear_regression_properties = self.perform_linear_regression()
        return self.closing_prices_2[0] + self.linear_regression_properties.get_hedge_ratio() * self.closing_prices_1[0]

    def generate_trading_signal_plot(self) -> None:
        """
        Generate a trading signal plot based on the given data for visualisation purposes
        """
        import matplotlib.pyplot as plt
        training_data_spread = self.calculate_spread()[:self.train_test_split_index]
        testing_data_spread = self.calculate_spread()[self.train_test_split_index:]
        threshold_value = self.generate_threshold()

        plt.plot(training_data_spread)
        plt.plot(testing_data_spread, color='g')
        plt.legend(['training data', 'test data'])
        plt.axhline(y=threshold_value, color='r')
        plt.axhline(y=-threshold_value, color='r')
        plt.ylabel('Spread of {} and {}'.format(self.company1, self.company2))
        plt.grid()
        plt.show()
