import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from utils.data.constants.column_headings import *


class StockVisualiser:
    def __init__(self, company: str, data: pd.DataFrame) -> None:
        self.company = company
        self.data = data

    def plot(self) -> None:
        x1 = np.array(self.data[DATE])
        y1 = self.data[OPEN]
        y1_2 = self.data[VOLUME]

        plt.title('{} Performance Over years'.format(self.company))
        plt.xlabel("Year")
        plt.ylabel("Price in $")
        plt.plot(x1, y1)

        ax2 = plt.twinx()
        color = 'tab:red'
        ax2.set_ylabel(VOLUME, color=color)  # we already handled the x-label with ax1
        ax2.plot(x1, y1_2, color=color)
        ax2.tick_params(axis='y', labelcolor=color)

        plt.show()
