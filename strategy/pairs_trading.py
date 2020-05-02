import numpy as np
import pandas as pd

from utils.data import stock_price_data


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

        self.closing_prices = stock_price_data.get_stocks_data_for_period(
            [self.company1, self.company2], start, end)

        self.closing_prices_1 = self.closing_prices[self.company1]
        self.closing_prices_2 = self.closing_prices[self.company2]

    def create_train_test_split(self, data: pd.Dataframe, split_index: int=None) -> (np.array, np.array):
        return data[:-self.train_test_split_index], data[-self.train_test_split_index:] if split_index is None else \
            data[:-split_index], data[-split_index:]

