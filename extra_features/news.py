"""
News module aggregates news for tickers in portfolio
User may filter the list of required news, add, rate, set notifications to Telegram
"""

import requests
# from bs4 import BeautifulSoup


def show_news():
    all_news = requests.get("http://iss.moex.com/iss/sitenews.json?")
    all_news = all_news.json()
    all_news = all_news['sitenews']['data']
    print(len(all_news))
    for a in all_news:
        print(a)
    return all_news


def get_tickers_list():
    pass


def set_rates():
    """
    rates, filter, choose source etc
    :return:
    """
    pass


def set_view():
    """
    set the headers, text length
    :return:
    """
    pass


def set_notifications():
    """
    email, telegram or something
    :return:
    """
    pass


