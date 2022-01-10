"""
DB_update module creates DB and updates the values for received tickers
"""

import sqlite3
from sqlite3 import Error
import os
from parse_ticker import read_json, filter_response, get_json_from_moex

BASE_DIR = os.path.join(os.getcwd())
db_file = os.path.join(BASE_DIR, 'sql_investor.db')
print(db_file)


def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def create_table_tickers(connection):
    """
    Table Tickers stores all the tickers ever bought by the investor. Ticker code and ID should unique
    Ticker ID helps to join transactions and prices history
    :param connection:
    :return:
    """
    try:
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS Tickers (
                                    _id INTEGER PRIMARY KEY,
                                    ticker TEXT NOT NULL UNIQUE,
                                    name text NOT NULL);'''
        cursor = connection.cursor()
        print("Successfully Connected to SQLite DB")
        cursor.execute(sqlite_create_table_query)
        connection.commit()
        print("SQLite table 'TICKERS' successfully created!")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table ('Tickers' table)", error)
    finally:
        if connection:
            connection.commit()


def update_values_tickers(ticker_data, connection):
    try:
        cursor = connection.cursor()
        print("Connected to SQLite DB")

        sqlite_insert_query = """INSERT OR IGNORE INTO Tickers
                              (ticker, name)
                              VALUES (?, ?);"""

        ticker = ticker_data['SECID']
        name = ticker_data['SHORTNAME']
        record_list = [('GAZP-3', 'Gazprom3'),
                       ('TCSG', 'Tinkoff'),
                       # ('VISA', 'Visa card'),
                       # ('YNDX', 'Yandex')
                       ]
        cursor.executemany(sqlite_insert_query, record_list)
        connection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into TICKERS table")
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table TICKERS", error)
    finally:
        if connection:
            connection.commit()


def create_table_history_prices(connection):
    """
        Table History prices stores daily prices for each ticker.
        Period of prices starts from purchase date, ends by today date.
        Daily prices are used for analysis
        :param connection:
        :return:
        """
    try:
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS Prices (
                                    _id INTEGER PRIMARY KEY,
                                    ticker VARCHAR(30) NOT NULL,
                                    name text NOT NULL,
                                    date datetime,
                                    price DECIMAL NOT NULL);'''
        cursor = connection.cursor()
        print("Successfully Connected to SQLite DB")
        cursor.execute(sqlite_create_table_query)
        connection.commit()
        print("SQLite table PRICES successfully created!")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table (PRICES table)", error)
    finally:
        if connection:
            connection.commit()


def update_values_history_prices(connection):
    try:
        cursor = connection.cursor()
        print("Connected to SQLite DB")

        sqlite_insert_query = """INSERT INTO Prices
                              (ticker, name, date, price)
                              VALUES (?, ?, ?, ?);"""

        prices_data_sample = [('SBER', 'Sberbank', '2019-05-15', 7600.20),
                              ('SBER', 'Sberbank', '2019-05-16', 7600.80),
                       ('VISA', 'Visa card', '2019-03-28', 84.1),
                       ('VISA', 'Visa card', '2019-03-27', 84.0)]

        prices_data = prices_data_sample
        cursor.executemany(sqlite_insert_query, prices_data)
        connection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into PRICES table")
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table PRICES", error)
    finally:
        if connection:
            connection.commit()


def create_table_transactions(connection):
    """
        Table Transactions stores all the buy & sell history.
        User inputs manually (if not Tinkoff api)
        Commissions for transactions, tickers dividends / coupons are stored as well.
        This data helps to calculate taxes.
        :param connection:
        :return:
        """
    try:
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS Transactions (
                                    _id INTEGER PRIMARY KEY,
                                    ticker TEXT NOT NULL,
                                    type TEXT NOT NULL,
                                    type_code INTEGER NOT NULL,
                                    date datetime,
                                    currency TEXT NOT NULL,
                                    price REAL NOT NULL);'''
        cursor = connection.cursor()
        print("Successfully Connected to SQLite DB")
        cursor.execute(sqlite_create_table_query)
        connection.commit()
        print("SQLite table 'TRANSACTIONS' successfully created!")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table ('TRANSACTIONS' table)", error)
    finally:
        if connection:
            connection.commit()


def update_values_transactions(connection):
    try:
        cursor = connection.cursor()
        print("Connected to SQLite DB")

        sqlite_insert_query = """INSERT INTO Transactions
                              (ticker, type, type_code, date, currency, price)
                              VALUES (?, ?, ?, ?, ?, ?);"""

        update_data_sample = [
                              ('SBER', 'commission', 5, '2019-05-15', 'RUB', -700.20 * 0.03),
                              ('SBER', 'sell', 2, '2019-05-20', 'RUB', 780.20),
                              # ('SBER', 'commission', 5,  '2019-05-15',  'RUB', -780.20 * 0.03),
                              # ('YNDX', 'buy', 1, '2019-05-15', 'RUB', 7700.20),
                              # ('YNDX', 'commission', 5,  '2019-05-15', 'RUB',  7700.20 * 0.03),
                              # ('SBER', 'dividend',  '2019-05-15', 'RUB', 10.20),
                              # ('no', 'month_fee', 6,  '2019-05-15', 'RUB', -177.00)
            ]

        update_data = update_data_sample

        cursor.executemany(sqlite_insert_query, update_data)
        connection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into TRANSACTIONS table")
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table TRANSACTIONS", error)
    finally:
        if connection:
            connection.commit()


def read_db():
    cursor = connection.cursor()
    cursor.execute("SELECT * from Tickers")
    result = cursor.fetchall()

    print("DB content Tickers: ")
    for r in result:
        print(r)


connection = create_connection()

create_table_tickers(connection)
create_table_transactions(connection)
create_table_history_prices(connection)


update_values_tickers(ticker_data=filter_response(value_dict=read_json(content_dict=get_json_from_moex())),
                      connection=connection)
update_values_transactions(connection=connection)
update_values_history_prices(connection=connection)

read_db()
