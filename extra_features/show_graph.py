"""
News module aggregates news for tickers in portfolio
User may filter the list of required news, add, rate, set notifications to Telegram
"""

import requests


def show_graph():
    """
    https://habr.com/en/post/495324/
    Получить историю по одной бумаге на рынке за интервал дат.
    :return:
    """
    base_url = 'http://iss.moex.com/'
    engine = 'stock'
    market = 'shares'
    session = ''
    boardid = 'TQBR'
    security = 'SBER'
    url = "http://iss.moex.com/iss/history/engines/{}/markets/{}/sessions/{}/securities/{}.json?".format(engine, market, session, security)
    url2 = 'http://iss.moex.com/iss/history/engines/stock/markets/shares/boards/tqbr/securities/SBER.json?meta=off&date=2022-01-01'
    print(url2)
    all_prices = requests.get(url2)

    all_prices = all_prices.json()
    print(all_prices)

show_graph()

