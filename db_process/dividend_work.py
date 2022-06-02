"""
Фильтруем новые тикеры, которые еще не записаны в таблицу Дивиденды
"""
import requests
import json
import logging
from .db_connection import create_connection



file_format = 'json?'
filename = 'coupons.json'
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger('dividend_work')
connection = create_connection()
"""
Делим логику на :
1. Фоновая проверка на новые выплаты по всем имеющимся облигациям и акциям в таблице Тикерс
заджойнить 1 и 2
2. Отрезолвить группировку по периодам покупки по каждому тикеру

3. начислить выплату в табличку портфолио
"""


def get_tickers_to_parse_dividends() -> list:
    """
    Выбираем все тикеры с проверкой уже записанных тикеров в табличку дивиденды
    Приоритетная таблица - тикеры (т.к. она обновляется сразу после записи новых транзакций)
    По новым тикерам идем получать расписание дивов
    """
    print('2. ------- Start get_tickers_to_parse_dividends ')
    cursor = connection.cursor()
    cursor.execute("SELECT Distinct Tickers.ticker "
                   "FROM Tickers "
                   "LEFT JOIN Dividends ON Tickers.ticker=Dividends.ticker "
                   "WHERE type='common_share' "
                   "ORDER BY Tickers.ticker;")
    joined_tickers = cursor.fetchall()
    print(joined_tickers)
    print('2. ------ End get_tickers_to_parse_dividends ')
    return joined_tickers


# def extract_new_tickers_to_dividends(tickers_list, dividends_list):
#     print('3. ------ Start extract_new_tickers_to_dividends ')
#     # оставляем только новые (пересечение))
#     only_new_items = list(set(dividends_list) - set(tickers_list))
#     print("only_new_items")
#     print(only_new_items)
#     print('3. ------ End extract_new_tickers_to_dividends ')
#     return only_new_items


def tickers_caller():
    # tickers = extract_new_tickers_to_dividends(
    #     tickers_list=filter_coupon_tickers(),
    #     dividends_list=get_tickers_to_parse_dividends()
    # )
    tickers = get_tickers_to_parse_dividends()
    return tickers


# def read_div_table():
#     cursor = connection.cursor()
#     cursor.execute("SELECT * from Dividends "
#                    "ORDER BY ticker, last_purch_date;")
#     div_table = cursor.fetchall()
#     for d in div_table:
#         print(d)


if __name__ == '__main__':
    tickers_caller()
