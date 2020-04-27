import numpy as np



def calculate_volume_weighed_average_price(closing_prices, volumes):
    """
    Calculate VWAP using sum of daily_volume x price divided by total volume

    :param closing_prices: stock prices closing prices
    :type closing_prices: list
    :param volumes: stock volumes on those days
    :type volumes: list
    :return: VWAP prices
    :rtype: int
    """
    return np.sum(np.multiply(closing_prices, volumes))/np.sum(volumes)
