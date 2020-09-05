import math


def format_price(n: int) -> str:
    """
    format price to 2dp

    :param n: value to format
    :type n: flat
    :return: price in 2 dp
    :rtype: str
    """
    return ('-$' if n < 0 else '$') + "{0:.2f}".format(abs(n))


def sigmoid(x: float) -> float:
    """
    Calculate sigmoid

    :param x: value
    :type x: float
    :return: sigmoid value
    :rtype: float
    """
    return 1 / (1 + math.exp(-x))
