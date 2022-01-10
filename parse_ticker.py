"""
Parse_ticker module finds data for a ticker
or a list of tickers received from web form or uploaded list
"""
import requests
import json
import pandas as pd
from get_tickers import upload_list
from pprint import pprint
import sqlite3
from sqlite3 import Error
import os
from get_tickers import upload_list

BASE_DIR = os.path.join(os.getcwd())
print(BASE_DIR)

filename = "raw_data.json"
url_ticker_spec = "https://iss.moex.com/iss/securities.xml?q="
url_ticker_price = "https://iss.moex.com/iss/engines/stock/markets/shares/securities/"


def get_json_from_moex():
    """
    Download raw json content from MOEX
    :return: json format file
    """
    ticker_list = upload_list()
    print(type(ticker_list))
    print(ticker_list)
    ticker_list2 = ['ROSN', 'LKOH']
    file_format = 'json'
    for t in ticker_list:
        request_url = 'https://iss.moex.com/iss/engines/stock/markets/shares/securities/{}.{}'.format(
            t, file_format)
        # TODO !!! если в конце слеш, то формат XML
        print(request_url)
    # TODO убрать слэш в конце урла (если не прописывать стрингом, то автомтически добавляется) .strip("/")
        response = requests.get(request_url)
        print(response)  # <Response [200]>
        response.raise_for_status()  # raises exception when not a 2xx response
        if response.status_code == 200:
            print("Ok, Response 200")
        content_dict = response.json()  # <class 'dict'>

        with open(filename, 'w') as f:
            json.dump(content_dict, f)
        f.close()
        return content_dict


def read_json(content_dict):
    """
    Read JSON file as a dict data, extract the necessary ticker info
    :param content_dict:
    :return: dictionary
    """
    with open(filename, 'r') as f:
        raw_json_string = f.read()
        raw_json = json.loads(raw_json_string)  # TODO наверное надо убрать чтение файла, это лишнее
    print(type(raw_json))

    headers = content_dict['securities']['columns']
    print("HEADERS:")
    print(headers)

    header_values = content_dict['securities']['data']
    print(header_values)
    header_values = header_values[0]

    value_dict = {key: value for key, value in zip(headers, header_values)}
    pprint(value_dict)
    filter_keys_list = ['ISIN', 'SECID', 'LATNAME', 'SHORTNAME',
                        'SECNAME', 'PREVDATE', 'PREVPRICE', 'LOTSIZE']
    value_dict_filtered = {}
    for key, value in value_dict.items():
        if key in filter_keys_list:
            value_dict_filtered[key] = value

    pprint(value_dict_filtered)

    return value_dict


def create_pandas_df():
    df = pd.read_json("raw_data.json")
    print(df)


value_dict = read_json(content_dict=get_json_from_moex())
create_pandas_df()
