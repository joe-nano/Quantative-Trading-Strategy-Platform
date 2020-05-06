import numpy as np

from sklearn.linear_model import LinearRegression
from utils.finance import formulas

from configs.logger import Logger

logger = Logger(__name__).log


class FinanceLinearRegressionModel(LinearRegression):

    def fit(self, x: np.array, y: np.array, sample_weight=None) -> LinearRegression:
        """
        Fit two numpy array into linear regression model
        :param x: data
        :type x: np.array
        :param y: data
        :type y: np.array
        :param sample_weight: sample weight, array like shape of sample weights
        :type sample_weight: np.array
        :return: the linear regression model, instant of self
        :rtype: LinearRegression
        """
        logger.info("Received these data for linear regression on x:\n{}\n\ny:{}".format(x, y))
        X = np.array([x]).T
        Y = np.array(y)
        if len(X) != len(Y):
            min_length = min(len(X), len(Y))
            X = X[:min_length]
            Y = Y[:min_length]
        logger.info("Linear regression on X:\n{}\n\nY:{}".format(X, Y))
        return super().fit(X, Y)

    def fit_returns(self, x: str, y: str) -> LinearRegression:
        """
        Fit two company's returns into the model

        :param x: code for company 1
        :type x: str
        :param y: code for company 2
        :type y: str
        :return: the linear regression model
        :rtype: LinearRegression
        """
        X = np.array(formulas.calculate_percentage_change_based_on_adjusted_closing_price(x)[x]).T
        Y = np.array(formulas.calculate_percentage_change_based_on_adjusted_closing_price(y)[y])
        return super().fit(X, Y)

    def get_intercept(self) -> float:
        """
        Return the intercept of the model

        :return: the intercept
        :rtype: float
        """
        return self.intercept_

    def get_coefficient(self) -> np.array:
        """
        Return the coefficient of the model

        :return: the coefficient of the model
        :rtype: np.array
        """
        return self.coef_
