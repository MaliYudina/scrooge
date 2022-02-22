"""
Gets user input with tickers transactions (manual input by user in case if broker does not have API)
"""
import csv
import json
import logging
import os
from extra_features.news import show_news
from user_work.user_profile import show_portfolio
from moex_api.get_coupons import get_coupons

current_dir = os.path.abspath(os.path.dirname(__file__))


INPUT_CSV = os.path.join(current_dir, "user_input.csv")
OUTPUT_JSON = os.path.join(current_dir, "json_input.json")
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger('get_user_input')


def ask_input():
    print("-- Let's start investing. Please choose option: --")
    choice_number = input(
        "Add transactions : 1\n"
        "Show my portfolio : 2\n"
        "Check coupons transactions : 3\n"
        "Read news : 4\n"
    )

    # проверить как использовать указатель на функцию
    options_choice = {'1': add_transactions,
                      '2': show_portfolio,
                      '3': get_coupons,
                      '4': show_news,
                      }
    print(choice_number)
    func_pointer = options_choice[choice_number]
    return func_pointer


def caller():
    ask_input()()


def add_transactions(csv_file, json_file):
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
    with open(json_file, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    LOG.info("2. CSV file successfully received!",)
    return data


def upload_list():
    with open(INPUT_CSV, encoding='UTF-8') as file:
        LOG.info("3. Start writing down user input into csv file", )
        file_data = csv.DictReader(file)
        tickers_list = []
        for col in file_data:
            tickers_list.append(col['ticker'])
    LOG.info("4. Successfully written down", )
    return tickers_list


def broker_authorization():
    pass
#


caller()
# add_transactions(csv_file=INPUT_CSV, json_file=OUTPUT_JSON)

