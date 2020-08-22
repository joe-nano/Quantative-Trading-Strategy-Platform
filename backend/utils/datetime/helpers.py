from datetime import timedelta
from utils.datetime.converter import *
from utils.finance.constants.trading_days import NUMBER_OF_DAYS_IN_A_YEAR

DATE_STRING_FORMATTER = '%Y-%m-%d'


def get_current_date_str(formatter=DATE_STRING_FORMATTER) -> str:
    """
    Get current date with the format

    :param formatter: format of date
    :type formatter: str
    :return: date
    :rtype: str
    """
    return get_current_time_in_local_time_zone().strftime(formatter)


def get_current_date_one_year_ago_str(formatter=DATE_STRING_FORMATTER) -> str:
    """
    Get a current date from some years ago

    :param formatter: format of date
    :type formatter: str
    :return: Date before some years
    :rtype: str
    """
    return (get_current_time_in_local_time_zone() - timedelta(days=NUMBER_OF_DAYS_IN_A_YEAR)).strftime(formatter)


def get_current_date_some_year_ago_str(year: int, formatter=DATE_STRING_FORMATTER) -> str:
    """
    Get a current date from some years ago

    :param year: number of years before
    :type year: int
    :param formatter: format of date
    :type formatter: str
    :return: Date before some years
    :rtype: str
    """
    return (get_current_time_in_local_time_zone() - timedelta(days=year*NUMBER_OF_DAYS_IN_A_YEAR)).strftime(formatter)


def get_number_of_days_between_two_dates(d1: str, d2: str) -> int:
    """
    Get number of days between days including the end date

    :param d1: date 1 in '%Y-%m-%d' format
    :type d1: str
    :param d2: date 2 in '%Y-%m-%d' format
    :type d2: str
    :return: difference in number of dates
    :rtype: int
    """
    d1 = datetime.strptime(d1, DATE_STRING_FORMATTER)
    d2 = datetime.strptime(d2, DATE_STRING_FORMATTER)
    return abs((d2 - d1).days) + 1
