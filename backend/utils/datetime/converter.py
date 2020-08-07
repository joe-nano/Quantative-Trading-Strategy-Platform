import pytz

from datetime import datetime
from utils.datetime.constants.timezones import UTC
from delorean import Delorean

from datatypes.exceptions import timezones


def get_current_time_in_utc() -> datetime:
    return datetime.now(pytz.timezone(UTC))


def get_current_time_in_local_time_zone() -> datetime:
    return datetime.now()


def convert_simple_datetime_string_to_datetime():
    pass


def get_current_time_in_timezone(timezone: str) -> datetime:
    try:
        return datetime.now(pytz.timezone(timezone))
    except Exception as e:
        get_invalid_timezone_exception(e, timezone)


def get_datetime_in_timezone(year: int, month: int, date: int, timezone: str) -> Delorean:
    try:
        return Delorean(datetime(year, month, date), timezone=timezone)
    except Exception as e:
        get_invalid_timezone_exception(e, timezone)

def get_invalid_timezone_exception(e: Exception, timezone: str) -> None:
    message = 'Invalid timezone {} used, got exception: {}'.format(timezone, e)
    raise timezones.TimeZoneConversionException(message, e)
