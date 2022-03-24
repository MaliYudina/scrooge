"""
Gets user input with tickers transactions (manual input by user in case if broker does not have API)
"""
import csv
import json
import logging
import os


current_dir = os.path.abspath(os.path.dirname(__file__))


INPUT_CSV = os.path.join(current_dir, "add_transactions_template.csv")
OUTPUT_JSON = os.path.join(current_dir, "transactions_json.json")
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger('get_user_csv')



def add_new_transactions():
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
        LOG.info("1. Reading user's CSV file {}".format(csv_file),)
        # LOG.info("1. Start uploading user's csv file...", )
        csv_reader = csv.DictReader(csvf)
        for row in csv_reader:
            data.append(row)

    with open(json_file, 'w', encoding='utf-8') as jsonf:
        LOG.info("2. Start dump into json file {}".format(json_file), )
        jsonf.write(json.dumps(data, indent=4))
        LOG.info("2. End dump into json file {}".format(json_file), )
    LOG.info("2. CSV file successfully dumped into JSON file!",)

    with open(json_file, 'r') as jsonf:
        LOG.info("3. Read json file {}".format(OUTPUT_JSON), )
        json_str = jsonf.read()
        list_dump = json.loads(json_str)
    print("Transactions added: {}".format(len(list_dump)))
    # print(list_dump)
    # for l in list_dump:
    #     print(l)
    LOG.info("4. Extract data as dict", )
    return list_dump


if __name__ == "__main__":
    add_new_transactions()
