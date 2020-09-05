import numpy as np


class State:
    def __init__(self, data1, data2, bal_stock1, bal_stock2, open_cash, timestep):
        self.data1 = data1
        self.data2 = data2
        self.start_timestep = timestep
        self.start_bal_stock1 = bal_stock1
        self.start_bal_stock2 = bal_stock2
        self.start_open_cash = open_cash
        self.timestep = timestep
        self.stock_one_price = data1[timestep]  # stock 1 open price
        self.stock_two_price = data2[timestep]  # stock 2 open price
        self.stock_one_balance = bal_stock1  # stock 1 balance
        self.stock_two_balance = bal_stock2  # stock 2 balance
        self.open_cash = open_cash  # cash balance
        self.fiveday_stock1 = self.five_day_window(data1, timestep)
        self.fiveday_stock2 = self.five_day_window(data2, timestep)
        self.portfolio_value = self.portfolio_value()

    def portfolio_value(self):
        v1 = self.stock_one_price * float(self.stock_one_balance)
        v2 = self.stock_two_price * float(self.stock_two_balance)
        v3 = float(self.open_cash)
        return v1 + v2 + v3

    def next_opening_price(self):
        return [self.data1[self.timestep + 1], self.data2[self.timestep + 1]]

    @staticmethod
    def five_day_window(data, timestep):
        step = timestep
        if step < 5:
            return data[0]

        stock_5days = np.mean(data[step - 5:step])
        return stock_5days

    def reset(self):
        self.stock_one_price = self.data1[self.start_timestep]
        self.stock_two_price = self.data2[self.start_timestep]
        self.stock_one_balance = self.start_bal_stock1
        self.stock_two_balance = self.start_bal_stock2
        self.open_cash = self.start_open_cash
        self.fiveday_stock1 = self.five_day_window(self.data1, self.start_timestep)
        self.fiveday_stock2 = self.five_day_window(self.data2, self.start_timestep)
        self.portfolio_value = self.portfolio_value()

    def get_state(self):
        res = [self.stock_one_price, self.stock_two_price, self.stock_one_balance,
               self.stock_two_balance, self.open_cash, self.fiveday_stock1,
               self.fiveday_stock2, self.portfolio_value()]
        return np.array([res])
