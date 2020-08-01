from utils.finance import formulas
from utils.finance.constants import TRADING_DAYS_IN_A_YEAR
from utils.datetime import helpers as datetime_helpers
from strategies.pairs_trading import PairsTrading
from strategies.backtest import Backtest
from strategies.key_metrics import *

import collections
import numpy as np
import typing

from scipy.stats import norm

from configs.logger import Logger

logger = Logger(__name__).log


class TraderAlpha(object):
    def __init__(self, companies: list):
        """
        Constructor for a trading bot
        :param companies: list of companies to trade with
        :type companies: list
        """
        logger.info('Starting trade bot alpha to watch companies: {}'.format(companies))
        self.companies = companies
        self.correlation_matrix = formulas.calculate_correlation(companies)
        self.stocks_data = formulas.get_stocks_data(companies)

        self.correlation_map = collections.defaultdict(dict)

        self.benchmark_returns = None
        self.set_benchmark()

        self.pair_trader = None

        self.correlation_threshold = CORRELATION_THRESHOLD

    def _rank_correlations(self):
        for company in list(self.correlation_matrix):
            self.correlation_map[company] = self.correlation_matrix[company]\
                .sort_values(ascending=False).to_dict()
        self._clean_up_correlation_map()

    def _clean_up_correlation_map(self):
        for key, item in self.correlation_map.items():
            if key in item.keys():
                del item[key]

    def compute_correlation_pairs_for_trading_strategy(self) -> typing.List[tuple]:
        """
        Compute which companies closely relate to each other to perform pair trading with
        """
        results = set()
        self._rank_correlations()
        self._clean_up_correlation_map()
        logger.info('Computing correlation pairs from correlation map: {}'.format(self.correlation_map))
        for primary_index, sorted_index_correlation_dict in self.correlation_map.items():
            # in Python, dict.keys() always return same order if dict is not altered
            secondary_index = list(sorted_index_correlation_dict.keys())[0]
            if sorted_index_correlation_dict[secondary_index] <= self.correlation_threshold:
                continue
            index_tuple = (primary_index, secondary_index) if primary_index < secondary_index else \
                (secondary_index, primary_index)
            results.add(index_tuple)
        correlation_pairs = list(results)
        logger.info('Finished computing correlation pairs, result is: {}'.format(correlation_pairs))
        return correlation_pairs

    def set_benchmark(self, benchmark_index='SPY') -> None:
        """
        Set benchmark for bot to use. By default use S&P 500

        :param benchmark_index: index to use
        :type benchmark_index: str
        """
        logger.info('Set {} as benchmark to measure performance'.format(benchmark_index))
        self.benchmark_returns = formulas.calculate_percentage_change_based_on_adjusted_closing_price(benchmark_index)

    def perform_pair_trading(self,
                             comp_a: str,
                             comp_b: str,
                             start: str=datetime_helpers.get_current_date_some_year_ago_str(5),
                             end: str=datetime_helpers.get_current_date_str()) -> float:
        """
        Generate threshold value for a trade signal

        :param comp_a: company a index
        :type comp_a: str
        :param comp_b: company b index
        :type comp_b: str
        :param start: start date to analyse
        :type start: str
        :param end: end date to analyse
        :type end: str
        :return: threshold value
        :rtype: float
        """

        self.pair_trader = PairsTrading(comp_a, comp_b, start, end)
        threshold = self.pair_trader.generate_threshold()
        return threshold

    def perform_backtest(self) -> None:
        """
        Perform backtest
        """
        if self.pair_trader:
            backtest = Backtest(self.pair_trader)
            backtest.perform_backtest()


    @staticmethod
    def calculate_sharpe_ratio(daily_returns: np.array, time_period: int=TRADING_DAYS_IN_A_YEAR) -> float:
        """
        Calculate Sharpe ratio

        :param daily_returns: returns
        :type daily_returns: np.array
        :param time_period: time period to roll
        :type time_period: int
        :return: Sharpe ratio
        :rtype: float
        """
        return np.mean(daily_returns)/np.std(daily_returns) * np.sqrt(time_period)

    @staticmethod
    def calculate_shortino_ratio(daily_returns: np.array, time_period: int=TRADING_DAYS_IN_A_YEAR) -> float:
        """
        Calculate shortino ratio.

        The Sortino ratio is similar to the Sharpe ratio but it only regards the standard deviation of the negative
        returns. This avoids being penalised for excessive positive returns as it is the case for the Sharpe ratio and
        it may in some cases be a better metric.

        :param daily_returns: returns values
        :type daily_returns: np.array
        :param time_period: time period to roll back to
        :type time_period: int
        :return: Shortino ratio
        :rtype: float
        """
        return np.mean(daily_returns)/np.std(daily_returns[daily_returns<0])*np.sqrt(time_period)

    @staticmethod
    def calculate_drawdown(ret: np.array) -> float:
        """
        Calculate drawdown

        :param ret: returns array
        :type ret: np.array
        :return: drawdown
        :rtype: float
        """
        cum_ret = np.cumprod(ret + 1)
        running_max = np.fmax.accumulate(cum_ret)
        # Ensure the value never drops below 1
        running_max[running_max < 1] = 1

        d = cum_ret / running_max - 1
        return d

    @staticmethod
    def calculate_VaR(P: float, c: float, lkbk: int, rets: np.array) -> float:
        """
        Calculate Value at Risk (VaR)

        VaR measures how much the investor might lose in a single day (or month, or year), in a worst case scenario,
        given a specified confidence interval, usually 95% or 99%.

        :param P: portfolio value
        :type P: float
        :param c: confidence interval
        :type c:float
        :param lkbk: lookback window
        :type lkbk: int
        :param rets: returns
        :type rets: np.array
        :return: VaR
        :rtype: float
        """
        mu = np.mean(rets[-lkbk:])
        sigma = np.std(rets[-lkbk:])
        alpha = norm.ppf(1 - c, mu, sigma)

        result = round(P - P * (alpha + 1))
        print('With {} confidence, we expect that our worst daily loss will not exceed ${} on our ${} portfolio.'.
              format(c, result, P))
        return result


if __name__ == '__main__':
    trading_bot = TraderAlpha(['CBA.AX', 'MSFT', 'TSLA', 'AMZN'])
    trading_bot.compute_correlation_pairs_for_trading_strategy()
    # trading_bot.perform_pair_trading('CBA.AX', 'MSFT')
    # trading_bot.pair_trader.generate_trading_signal_plot()
