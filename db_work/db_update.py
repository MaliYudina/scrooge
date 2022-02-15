"""
DB_update module creates DB and updates the values for received tickers
"""
from user_work import login
import sqlite3
from sqlite3 import Error
import os
from user_work.read_json import read_json

current_dir = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(current_dir, 'sql_investor.db')
print(db_file)

json_file_path = '/Users/mali/PycharmProjects/investor/user_work/json_input.json'
transactions_list = read_json(json_file_path)


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
    try:
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS Transactions (
                                    user_name TEXT NOT NULL,
                                     _id INTEGER PRIMARY KEY,
                                     ticker TEXT NOT NULL,
                                     trans_type TEXT NOT NULL,
                                     type_code NOT NULL,
                                     date NOT NULL,
                                     cur TEXT NOT NULL,
                                     qty NOT NULL,
                                     price REAL NOT NULL,
                                     total_price NOT NULL,
                                     commission NOT NULL,
                                     est_taxes INTEGER DEFAULT 0);'''
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


def update_values_transactions(connection, transactions):
    try:
        cursor = connection.cursor()
        print("Connected to SQLite DB")

        sqlite_insert_query = """INSERT INTO Transactions
                               (user_name, ticker, trans_type, type_code, date, cur, qty, 
                               price, total_price, commission, est_taxes)
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        comm_rate = 0.03
        tax_base = 0.13
        choose_type_code = {'buy': 1,
                            'sell': 2,
                            'commission': 3}

        for line in transactions_list:
            user_name = "test_user"
            ticker = line['ticker']
            trans_type = line["trans_type"]
            type_code = choose_type_code.get(trans_type)
            date = line['date']
            cur = 'rub'
            qty = int(line['qty'])
            price = float(line['price'])
            total_price = qty * price
            commission = total_price * comm_rate
            est_taxes = total_price * tax_base

            update_data_sample = (user_name, ticker, trans_type, type_code, date, cur, qty,
                              price, total_price, commission, est_taxes)
            cursor.execute(sqlite_insert_query, update_data_sample)
            connection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into TRANSACTIONS table")
        # cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table TRANSACTIONS", error)
    finally:
        if connection:
            connection.commit()


def create_table_user(connection):
    """
        Table Transactions stores all the buy & sell history.
        User inputs manually (if not Tinkoff api)
        Commissions for transactions, tickers dividends / coupons are stored as well.
        This data helps to calculate taxes.
        :param connection:
        :return:
        """
    try:
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS Users (
                                    _id INTEGER PRIMARY KEY,
                                    email TEXT UNIQUE,
                                    name TEXT NOT NULL,
                                    surname TEXT NOT NULL,
                                    password TEXT NOT NULL, 
                                    broker_name TEXT NOT NULL,
                                    date_joined datetime);'''
        # ('test@email.ru', 'kate', 'smirnova', 'kat123', 'Finam', '2022-02-15')
        cursor = connection.cursor()
        print("Successfully Connected to SQLite DB")
        cursor.execute(sqlite_create_table_query)
        connection.commit()
        print("SQLite table 'USERS' successfully created!")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table ('USERS' table)", error)
    finally:
        if connection:
            connection.commit()


def update_values_user(connection, user_data):
    try:
        cursor = connection.cursor()
        print("Connected to SQLite DB")

        sqlite_insert_query = """INSERT OR IGNORE INTO Users
                              (email, name, surname, password, broker_name, date_joined)
                              VALUES (?, ?, ?, ?, ?, ?);"""

        # update_data_sample = [
        #     ('Petr', 'Ivanov', 'mail@mail.ru', '2019-05-15', 'Finam'),
        #     ('Ivan', 'Petrof', 'inbox@mail.ru', '2020-06-10', 'Tinkoff, Finam'),
        #     ('Katya', 'Smirnova', 'ya@mail.ru', '2021-10-20', 'Finam'),
        #     ('Lena', 'Smith', 'yandex@mail.ru', '2021-10-20', 'Otkritie'),
        # ]

        cursor.execute(sqlite_insert_query, user_data)
        connection.commit()
        print("Total", cursor.rowcount, "records inserted successfully into USERS table")
        print("Inserted data: ", user_data)
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert record into sqlite table USERS", error)
    finally:
        if connection:
            connection.commit()


def join_user_transactions(connection):
    """
    Table that joins registered user and their transactions
    :return:
    """
    # Transactions columns : (user_name, ticker, trans_type, type_code, date, cur, qty,
    #                                price, total_price, commission, est_taxes)
    search_name = 'Ivan'
    search_name_set = (search_name,)
    cursor = connection.cursor()
    cursor.execute("""SELECT name, broker_name, ticker, date, total_price 
    FROM Users 
    INNER JOIN Transactions on Transactions.user_name = Users.name 
    WHERE Users.name=?""", search_name_set)
    # TODO я передаю строчку, а принимает set, поэтому конфликт, надо строку запихнуть в set ('Ivan',)
    join = cursor.fetchall()
    print(f"Joined table Users and Transactions for name {search_name}:")
    print(join)


def calculations():
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(commission) FROM Transactions;")
    result = cursor.fetchall()

    print("All commissions: ", result)


def read_users_table():
    cursor = connection.cursor()
    cursor.execute("SELECT * from Users")
    result = cursor.fetchall()

    print("DB content Users: ")
    for r in result:
        print(r)


def read_login_pass_users():
    cursor = connection.cursor()
    search_login = 'mail@mail.ru'
    search_login_set = (search_login,)
    cursor.execute("""SELECT name, surname, email 
        FROM Users
        WHERE Users.email=?""", search_login_set)
    cursor.execute("SELECT * from Users")
    login_result = cursor.fetchone()
    print("User name: ", login_result)
    return login_result



connection = create_connection()

# create_table_tickers(connection)
# update_values_tickers(ticker_data=filter_response(value_dict=read_json(content_dict=get_json_from_moex())),
#                       connection=connection)

# create_table_transactions(connection)
# update_values_transactions(connection=connection, transactions=transactions_list)

# create_table_history_prices(connection)
# update_values_history_prices(connection=connection)
create_table_user(connection=connection)
update_values_user(connection=connection, user_data=login.register_user())
# join_user_transactions(connection=connection)

# read_db()
# calculations()
read_users_table()
# read_login_pass_users()