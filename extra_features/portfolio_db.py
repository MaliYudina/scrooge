"""
portfolio_db module creates DB and shows the current portfolio of a user"""

import sqlite3
from sqlite3 import Error
import os
BASE_DIR = os.path.join(os.getcwd())
db_file = os.path.join(BASE_DIR, '../sql_investor.db')
print(db_file)


def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def create_table_portfolio(connection):
    """
        Table Portfolio is a table joined of Transactions and User tables,
        updated with calculations and API requests
        :param connection:
        :return:
        """
    try:
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS Portfolio (
                                    _id INTEGER PRIMARY KEY,
                                    ticker TEXT NOT NULL,
                                    shortname TEXT NOT NULL,
                                    qty NOT NULL,
                                    avg_price_total REAL NOT NULL,
                                    cur TEXT NOT NULL,
                                    avg_price_total_rub REAL NOT NULL,
                                    dividend_total,
                                    dividend_percent_total,
                                    total_margin_rub,
                                    total_margin_percent,
                                    weight decimal);'''
        cursor = connection.cursor()
        print("Successfully Connected to SQLite DB")
        cursor.execute(sqlite_create_table_query)
        connection.commit()
        print("SQLite table 'Portfolio' successfully created!")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table ('Portfolio' table)", error)
    finally:
        if connection:
            connection.commit()


def update_values_transactions(connection):
    try:
        cursor = connection.cursor()
        print("Connected to SQLite DB")

        sqlite_insert_query = """INSERT INTO Transactions
                              (ticker, trans_type, type_code, date, cur, qty, 
                              price, total_price, commission, est_taxes)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

        connection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into Portfolio table")
        connection.commit()
        # cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table PORTFOLIO", error)
    finally:
        if connection:
            connection.commit()
