"""
This module opens csv template file and saves user input with transactions
"""

import csv
import logging
import os

current_dir = os.path.abspath(os.path.dirname(__file__))

INPUT_CSV = os.path.join(current_dir, "template.csv")
OUTPUT_JSON = os.path.join(current_dir, "transactions.json")
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger('create_template')


def popup_file():
    os.system("open /Users/mali/PycharmProjects/investor/user_work/csv_template.csv")

popup_file()