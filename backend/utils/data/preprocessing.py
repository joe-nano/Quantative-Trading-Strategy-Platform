import pandas as pd
import datetime
import typing

from utils.data.constants.column_headings import *


def make_data_match(stock_one_data: pd.DataFrame, stock_two_data: pd.DataFrame) ->\
        typing.Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Pre-Processing data and drop dates that is not in both stock data

    :param stock_one_data:
    :type stock_one_data:
    :param stock_two_data:
    :type stock_two_data:
    :return:
    :rtype:
    """
    # Truncate data by date
    if stock_one_data[DATE][0] > stock_two_data[DATE][0]:
        stock_one_data = stock_one_data[stock_one_data.Date >= stock_two_data['Date'][0]]
        stock_one_data.reset_index(inplace=True, drop=True)
    else:
        stock_two_data = stock_two_data[stock_two_data.Date >= stock_one_data['Date'][0]]
        stock_two_data.reset_index(inplace=True, drop=True)

    # Remove dates not in either data
    list1 = stock_one_data[DATE]
    list2 = stock_two_data[DATE]
    diff_pd1_data = list(set(list1) - set(list2))
    diff_pd2_data = list(set(list2) - set(list1))
    for k in range(len(diff_pd1_data)):
        pd1_dat_format = diff_pd1_data[k].strftime('%Y-%m-%d 00:00:00')
        date_format_pd1 = datetime.datetime.strptime(pd1_dat_format, "%Y-%m-%d 00:00:00")
        for i, j in enumerate(list1):
            if j == date_format_pd1:
                stock_one_data.drop([i], inplace=True)

    stock_one_data.reset_index(inplace=True, drop=True)

    for k in range(len(diff_pd2_data)):
        pd2_dat_format = diff_pd2_data[k].strftime('%Y-%m-%d 00:00:00')
        date_format_pd2 = datetime.datetime.strptime(pd2_dat_format, "%Y-%m-%d 00:00:00")
        for M, N in enumerate(list2):
            if N == date_format_pd2:
                stock_two_data.drop([M], inplace=True)

    stock_two_data.reset_index(inplace=True, drop=True)
    return stock_one_data, stock_two_data


def get_train_test_split(data: pd.DataFrame, train_split: int, test_split: int) -> \
        typing.Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Get train test split data, default to 7:3 split if input is bad

    :param data: data to split
    :type data: pd.Dataframe
    :param train_split: training set split index
    :type train_split: int
    :param test_split: testing set size
    :type test_split: int
    :return: training and testing data set
    :rtype: Tuple(pd.Dataframe, pd.Dataframe)
    """
    if train_split + test_split > len(data):
        return data[:int(len(data)*0.7)], data[int(len(data)*0.7):]
    return data[:train_split], data[train_split: train_split+test_split]
