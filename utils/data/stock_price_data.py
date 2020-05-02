import typing
import pandas_datareader
import pandas as pd


def get_stock_data(code: str) -> pd.DataFrame:
    """
    Get historical stock closing_prices from Yahoo finance

    :param code: company code
    :type code: str
    :return: stocks closing_prices
    :rtype: pd.Dataframe
    """
    try:
        return pandas_datareader.get_data_yahoo(code)
    except Exception as e:
        print('Error retrieving closing_prices from Yahoo Finance, company code used: {}, Exception: '.format(code, e))


def get_stocks_data(codes: typing.List[str]) -> pd.DataFrame:
    """
    Get historical stock closing_prices from Yahoo finance for a list of companies

    :param codes: company codes
    :type codes: list[str]
    :return: stocks closing_prices
    :rtype: pd.Dataframe
    """
    try:
        return pandas_datareader.get_data_yahoo(codes)
    except Exception as e:
        print('Error retrieving closing_prices from Yahoo Finance, company codes used: {}, Exception: '.format(codes, e))


def get_stock_data_for_period(code: str, start: str, end: str) -> pd.DataFrame:
    """
    Get historical stock closing_prices from Yahoo finance for a start and end period

    :param code: company code
    :type code: str
    :param start: start date
    :type start: str
    :param end: end date
    :type end: str
    :return: stocks closing_prices
    :rtype: pd.Dataframe
    """
    try:
        return pandas_datareader.get_data_yahoo(code, start, end)
    except Exception as e:
        print('Error retrieving closing_prices from Yahoo Finance, company code used: {}, Exception: '.format(code, e))


def get_stocks_data_for_period(codes: typing.List[str], start: str, end: str) -> pd.DataFrame:
    """
    Get historical stock closing_prices from Yahoo finance for a start and end period

    :param codes: company code
    :type codes: list[str]
    :param start: start date
    :type start: str
    :param end: end date
    :type end: str
    :return: stocks closing_prices
    :rtype: pd.Dataframe
    """
    try:
        return pandas_datareader.get_data_yahoo(codes, start, end)
    except Exception as e:
        print('Error retrieving closing_prices from Yahoo Finance, company codes used: {}, Exception: '.format(codes, e))
