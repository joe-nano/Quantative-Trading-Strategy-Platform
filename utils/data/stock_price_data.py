import pandas_datareader


def get_stock_data(code):
    try:
        return pandas_datareader.get_data_yahoo(code)
    except Exception as e:
        print('Error retrieving data from Yahoo Finance, company code used: {}, Exception: '.format(code, e))
