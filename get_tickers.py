"""
Gets list of all the tickers from users investment portfolio
"""
import csv

TICKERS_CSV = "my_tickers.csv"


def upload_list():
    with open(TICKERS_CSV, encoding='UTF-8') as file:
        file_data = csv.DictReader(file)
        tickers_list = []
        for col in file_data:
            tickers_list.append(col['ticker_name'])
    print(tickers_list)
    return tickers_list


def broker_authorization():
    pass


upload_list()
