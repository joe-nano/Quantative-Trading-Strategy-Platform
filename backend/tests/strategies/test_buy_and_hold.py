import unittest

from strategies.buy_and_hold import BuyAndHold


class TestBuyAndHold(unittest.TestCase):
    def test_init_with_no_company(self):
        buy_and_hold = BuyAndHold(10)
        self.assertIsNotNone(buy_and_hold)
        self.assertIsNone(buy_and_hold.company)
        self.assertIsNone(buy_and_hold.closing_prices)

        self.assertEqual(0, len(buy_and_hold.pnl))
        self.assertEqual(0, len(buy_and_hold.pos))
        self.assertEqual(0, len(buy_and_hold.time_in_trade))

    def test_init_with_company(self):
        buy_and_hold = BuyAndHold(10, 'AAPL')
        self.assertIsNotNone(buy_and_hold)
        self.assertIsNotNone(buy_and_hold.company)
        self.assertIsNotNone(buy_and_hold.closing_prices)

        self.assertEqual(0, len(buy_and_hold.pnl))
        self.assertEqual(0, len(buy_and_hold.pos))
        self.assertEqual(0, len(buy_and_hold.time_in_trade))

    def test_set_company_and_data(self):
        buy_and_hold = BuyAndHold(10)
        self.assertIsNotNone(buy_and_hold)
        self.assertIsNone(buy_and_hold.company)
        self.assertIsNone(buy_and_hold.closing_prices)

        self.assertEqual(0, len(buy_and_hold.pnl))
        self.assertEqual(0, len(buy_and_hold.pos))
        self.assertEqual(0, len(buy_and_hold.time_in_trade))

        company = 'AAPL'
        buy_and_hold.set_company_and_data(company)
        self.assertEqual(company, buy_and_hold.company)
        self.assertNotEqual(0, len(buy_and_hold.closing_prices))

    def test_perform_strategy(self):
        buy_and_hold = BuyAndHold(10, 'AAPL')
        buy_and_hold.perform_strategy()

        self.assertNotEqual(0, len(buy_and_hold.pos))
        self.assertNotEqual(0, len(buy_and_hold.pnl))