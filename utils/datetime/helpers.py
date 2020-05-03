from datetime import datetime, timedelta
from utils.datetime.converter import *
from utils.finance.constants import NUMBER_OF_DAYS_IN_A_YEAR

DATE_STRING_FORMATTER = 'YY/MM/dd'


def get_current_date_str(formatter=DATE_STRING_FORMATTER) -> str:
    return get_current_time_in_utc().strftime(formatter)


def get_current_date_one_year_ago_str(formatter=DATE_STRING_FORMATTER) -> str:
    return (get_current_time_in_utc() - timedelta(days=NUMBER_OF_DAYS_IN_A_YEAR)).strftime(formatter)


def get_current_date_some_year_ago_str(year: int, formatter=DATE_STRING_FORMATTER) -> str:
    return (get_current_time_in_utc() - timedelta(days=year*NUMBER_OF_DAYS_IN_A_YEAR)).strftime(formatter)
