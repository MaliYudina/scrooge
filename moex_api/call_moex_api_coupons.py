"""
Get coupons module requests data for dividends or coupons for an instrument
Returns the sum and dates of received and planned dividends/coupons
"""
import requests
import json
from datetime import datetime, timedelta

from log_work.log_setup import setup_logger
logger = setup_logger()
logger.info('call_moex_api_coupons start')
LOGGER = logger

file_format = 'json?'
filename = 'coupons.json'

"""
Делим логику на :
1. Фоновая проверка на новые выплаты по всем имеющимся облигациям и акциям в таблице Тикерс
заджойнить 1 и 2
2. Отрезолвить группировку по периодам покупки по каждому тикеру

3. начислить выплату в табличку портфолио
"""


def get_share_divs_from_moex(secid) -> tuple:
    """
    Requests dividends for shares - date and sum payment, starting from purchase date
    Purchase date is diffferent for certain purchase lot !!!
    :param secid:
    :return: dict of dividends
    """
    LOGGER.info("1. Start get_coupons from MOEX API (get_share_divs_from_moex)...", )
    request_url = 'http://iss.moex.com/iss/securities/{}/dividends.{}&iss.meta=off'.format(
        secid, file_format)
    # print(request_url)
    response = requests.get(request_url)
    response.raise_for_status()  # raises exception when not a 2xx response
    coupons_data = response.json()  # <class 'dict'>
    coupons = coupons_data['dividends']['data']
    div_list_answer = []
    if len(coupons) == 0:
        print("No dividends for {}".format(secid))
        pass
    else:
        print("Dividends for {}:".format(secid))
        # pprint(coupons)
        for c in coupons:
            ticker = c[0]
            figi = c[1]  # moex has only isin
            reg_close_date = c[2]
            last_purch_date = datetime.strptime(reg_close_date, '%Y-%m-%d') - timedelta(days=3)
            fact_paym_date = 'n/a'
            cur = c[4]
            value = c[3]
            div_answer = (ticker, figi, str(last_purch_date), reg_close_date,
                          fact_paym_date, cur, value)
            # print(div_answer)
            div_list_answer.append(div_answer)
            # pprint(tuple(div_list_answer))
        return tuple(div_list_answer)

