import numpy as np


class CointegrationResult:
    def __init__(self, coint_t: float, pvalue: float, crit: np.array):
        """
        Constructor for cointegration result

        :param coint_t: t-statistic of unit-root test on residuals
        :type coint_t: float
        :param pvalue: p-value
        :type pvalue: float
        :param crit: critical values for the test statistic at the 1%, 5%, and 10% levels
        :type crit: np.array
        """
        self.coint_t = coint_t
        self.pvalue = pvalue
        self.crit = crit
