import unittest
import pytest

from utils.datetime.converter import *
from utils.datetime.constants import timezones

from datatypes.exceptions.timezones import TimeZoneConversionException


class TestConverter(unittest.TestCase):
    def test_get_current_time_in_utc(self):
        self.assertEqual(get_current_time_in_utc().month, datetime.now(pytz.timezone(UTC)).month)

    def test_get_current_time_in_local_time_zone(self):
        self.assertEqual(datetime.now().day, get_current_time_in_local_time_zone().day)

    def test_get_current_time_in_timezone(self):
        self.assertIsNotNone(get_current_time_in_timezone(timezones.AEST))

    def test_get_current_time_in_timezone_with_invalid_timezone_exception(self):
        with pytest.raises(TimeZoneConversionException):
            get_current_time_in_timezone('Unknown Time Zone')

    def test_get_datetime_in_timezone(self):
        self.assertIsNotNone(get_datetime_in_timezone(2020, 10, 2, timezones.US_EASTERN_DAYLIGHT_TIME))

    def test_get_datetime_in_timezone_with_invalid_timezone_exception(self):
        with pytest.raises(TimeZoneConversionException):
            get_datetime_in_timezone(20001, 13, 40, 'Unknown timezone')(timezones.UTC, 'Unknown timezone')
