"""
Class for cointegration

Cointegration is a statistical property of a collection of time series
variables. First, all of the series must be integrated of order d. Next,
if a linear combination of this collection is integrated of order less
than d, then the collection is said to be co-integrated.

Cointegration is the existence of long-run relationship between two or more variables. However, the correlation does
not necessarily means "long-run". Correlation is simply a measure of the
degree of mutual association between two or more variables.
"""
import typing

from datatypes.cointegration_result import CointegrationResult
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
        self.closing_prices = stock_price_data.get_stocks_data_adjusted_closing_price(self.companies)
        self.closing_prices.dropna(inplace=True)

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
        if company1 not in self.companies or company2 not in self.companies:
            raise ValueError('Input companies: {}, {} must be in the list of companies used to construct '
                             'with: {}'.format(company1, company2, self.companies))
        coint_t, pvalue, crit = coint(self.closing_prices[company1], self.closing_prices[company2])
        return CointegrationResult(coint_t=coint_t, pvalue=pvalue, crit=crit)
