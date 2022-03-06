"""
Get coupons module requests data for dividends or coupons for an instrument
Returns the sum and dates of received and planned dividends/coupons
"""
import requests
import json
import logging
file_format = 'json'
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger('get_prices')


def get_prices(secid, purchase_date):
    """

    :param secid:
    :return:
    """
    LOG.info("1. Start get_prices...", )
    limit = 'limit=100&start=0'
    today = '2022-01-01'
    base_url = "/iss/statistics/engines/stock/currentprices"
    request_url = 'http://iss.moex.com/iss/statistics/engines/stock/currentprices.json?'
    # http://iss.moex.com/iss/securities/ROSN/dividends.json?from=2017-01-01&iss.meta=off
        # "&limit=100&start=0&",
        # str('&'+'till=' + today))
    print(request_url)
    response = requests.get(request_url)
    print(response)  # <Response [200]>
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
    for c in coupons:
        print(c)  # ['SBER', 'RU0009029540', '2019-06-13', 16, 'RUB']
    LOG.info("2. Start dump json with coupons result ...", )
    with open(filename, 'w') as f:
        json.dump(coupons_data, f)
    f.close()
    LOG.info("3. Success dump json with coupons result ...", )
    return coupons_data
    # TODO возвращать список из списков?
    #  sample_coupon_answer = [['YNDX', '15-03-2021', 21], ['YNDX', '15-10-2021', 7]]


def get_market_price(secid):
    request_url = 'http://iss.moex.com/iss/statistics/engines/stock/markets.json?'
    print(request_url)
    response = requests.get(request_url)
    print(response)  # <Response [200]>
    pass

get_market_price(secid="SBER")