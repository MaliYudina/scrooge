"""
Get coupons module requests data for dividends or coupons for an instrument
Returns the sum and dates of received and planned dividends/coupons
"""
import requests
import json
import logging
from db_work.db_update import get_tickers_data_for_dividends
file_format = 'json?'
filename = 'coupons.json'
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger('get_coupons')


def prepare_transactions_data(div_data):
    """
    extract ticker name, date, qty from list of tuples received from DB Transactions
    :param div_data:
    :return:
    """
    tickers_list = []
    for d in div_data:
        if d[0] not in tickers_list:
            tickers_list.append(d[0])
    print(tickers_list)
    return tickers_list


def loop_for_get_coupons(ticker_list):
    for t in ticker_list:
        print("start get coupons for ", t)
        get_coupons(secid=t)


def get_coupons(secid) -> list:
    """
    Requests coupons and dividends date and sum payment, starting from purchase date
    Purchase date is diffferent for certain purchase lot !!!
    :param secid:
    :return: dict of dividends
    """
    LOG.info("1. Start get_coupons...", )
    request_url = 'http://iss.moex.com/iss/securities/{}/dividends.{}&iss.meta=off'.format(
        secid, file_format)
    response = requests.get(request_url)
    response.raise_for_status()  # raises exception when not a 2xx response
    if response.status_code == 200:
        print("Ok, Response 200")
    coupons_data = response.json()  # <class 'dict'>
    coupons = coupons_data['dividends']['data']
    # [
    # 		["SBER", "RU0009029540", "2019-06-13", 16, "RUB"],
    # 		["SBER", "RU0009029540", "2020-10-05", 18.7, "RUB"],
    # 		["SBER", "RU0009029540", "2021-05-12", 18.7, "RUB"]
    # 	]
    print(coupons)
    return coupons


def sum_coupons(coupons_data, date_start_and_qty):
    """
    из БД транзакции достаем пару и считаем с какой даты сколько начислять дивидендов
    :param coupons_data:
    :param date_start_and_qty:
    :return:
    """
    # дата покупки лота, количество акций в лоте
    date_qty = [['10-03-2021', 10],
               ['05-10-2021', 3],
               ['01-10-2020', 7]]

    # дата выплата купонов, сумма выплаты по одному купону
    coupons_data = [['YNDX', '15-03-2021', 21],
                    ['YNDX', '15-10-2021', 7],
                    ['YNDX', '15-10-2020', 7]]
    coupons_data_dates = ['05-03-2021', '15-10-2021', '15-10-2020']

    purchase_dates = []
    for d in date_qty:
        purchase_dates.append(d[0])
    print(purchase_dates)
    nums = [x for x in coupons_data_dates]
    print(nums)

    for d in purchase_dates:
        if d < '15-10-2020':
            print(d, '!!!', 'ok')


tickers = prepare_transactions_data(div_data=get_tickers_data_for_dividends())
loop_for_get_coupons(ticker_list=tickers)

# get_coupons('SBER')
# get_coupons('ROSN')
# get_coupons('GMKN')


date_qty = ('15-03-2021', 10)
coupons_data = [['YNDX', '15-03-2021', 21],
                ['YNDX', '15-10-2021', 7],
                ['YNDX', '15-10-2020', 7]]
sum_coupons(coupons_data, date_qty)