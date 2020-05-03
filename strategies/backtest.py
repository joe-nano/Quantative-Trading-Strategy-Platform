"""
Class for backtest

When our spread rises more than one standard deviation above the mean, we buy EWA and sell EWC in the proportion of our hedge ratio
When our spread falls to more than one standard deviation below the mean, we do the opposite.
"""
import numpy as np
import pandas as pd

from strategies.pairs_trading import PairsTrading


class Backtest:
    def __init__(self, pairs_trader: PairsTrading):
        """
        Constructor for backtest

        :param pairs_trader: PairsTrading data
        :type pairs_trader: PairsTrading Class
        """
        self.pairs_trader = pairs_trader
        self.inpos = 0
        self.pnl = []
        self.pos = []

        self.time_in_trade = []
        self.exit_date = []

        self.spread = pairs_trader.calculate_spread()
        self.threshold = pairs_trader.generate_threshold()

        self.entry_price, self.open_time = None, None

    # TODO: PnL analysis
    def perform_backtest(self) -> None:
        for date in self.spread.index:

            if self.spread[date] > self.threshold and not self.inpos:
                '''Entry Short Spread'''
                self.entry_price = self.spread[date]
                self.open_time = date
                self.inpos = -1

            elif self.spread[date] < 0 and self.inpos == -1:
                '''Exit Short Spread'''
                p = self.entry_price - self.spread[date]
                self.pnl.append(p)
                self.inpos = 0
                self.time_in_trade.append((date - self.open_time).days)
                self.exit_date.append(date)
                print('Exit short:', sum(self.pnl))

            elif self.spread[date] < -self.threshold and not self.inpos:
                '''Entry Long Spread'''
                self.entry_price = self.spread[date]
                self.open_time = date
                self.inpos = 1

            elif self.spread[date] > 0 and self.inpos == 1:
                '''Exit Long Spread'''
                p = self.spread[date] - self.entry_price
                self.pnl.append(p)
                self.inpos = 0
                self.time_in_trade.append((date - self.open_time).days)
                self.exit_date.append(date)
                print('Exit long:', sum(self.pnl))

            self.pos.append(self.inpos)

    def get_profit_per_trade(self) -> pd.Series:
        return pd.Series(self.pnl)

    def get_daily_pnl(self) -> np.array:
        pos1 = [0] + self.pos
        return self.spread.diff() * pos1[:-1]

    def get_cumulative_pnl(self) -> np.array:
        return np.cumsum(self.get_daily_pnl())

    def get_cumulative_profit_per_trade(self) -> np.array:
        return np.cumsum(self.get_profit_per_trade())

    def calculate_portfolio_size(self):
        return self.get_daily_pnl()/self.pairs_trader.get_portfolio_size()