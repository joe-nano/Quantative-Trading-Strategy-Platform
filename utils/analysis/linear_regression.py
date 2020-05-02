import numpy as np

from sklearn.linear_model import LinearRegression
from utils.finance import formulas


class FinanceLinearRegressionModel:
    def __init__(self):
        self.lm = LinearRegression()

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
        return self.lm.fit(X, Y)

    def get_intercept(self) -> float:
        """
        Return the intercept of the model

        :return: the intercept
        :rtype: float
        """
        return self.lm.intercept_

    def get_coefficient(self) -> np.array:
        """
        Return the coefficient of the model

        :return: the coefficient of the model
        :rtype: np.array
        """
        return self.lm.coef_
