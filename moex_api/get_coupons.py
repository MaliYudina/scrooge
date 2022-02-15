"""
Get coupons module requests data for dividends or coupons for an instrument
Returns the sum and dates of received and planned dividends/coupons
"""
import requests
import json
file_format = 'json'
filename = 'coupons.json'


def get_coupons(secid):
    """
    Requests coupons and dividends date and sum payment, starting from purchase date
    Purchase date is diffferent for certain purchase lot
    :param secid:
    :return:
    """
    date_from = '2019-01-01'
    limit = 'limit=100&start=0'
    request_url = 'http://iss.moex.com/iss/securities/{}/dividends.{}{}&iss.meta=off'.format(
        secid, file_format, str('?'+'from=2021-08-10'))
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

    with open(filename, 'w') as f:
        json.dump(coupons_data, f)
    f.close()
    return coupons_data
    # TODO возвращать список из списков?
    #  sample_coupon_answer = [['YNDX', '15-03-2021', 21], ['YNDX', '15-10-2021', 7]]


def sum_coupons(coupons_data, date_qty):
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




get_coupons('SBER')
date_qty = ('15-03-2021', 10)
coupons_data = [['YNDX', '15-03-2021', 21],
                ['YNDX', '15-10-2021', 7],
                ['YNDX', '15-10-2020', 7]]
sum_coupons(coupons_data, date_qty)