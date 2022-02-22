"""
News module aggregates news for tickers in portfolio
User may filter the list of required news, add, rate, set notifications to Telegram
"""

import requests
# from bs4 import BeautifulSoup


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


def show_news():
    r = requests.get('https://quote.rbc.ru/?utm_source=topline')
    parsed_string = r.text
    # soup = BeautifulSoup(parsed_string, "html.parser")
    # news = soup.text[0:100]
    fake_news = "some normal news will be here"
    print(fake_news)
    return fake_news
