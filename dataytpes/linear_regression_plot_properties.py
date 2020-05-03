import numpy as np


class LinearRegressionPlotProperties:
    def __init__(self, xx: np.array, yy: np.array, a: float, beta: np.array):
        """
        Constructor for LinearRegressionPlotProperties
        :param xx: plot points for x values
        :type xx: np.array
        :param yy: plot points for y values
        :type yy: np.array
        :param a: the intercept point
        :type a: float
        :param beta: beta values
        :type beta: np.array
        """
        self.xx, self.yy = xx, yy
        self.a = a
        self.beta = beta

    def get_hedge_ratio(self) -> float:
        """
        Get hedge ratio from beta values

        :return: hedge ratio
        :rtype: float
        """
        return self.beta[0]
