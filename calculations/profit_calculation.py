"""
Profit_calculation module shows the current portfolio price
"""

import numpy

# numpy.fv(rate, nper, pmt, pv, when='end')


all_transactions = [['MOEX', 2, 3400],
                    ['MOEX', 10, 3000],
                    ['SBER', 10, 1500],
                    ['AAPL', 5, 7490],
                    ['AAPL', 3, 5490],
                    ]


def update_current_price():
    for t in all_transactions:
        cost = t[2] * t[1]
        print(cost)
        # profit = cost - PURCHASE_PRICE посчитать сразу в баске
    pass


def profit():
    pass


def average_per_ticker():
    pass


update_current_price()