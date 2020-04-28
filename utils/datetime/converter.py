import pytz


from datetime import datetime, timedelta
from dateutil.parser import parse
from utils.datetime.timezones import UTC
from delorean import Delorean


def get_current_time_in_utc():
    return datetime.now(pytz.timezone(UTC))


def convert_simple_datetime_string_to_datetime():
    pass


def get_current_time_in_timezone(timezone: str):
    try:
        return datetime.now(pytz.timezone(timezone))
    except Exception as e:
        get_invalid_timezone_exception(e, timezone)


def get_datetime_in_timezone(year: int, month: int, date: int, timezone: str):
    try:
        return Delorean(datetime(year, month, date), timezone=timezone).datetime
    except Exception as e:
        get_invalid_timezone_exception(e, timezone)


def get_time_difference_to_timezone_delorean(src_datetime: Delorean, timezone_to_lookup: str):
    try:
        return src_datetime.datetime - src_datetime.shift(timezone_to_lookup).datetime
    except Exception as e:
        get_invalid_timezone_exception(e, timezone_to_lookup)


def get_time_difference_to_timezone():
    pass


def get_invalid_timezone_exception(e: Exception, timezone: str):
    print('Invalid timezone {} used, got exception: {}'.format(timezone, e))