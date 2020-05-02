"""
Class for cointegration
"""
import typing

from dataytpes.cointegration_result import CointegrationResult
from utils.data import stock_price_data
from statsmodels.tsa.stattools import coint


class Cointegration:
    def __init__(self, companies: typing.List[str]):
        """
        Constructor for cointegration

        :param companies: list of companies
        :type companies: list[str]
        """
        self.companies = companies
        self.closing_prices = stock_price_data.get_stocks_data(self.companies)

    def perform_cointegration(self, company1: str, company2: str) -> CointegrationResult:
        """
        Perform cointegration

        :param company1: company 1 in the list of companies
        :type company1: str
        :param company2: company 1 in the list of companies
        :type company2: str
        :return: t-statistic of unit-root test on residuals
        :rtype: float
        :return: p-value
        :rtype: float
        :return: Critical values for the test statistic at the 1%, 5%, and 10% levels
        :rtype: np.array
        """
        coint_t, pvalue, crit = coint(self.closing_prices[company1], self.closing_prices[company2])
        return CointegrationResult(coint_t=coint_t, pvalue=pvalue, crit=crit)
