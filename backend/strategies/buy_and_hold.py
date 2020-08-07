"""
Class for buy and hold strategy
"""
from datetime import timedelta

from utils.data import stock_price_data
from utils.data.constants import column_headings


class BuyAndHold:
    def __init__(self, holding_period: int, company: str=None):
        """
        Constructor for buy and hold strategy

        :param holding_period: holding period to use
        :type holding_period: int
        """
        self.holding_period = timedelta(holding_period)

        # This indicates whether we have a position on or not
        self.inpos = 0

        # current time to wait
        self.wait = 0

        # This is the PnL
        self.pnl = []
        self.pos = []
        self.time_in_trade = []

        self.company = company
        if not self.company:
            self.closing_prices = None
        else:
            self.set_company_and_data(self.company)

    def set_company_and_data(self, code: str):
        """
        Set the company and the closing_prices for this buy and hold strategy

        :param code: company code
        :type code: str
        """
        self.company = code
        self.closing_prices = stock_price_data.get_stock_data(self.company)[column_headings.ADJUSTED_CLOSING_PRICE]

    def perform_strategy(self):
        """
        Perform the buy and hold strategy on the given closing_prices set
        """
        dates = self.closing_prices.index
        entry_price = self.closing_prices[dates[0]]
        open_time = self.closing_prices.index[0]

        for date in dates:
            if self.inpos == 0 and self.wait == 2:
                entry_price = self.closing_prices[date]
                open_time = date
                self.inpos = 1

            elif self.inpos == 1 and date - open_time >= self.holding_period:
                # Profit/loss for this trade
                p = self.closing_prices[date] - entry_price
                self.pnl.append(p)
                self.inpos = 0

            elif self.inpos == 0 and self.wait < 2:
                self.wait += 1

            self.pos.append(self.inpos)
