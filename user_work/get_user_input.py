"""
Gets user input with tickers transactions (manual input by user in case if broker does not have API)
"""
import csv
import json
import logging

INPUT_CSV = "user_input.csv"
OUTPUT_JSON = "json_input.json"
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger('get_user_input')


def input_to_json(csv_file, json_file):
    """
    Manual input by user : received through csv or inline input from telegram
    :param csv_file:
    :param json_file:
    :return:
    """
    data = []
    with open(csv_file, encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)
        for row in csv_reader:
            data.append(row)
    with open(json_file, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    LOG.info("1. User input successfully received",)
    return data


def upload_list():
    with open(INPUT_CSV, encoding='UTF-8') as file:
        file_data = csv.DictReader(file)
        tickers_list = []
        for col in file_data:
            tickers_list.append(col['ticker'])
    return tickers_list


def broker_authorization():
    pass


upload_list()
input_to_json(csv_file=INPUT_CSV, json_file=OUTPUT_JSON)
