"""
DB_update module creates DB and updates the values for received tickers
"""
import sqlite3
from db_process.db_connection import create_connection
import logging
from config import read_file_user_name

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger('run_coupons_job')

connection = create_connection()
session_user_name = read_file_user_name()


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
        sqlite_insert_query = """INSERT OR IGNORE INTO Users
                              (email, name, surname, password, broker_name, date_joined)
                              VALUES (?, ?, ?, ?, ?, ?);"""
        cursor.execute(sqlite_insert_query, user_data)
        connection.commit()
        print("Data to insert: ", user_data)
        connection.commit()
        cursor.close()
        print("---- Successfully added to USERS Table! ----")
    except sqlite3.Error as error:
        print("Failed to insert record into sqlite table USERS", error)
    finally:
        if connection:
            connection.commit()


def create_table_transactions(connection):
    try:
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS Transactions (
                                    _id INTEGER PRIMARY KEY,
                                    user_email TEXT NOT NULL,   
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


def update_values_transactions(connection, user_name, transactions):
    try:
        cursor = connection.cursor()
        print("Connected to SQLite DB")
        sqlite_insert_query = """INSERT INTO Transactions
                               (user_email, ticker, trans_type, type_code, date, cur, qty, 
                               price, total_price, commission, est_taxes)
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        comm_rate = 0.03
        tax_base = 0.13
        choose_type_code = {'buy': 1,
                            'sell': 2,
                            'commission': 3}

        for line in transactions:
            user_email = session_user_name
            ticker = line['ticker']
            trans_type = line["trans_type"]
            type_code = choose_type_code.get(trans_type)
            if type_code == 2:
                qty = (int(line['qty'])) * -1
                price = (float(line['price'])) * -1
            else:
                qty = int(line['qty'])
                price = float(line['price'])
            date = line['date']
            cur = 'rub'
            total_price = qty * price
            commission = total_price * comm_rate
            est_taxes = total_price * tax_base

            update_data_sample = (user_email, ticker, trans_type, type_code, date, cur, qty,
                                  price, total_price, commission, est_taxes)
            cursor.execute(sqlite_insert_query, update_data_sample)

            connection.commit()
        print("Total", len(transactions), "records inserted successfully into TRANSACTIONS table")
        # cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table TRANSACTIONS", error)
    finally:
        if connection:
            connection.commit()


def create_table_dividends(connection):
    try:
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS Dividends (
                                     _id INTEGER PRIMARY KEY,
                                     user_id,
                                     ticker TEXT,
                                     ISIN TEXT,
                                     last_purch_date,
                                     reg_close_date, 
                                     fact_paym_date,
                                     cur,
                                     value,
                                     filtered_trans_id,
                                     div_paid,
                                     UNIQUE (user_id, ticker, ISIN, last_purch_date, reg_close_date, fact_paym_date, value)
                                     );'''
        cursor = connection.cursor()
        print("Successfully Connected to SQLite DB")
        cursor.execute(sqlite_create_table_query)
        connection.commit()
        print("SQLite table 'DIVIDENDS' successfully created!")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table ('DIVIDENDS' table)", error)
    finally:
        if connection:
            connection.commit()


def update_values_dividends(connection, dividends):
    try:
        cursor = connection.cursor()
        print("Connected to SQLite DB")

        sqlite_insert_query = """INSERT OR IGNORE INTO Dividends
                               (user_id, ticker, isin, 
                               last_purch_date, reg_close_date, fact_paym_date, 
                               cur, value, filtered_trans_id)
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""

        for line in dividends:
            user_id = 'sys'
            ticker = line[0]
            isin = line[1]
            last_purch_date = line[2]
            reg_close_date = line[3]
            fact_paym_date = line[4]
            cur = line[5]
            value = line[6]
            filtered_trans_id = ''
            update_data = (user_id, ticker, isin, last_purch_date,
                           reg_close_date, fact_paym_date, cur,
                           value, filtered_trans_id, )
            print(update_data)
            cursor.execute(sqlite_insert_query, update_data)
            connection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into DIVIDENDS table")
        # cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table DIVIDENDS", error)
    finally:
        if connection:
            connection.commit()


def update_dividends_values_paid(connection, secid, last_purch_date, start_date, end_date, div_paid_value):
    try:
        print(LOG.info('update_dividends_values_paid'))
        cursor = connection.cursor()
        print("Connected to SQLite DB. !!! update_dividends_values_paid")
        print(f"try execute {secid} / {last_purch_date} / {div_paid_value}")
        cursor.execute("""UPDATE Dividends
        SET div_paid = ?
        WHERE ticker == ?
        AND last_purch_date >= ?
        AND last_purch_date <= ?""", (div_paid_value, secid, start_date, end_date))
        result = cursor.fetchall()
        # TODO last_purch_date надо заменить - так как result_tickers = дивидендный период:
        #  tickers_result for 2014 - 06 - 14 00: 00: 00 / 2015 - 06 - 12 00: 00:00. Total 5
        print(result)
        # cursor.execute(sqlite_insert_query, update_data)
        connection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into DIVIDENDS table")
        # cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table DIVIDENDS", error)
    finally:
        if connection:
            connection.commit()


def update_dividends_filtered_trans_id(connection, secid, last_purch_date, trans_id, div_paid):
    try:
        print(LOG.info('update_dividends_filtered_trans_id'))
        print(secid, last_purch_date, trans_id, div_paid)
        cursor = connection.cursor()

        # print(f"try execute {secid} / {last_purch_date} / {trans_id}")
        cursor.execute("""UPDATE Dividends
        SET filtered_trans_id = ?,
        div_paid = ?
        WHERE ticker == ?
        AND last_purch_date == ?""", (trans_id, div_paid, secid, last_purch_date))
        result = cursor.fetchall()
        print(result)
        # cursor.execute(sqlite_insert_query, update_data)
        connection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into DIVIDENDS table")
        # cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table DIVIDENDS", error)
    finally:
        if connection:
            connection.commit()


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
                                    figi text NOT NULL,
                                    class_code text,
                                    name text NOT NULL,
                                    isin text NOT NULL UNIQUE,
                                    group_ text NOT NULL,
                                    type text NOT NULL,
                                    groupname text NOT NULL,
                                    typename text NOT NULL);'''
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


def update_values_tickers(connection, ticker_data):
    """
    Table with SECID specification data, new SECID added if new distinct tickers
    found in Transactions table
    :param connection:
    :param ticker_data: dictiionary
    :return:
    """
    try:
        cursor = connection.cursor()
        print("Connected to SQLite DB")
        cursor.execute("SELECT DISTINCT ticker from Transactions;")
        tickers_set = cursor.fetchall()
        print(tickers_set)
        for ticker in tickers_set:
            # print(ticker[0])
            sqlite_insert_query = """INSERT OR IGNORE INTO Tickers
                              (ticker, figi, class_code, name, isin, group_, type, groupname, typename)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
            ticker = ticker_data['SECID']
            # figi = ticker_data['FIGI']  # TODO добавить сюда резолв фигов
            figi = "figi_example"
            class_code = "example"
            name = ticker_data['NAME']
            isin = ticker_data['ISIN']
            group = ticker_data['GROUP']
            type = ticker_data['TYPE']
            group_name = ticker_data['GROUPNAME']
            type_name = ticker_data['TYPENAME']
            update_data = (ticker, figi, class_code, name, isin, group, type, group_name, type_name)
            # print(update_data)
            cursor.execute(sqlite_insert_query, update_data)
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
    cursor.execute("SELECT * from Users;")
    result = cursor.fetchall()

    print("DB content Users: ")
    for r in result:
        print(r)


def read_transactions_table():
    cursor = connection.cursor()
    cursor.execute("SELECT * from Transactions;")
    result = cursor.fetchall()

    print("DB content Transactions: ")
    for r in result:
        print(r)


def read_tickers_table():
    cursor = connection.cursor()
    cursor.execute("SELECT * from Tickers ORDER BY ticker;")
    result = cursor.fetchall()

    print("DB content Tickers: ")
    for r in result:
        print(r)


def get_tickers_data_for_dividends():
    cursor = connection.cursor()
    cursor.execute("SELECT ticker, date, qty from Transactions;")
    result = cursor.fetchall()
    return result


def validate_login_pass(search_login):
    cursor = connection.cursor()
    search_login_set = (search_login,)
    cursor.execute("""SELECT email, password 
        FROM Users
        WHERE email=?""", search_login_set)
    read_result = cursor.fetchone()
    print("Checking login and password data...")
    print("-------")
    # print("User's email & passwords: ", read_result)
    return read_result


# def create_tables():
#     dividends = create_table_dividends
#     history_prices = create_table_history_prices
#     tickers = create_table_tickers
#     transactions = create_table_transactions
#     user = create_table_user

def check_tables():
    """
    check_tables initiates creation (if not exists) of tables
    """
    create_table_user(connection)
    create_table_transactions(connection)
    create_table_dividends(connection)
    create_table_tickers(connection)


if __name__ == "__main__":
    logging.info("Running db_update.py")
    con = connection
    logging.info('Check exisiting tables')
    check_tables()
    # read_tickers_table()
    # read_transactions_table()
    # get_tickers_data_for_dividends()


    # update_values_dividends(connection=connection, dividends=[["SBER", "2019-06-13", 16],
    #                                                       ["SBER", "2019-06-13", 16],
    #                                                       ["SBER", "2019-06-13", 186],
    #                                                       ["ROSN", "2020-06-13", 50],
    #                                                       ["SBER", "2019-06-13", 789]
    #                                                       ])

    # update_values_tickers(ticker_data=filter_response(value_dict=read_json(content_dict=get_json_from_moex())),
    #                       connection=connection)


    # create_table_history_prices(connection)
    # update_values_history_prices(connection=connection)

    # join_user_transactions(connection=connection)
    # calculations()
    # read_users_table()
    # read_transactions_table()

    # read_login_pass_users()
