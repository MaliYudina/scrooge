"""
Gets user input with tickers transactions (manual input by user in case if broker does not have API)
"""
import csv
import json
import logging
import os
from db_process.db_connection import create_connection
from db_process.db_update import update_values_transactions, update_values_tickers, \
    read_transactions_table, read_tickers_table
from moex_api.get_specification import get_secid_specification

current_dir = os.path.abspath(os.path.dirname(__file__))

INPUT_CSV = os.path.join(current_dir, "add_transactions_template.csv")
OUTPUT_JSON = os.path.join(current_dir, "transactions_json.json")
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger('get_user_csv')


def read_new_transactions():
    """
    Пользователь загружает свой csv файл с новыми транзакциями
    формат записи:
    user_email,ticker,trans_type,type_code,date,cur,qty,price
    user_email добавляется автоматически, когда пользователь залогинен
    файл CSV преобразуется в JSON

    v 2.0 - ввод будет не через csv файл, а телеграм бот (строка, тапл)

    :param csv_file: CSV file uploaded by the user
    :param json_file: JSON file name to write down data from received CSV
    :return:
    """
    data = []
    csv_file = INPUT_CSV
    json_file = OUTPUT_JSON
    with open(csv_file, encoding='utf-8') as csvf:
        LOG.info("1. Reading user's CSV file {}".format(csv_file), )
        csv_reader = csv.DictReader(csvf)
        for row in csv_reader:
            data.append(row)

    with open(json_file, 'w', encoding='utf-8') as jsonf:
        LOG.info("2. Start dump into json file {}".format(json_file), )
        jsonf.write(json.dumps(data, indent=4))
        LOG.info("2. End dump into json file {}".format(json_file), )
    LOG.info("2. CSV file successfully dumped into JSON file!", )

    with open(json_file, 'r') as jsonf:
        LOG.info("3. Read json file {}".format(OUTPUT_JSON), )
        json_str = jsonf.read()
        list_dump = json.loads(json_str)
    LOG.info("4. Extract data as dict", )
    LOG.info(f"Total added {len(list_dump)} transactions :")
    for l in list_dump:
        print(l)
    return list_dump


def add_new_transactions(new_transactions):
    user_name = 'mali_na'
    update_values_transactions(connection=create_connection(),
                               user_name=user_name,  # TODO здесь должно быть имя юзера после логина
                               transactions=new_transactions)


def update_tickers():
    """
    Add new ticker to Tickers table,
    if Transactions table has new unregistered ticker
    :return:
    """
    connection = create_connection()
    cursor = connection.cursor()
    # cursor.execute("SELECT DISTINCT ticker, date, qty from Transactions;")
    cursor.execute("SELECT Distinct Transactions.ticker "
                   "FROM Transactions "
                   "LEFT JOIN Tickers ON Transactions.ticker=Tickers.ticker;")
    secid = cursor.fetchall()
    for sec in secid:
        LOG.info('print(sec)')
        print(sec)
        update_values_tickers(connection=create_connection(),
                          ticker_data=get_secid_specification(sec[0]))


def call_add_new_transactions():
    add_new_transactions(new_transactions=read_new_transactions())
    update_tickers()


if __name__ == "__main__":
    LOG.info("get_user_csv.py __main__ started")
    # read_transactions_table()
    call_add_new_transactions()
    read_tickers_table()
