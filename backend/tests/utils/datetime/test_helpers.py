import unittest
from utils.datetime.helpers import *


class TestDateTimeHelpers(unittest.TestCase):
    def test_get_current_date_str(self):
        self.assertIsNotNone(get_current_date_str())
        self.assertTrue('/' in get_current_date_str('%YY/%m/%d'))

    def test_get_current_date_one_year_ago_str(self):
        self.assertNotEqual(get_current_date_str(), get_current_date_one_year_ago_str())
        self.assertTrue('/' in get_current_date_one_year_ago_str('%YY/%m/%d'))

    def test_get_current_date_some_year_ago_str(self):
        self.assertNotEqual(get_current_date_one_year_ago_str(), get_current_date_some_year_ago_str(2))
        self.assertTrue('/' in get_current_date_some_year_ago_str(2, '%YY/%m/%d'))
