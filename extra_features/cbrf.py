"""
News module aggregates news for tickers in portfolio
User may filter the list of required news, add, rate, set notifications to Telegram
"""

import requests


def get_currency_rates():
    all_rates = requests.get("http://iss.moex.com/iss/statistics/engines/currency/markets/selt/rates.json?")
    all_rates = all_rates.json()
    all_rates = all_rates['cbrf']['metadata']
    all_rates_values = dir(all_rates)
    print(all_rates_values)


get_currency_rates()
