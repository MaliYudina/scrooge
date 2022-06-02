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


def url_constructor(secid):
    """
    Url_constructor makes working url using base url and options of engines and markets
    :param secid: string value of ticker
    :return: moex_url  - string value of url address

    /iss/engines/[engine]/markets/[market]/boards/[board]/securities/[security]
    Get data for the specified security on the specified board.

    /iss/engines/[engine]/markets/[market]/securities/[security]
    Get metadata and market data for the specified security on the specified market.
    Example: https://iss.moex.com/iss/engines/stock/markets/shares/securities/AFLT.xml?lang=en
    """
    engines = {1: "stock",
               2: "state",
               3: "currency",
               4: "futures",
               5: "commodity",
               6: "interventions",
               7: "offboard",
               9: "agro"
               }
    engine_value = engines.get(1)
    markets = {
        5: "index",
        1: "shares",
        2: "bonds",
        4: "ndm",
        29: "otc",
        27: "ccp",
        35: "deposit",
        3: "repo",
        28: "qnv",
        36: "mamc",
        47: "foreignshares",
        49: "foreignndm",
        33: "moexboard"
    }
    market_value = markets.get(1)
    security_value = secid

    moex_url = "http://iss.moex.com/iss/engines/{}/markets/{}/securities/{}.json?"\
        .format(engine_value, market_value, security_value)
    print(moex_url)
    example_url = "http://iss.moex.com/iss/engines/stock/markets/shares/securities/sber.json?iss.meta=off"

    return moex_url


url_constructor(secid='sber')


def get_secid_type(secid) -> str:
    """
    Get SECID specification from MOEX to resolve the type of the instrument, such as:
     - Common stock
     - Stock_etf
     - Exchange bond


    :param secid: string name of ticker
    :return: string name of instrument type
    """
    request_url = "https://iss.moex.com/iss/securities/{}.json?lang=en&iss.meta=off&iss.only=description".format(secid)
                  # "" \
                  # "https://iss.moex.com/iss/engines/stock/markets/shares/boards/" \
                  # "TQBR/securities/{}.json?iss.dp=comma&iss.meta=off&iss.only=securities&" \
                  # "description.columns=PREVADMITTEDQUOTE".format(secid)
    print(request_url)
    response = requests.get(request_url)
    spec = response.json()
    secid_type = spec['description']['data']
    for s in secid_type:
        # TODO ["TYPENAME", "Security type", "ETF", "string", 71, 0, null],
        # 		["GROUP", "Instrument type code", "stock_etf", "string", 72, 1, null],
        # 		["TYPE", "Security type", "etf_ppif", "string", 10000, 1, null],
        # 		["GROUPNAME", "Instrument type", "Exchange traded funds", "string", 10011, 1, null],
        if s[0] == 'TYPENAME':
            print(s)
            print(s[2])
            return s[2]


get_secid_type(secid='RU000A0ZZBN9')


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
    filename = "write_prices.json"
    with open(filename, 'w') as f:
        json.dump(coupons_data, f)
    f.close()
    LOG.info("3. Success dump json with coupons result ...", )
    return coupons_data
    # TODO возвращать список из списков?
    #  sample_coupon_answer = [['YNDX', '15-03-2021', 21], ['YNDX', '15-10-2021', 7]]


def get_market_price(secid) -> float:
    request_url = "https://iss.moex.com/iss/engines/stock/markets/shares/boards/" \
                  "TQBR/securities/{}.json?iss.dp=comma&iss.meta=off&iss.only=securities&" \
                  "securities.columns=PREVADMITTEDQUOTE".format(secid)
    print(request_url)
    response = requests.get(request_url)
    price = response.json()
    price_value = price['securities']['data'][0][0]
    # if IndexError:
    #     price_value = 0
    print(price_value)
    return price_value
    # print(response.json())  # <Response [200]>
# TODO сделать ссылку независимой от типа инструмента (если это ПИФ , то уже не работает)

# get_market_price(secid="VTBX")