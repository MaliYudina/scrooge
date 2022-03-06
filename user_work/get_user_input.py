"""
Gets user input with tickers transactions (manual input by user in case if broker does not have API)
"""
import csv
import json
import logging
import os
from extra_features.news import show_news
from db_work.portfolio_db import show_portfolio
from moex_api.get_coupons import get_coupons
from extra_features.show_graph import show_graph

current_dir = os.path.abspath(os.path.dirname(__file__))


INPUT_CSV = os.path.join(current_dir, "add_transactions_template.csv")
OUTPUT_JSON = os.path.join(current_dir, "transactions_json.json")
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger('get_user_input')


def ask_app_options():
    """
    ask_input function gives the logged user choice of further actions,
    such as checking portfolio or adding some new data
    :return:
    """
    print("-- Let's start investing. Please choose option: --")
    option_number = input(
        "Add transactions : 1\n"
        "Show my portfolio : 2\n"
        "Check coupons transactions : 3\n"
        "Read news : 4\n"
    )
    options_choice = {'1': add_new_transactions,
                      '2': show_portfolio,
                      '3': get_coupons,
                      '4': show_news,
                      '5': show_graph,
                      }
    print("Your choice: ", option_number)
    func_pointer = options_choice[option_number]
    return func_pointer


def caller():
    ask_app_options()()


def add_new_transactions(csv_file, json_file):
    """
    Пользователь загружает csv файл с новыми транзакциями,
    которые будут добавлены в базу со всеми Транзакциями
    v 2.0 - ввод будет не через csv файл, а телеграм бот (строка, тапл)
    формат записи:
    user_email,ticker,trans_type,type_code,date,cur,qty,price
    user_email добавляется автоматически, когда пользователь залогинен

    файл CSV преобразуется в JSON


    :param csv_file: CSV file uploaded by the user
    :param json_file: JSON file name to write down data from received CSV
    :return:
    """
    data = []
    with open(csv_file, encoding='utf-8') as csvf:
        LOG.info("1. Start uploading user's csv file...", )
        csv_reader = csv.DictReader(csvf)
        for row in csv_reader:
            data.append(row)
            print(row)
    with open(json_file, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    LOG.info("2. CSV file successfully received!",)
    return data


add_new_transactions(csv_file=INPUT_CSV, json_file=OUTPUT_JSON)


def upload_list():
    with open(INPUT_CSV, encoding='UTF-8') as file:
        LOG.info("3. Start writing down user input into csv file", )
        file_data = csv.DictReader(file)
        tickers_list = []
        for col in file_data:
            tickers_list.append(col['ticker'])
    LOG.info("4. Successfully written down", )
    print(tickers_list)
    return tickers_list

upload_list()

def broker_authorization():
    """
    Потом как нибудь реализую авторизацию у Тинькова
    :return:
    """
    pass
