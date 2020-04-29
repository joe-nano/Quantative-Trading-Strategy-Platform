import typing
import pandas_datareader
import pandas as pd


def get_stock_data(code: str) -> pd.DataFrame:
    try:
        return pandas_datareader.get_data_yahoo(code)
    except Exception as e:
        print('Error retrieving data from Yahoo Finance, company code used: {}, Exception: '.format(code, e))


def get_stocks_data(codes: typing.List[str]) -> pd.DataFrame:
    try:
        return pandas_datareader.get_data_yahoo(codes)
    except Exception as e:
        print('Error retrieving data from Yahoo Finance, company code used: {}, Exception: '.format(codes, e))
