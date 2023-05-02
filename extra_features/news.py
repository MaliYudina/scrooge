"""
News module aggregates news for tickers in portfolio
User may filter the list of required news, add, rate, set notifications to Telegram
"""

import requests
from requests.exceptions import ConnectTimeout
from bs4 import BeautifulSoup


def show_news():
    try:
        all_news = requests.get("http://iss.moex.com/iss/sitenews.json?", timeout=5)
        all_news = all_news.json()
        all_news = all_news['sitenews']['data']
        print(len(all_news))
        for a in all_news:
            print(a)
        return all_news
    except ConnectTimeout:
        header = {'Connection': 'keep-alive',
                  'Expires': '-1',
                  'Upgrade-Insecure-Requests': '1',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
                  }

        all_news = requests.get("https://finance.yahoo.com/news/", headers=header)
        soup = BeautifulSoup(all_news.text, 'lxml')
        all_news = soup.text
        print(all_news)
    #
    #
    # else:
    #     print("No Error")
    # finally:
    #     no_news_result = 'sorry, news not awailable'
    #     return no_news_result


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


