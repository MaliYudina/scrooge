import os
import sqlite3
from sqlite3 import Error

from log_work.log_setup import setup_logger
logger = setup_logger()
logger.info('db_connection.py start')
LOGGER = logger

current_dir = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(current_dir, 'sql_investor.db')


def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        LOGGER.info("Connection to SQLite DB successful")
    except Error as e:
        LOGGER.error(f"The error '{e}' occurred")

    return connection


if __name__ == "__main__":
    create_connection()
