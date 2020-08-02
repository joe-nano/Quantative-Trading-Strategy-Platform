import typing
import pandas_datareader
import pandas as pd

from utils.data.constants.column_headings import *
from datatypes.exceptions import data

error_msg = 'Error retrieving closing_prices from Yahoo Finance, company code used: {}, Exception: {}'


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
        raise_retrieval_error(code, e)


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
        raise_retrieval_errors(codes, e)


def get_stock_data_for_period(code: str, start: str, end: str) -> pd.DataFrame:
    """
    Get historical stock closing_prices from Yahoo finance for a start and end period

    :param code: company code
    :type code: str
    :param start: start date
    :type start: str
    :param end: end date
    :type end: str
    :return: stocks data
    :rtype: pd.Dataframe
    """
    try:
        return pandas_datareader.get_data_yahoo(code, start, end)
    except Exception as e:
        raise_retrieval_error(code, e)


def get_stocks_data_for_period(codes: typing.List[str], start: str, end: str) -> pd.DataFrame:
    """
    Get historical stock closing_prices from Yahoo finance for a start and end period

    :param codes: company code
    :type codes: list[str]
    :param start: start date
    :type start: str
    :param end: end date
    :type end: str
    :return: stocks data
    :rtype: pd.Dataframe
    """
    try:
        return pandas_datareader.get_data_yahoo(codes, start, end)
    except Exception as e:
        raise_retrieval_errors(codes, e)


def get_stock_data_adjusted_closing_price(code: str) -> pd.DataFrame:
    """
    Get historical stock closing_prices from Yahoo finance

    :param code: company code
    :type code: str
    :return: stocks adjusted closingprices
    :rtype: pd.Dataframe
    :param code:
    :type code:
    """
    return get_stock_data(code)[ADJUSTED_CLOSING_PRICE]


def get_stocks_data_adjusted_closing_price(codes: typing.List[str]) -> pd.DataFrame:
    """
    Get historical stock closing_prices from Yahoo finance

    :param codes: company codes
    :type codes: list[str]
    :return: stocks adjusted closingprices
    :rtype: pd.Dataframe
    :param codes:
    :type code:
    """
    return get_stocks_data(codes)[ADJUSTED_CLOSING_PRICE]


def get_stock_data_adjusted_closing_price_for_period(code: str, start: str, end: str) -> pd.DataFrame:
    """
    Get historical stock closing_prices from Yahoo finance for a start and end period

    :param code: company code
    :type code: str
    :param start: start date
    :type start: str
    :param end: end date
    :type end: str
    :return: adjusted closing price data
    :rtype: pd.Dataframe
    """
    return get_stock_data_for_period(code, start, end)[ADJUSTED_CLOSING_PRICE]


def get_stocks_data_adjusted_closing_price_for_period(codes: typing.List[str], start: str, end: str) -> pd.DataFrame:
    """
    Get historical stock closing_prices from Yahoo finance for a start and end period

    :param codes: company codes
    :type codes: list[str]
    :param start: start date
    :type start: str
    :param end: end date
    :type end: str
    :return: adjusted closing price data
    :rtype: pd.Dataframe
    """
    return get_stocks_data_for_period(codes, start, end)[ADJUSTED_CLOSING_PRICE]


def raise_retrieval_error(code: str, exception: Exception, msg: str=error_msg):
    msg = msg.format(code, exception)
    raise data.DataRetrievalException(msg, exception)


def raise_retrieval_errors(codes: typing.List[str], exception: Exception, msg: str=error_msg):
    msg = msg.format(codes, exception)
    raise data.DataRetrievalException(msg, exception)