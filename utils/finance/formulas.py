import numpy as np
import pandas as pd

from utils.data.stock_price_data import get_stock_data
from utils.data.column_headings import CLOSE, RETURNS
from utils.data.sample_rates import WEEK, MONTH


def calculate_volume_weighed_average_price(closing_prices: list, volumes: list) -> int:
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


def calculate_percentage_change(data: pd.DataFrame) -> pd.DataFrame:
    return data[CLOSE].pct_change()


def calculate_returns_daily(code: str) -> pd.DataFrame:
    """
    Calculate daily returns given a code

    :param code: code of the company
    :type code: str
    :return: daily percentage change
    :rtype: pd.Dataframe
    """
    data = get_stock_data(code)
    return calculate_percentage_change(data)


def calculate_returns_weekly(code: str) -> pd.DataFrame:
    """
    Calculate weekly returns given a code

    :param code: code of the company
    :type code: str
    :return: weekly percentage change
    :rtype: pd.Dataframe
    """
    data = get_stock_data(code)
    data[CLOSE].resample(WEEK).ffill().pct_change()


def calculate_returns_monthly(code: str) -> pd.DataFrame:
    """
    Calculate monthly return given a code

    :param code: code of the company
    :type code: str
    :return: monthly percentage change
    :rtype: pd.Dataframe
    """
    data = get_stock_data(code)
    return data[CLOSE].resample(MONTH).ffill().pct_change()


def calculate_cumulative_returns(code: str) -> pd.DataFrame:
    data = get_stock_data(code)
    data[RETURNS] = calculate_percentage_change(data)
    return (data[RETURNS] + 1).cumprod()
