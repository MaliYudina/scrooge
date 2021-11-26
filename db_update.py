"""
DB_update module creates DB and updates the values for received tickers
"""

import sqlite3
from sqlite3 import Error
import os

BASE_DIR = os.path.join(os.getcwd())
db_file = os.path.join(BASE_DIR, 'SQL_Investor.db')
print(db_file)


def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def create_table(connection):
    try:
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS Tickers (
                                    id INTEGER PRIMARY KEY,
                                    ticker TEXT NOT NULL,
                                    name text NOT NULL,
                                    date datetime,
                                    price REAL NOT NULL);'''
        cursor = connection.cursor()
        print("Successfully Connected to SQLite DB")
        cursor.execute(sqlite_create_table_query)
        connection.commit()
        print("SQLite table 'Tickers' successfully created!")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if connection:
            connection.commit()
            print("Finally happened")


def update_values(connection):
    try:
        cursor = connection.cursor()
        print("Connected to SQLite DB")

        sqlite_insert_query = """INSERT or replace INTO Tickers
                              (id, ticker, name, date, price)
                              VALUES (?, ?, ?, ?, ?);"""
        record_list = [(4, 'YNDX', 'Yandex', '2019-01-14', 9500),
                       (5, 'SBER', 'Sberbank', '2019-05-15', 7600.200),
                       (6, 'VISA', 'Visa card', '2019-03-27', 84)]
        cursor.executemany(sqlite_insert_query, record_list)
        connection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into TICKERS table")
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table", error)
    finally:
        if connection:
            connection.commit()
            print("Finally happened")

def read_db():
    cursor = connection.cursor()
    cursor.execute("SELECT * from Tickers")
    result = cursor.fetchall()

    for r in result:
        print(r)





connection = create_connection()

create_table(connection)

record_list = [(4, 'Jos', 'jos@gmail.com', '2019-01-14', 9500),
                       (5, 'Chris', 'chris@gmail.com', '2019-05-15', 7600),
                       (6, 'Jonny', 'jonny@gmail.com', '2019-03-27', 8400)]

update_values(connection)
read_db()
