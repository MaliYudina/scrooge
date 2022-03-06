"""
portfolio_db module creates DB and shows the current portfolio of a user"""

from db_work.db_config import create_connection
# from moex_api.get_prices import get_market_price

import sqlite3
connection = create_connection()


def get_tickers(connection) -> list:
    """
    Read Transactions DB to make unique list of tickers
    :param connection:
    :return: ticker_list - list of strings
    """
    ticker_list = []
    cursor = connection.cursor()
    cursor.execute("SELECT ticker FROM Transactions;")
    result = cursor.fetchall()
    for r in result:
        if r[0] not in ticker_list:
            ticker_list.append(r[0])
    print("Total {} tickers in portfolio: ".format(len(ticker_list)), ticker_list)
    print(ticker_list)
    return ticker_list


def get_possess_qty(connection=connection) -> int:
    """
    Gets current quantity of possessed shares
    :return:
    """
    search_secid = ('MOEX',)
    cursor = connection.cursor()
    # cursor.execute("""SELECT SUM(qty) FROM Transactions""")
    cursor.execute("""SELECT SUM(qty) FROM Transactions WHERE ticker=?""", search_secid)

    shares_qty = cursor.fetchone()
    print(shares_qty[0])
    return shares_qty


def calculate_average_price() -> float:
    search_secid = 'SBER'
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(qty) / COUNT(ticker)" # TODO суммирую сумму покупки и делю на количество транзакций
                   "FROM Transactions"
                   "WHERE ticker=?", search_secid)
    # TODO аналог функции
    total_price_list = [10, 20, 30]
    average_price = sum(total_price_list) / len(total_price_list)
    return average_price


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
                                    ticker TEXT UNIQUE,
                                    shortname TEXT NOT NULL,
                                    qty NOT NULL,
                                    avg_price REAL NOT NULL,
                                    cur TEXT NOT NULL,
                                    market_price,
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


def update_values_portfolio(connection, portfolio_data):
    try:
        cursor = connection.cursor()
        sqlite_insert_query = """INSERT OR IGNORE INTO Portfolio
                              (ticker, shortname, qty, avg_price, 
                              cur, market_price, dividend_total, dividend_percent_total, 
                              total_margin_rub, total_margin_percent, weight) 
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        cursor.execute(sqlite_insert_query, portfolio_data)
        connection.commit()
        print("Data to insert: ", portfolio_data)
        connection.commit()
        cursor.close()
        print("---- Successfully added to Portfolio Table! ----")
    except sqlite3.Error as error:
        print("Failed to insert record into sqlite table Portfolio", error)
    finally:
        if connection:
            connection.commit()


def portfolio_calculations():
    pass


def show_portfolio():
    cursor = connection.cursor()
    cursor.execute("SELECT * from Portfolio")
    result = cursor.fetchall()
    print("My portfolio ")
    for r in result:
        print(r)
    portfolio_calculations()
    return result


def portfolio_save_to_csv():
    """
    Save current portfolio data to CSV file
    :return: csf format file
    """
    pass


tickers = get_tickers(connection=connection)
get_possess_qty(connection=connection)

shortname = ''
# qty = get_possess_qty()
# avg_price = calculate_average_price()
cur = "RUB"
# market_price = get_market_price()
div_total = 100
div_percent_total = '10%'
total_margin = 100
total_margin_percent = "10%"
weight = '5%'


# create_table_portfolio(connection=connection)
#
#
# for ticker in tickers:
#     portfolio = (ticker, shortname,
#                     qty, avg_price,
#                     cur, market_price,
#                     div_total, div_percent_total,
#                     total_margin, total_margin_percent,
#                  weight)
#
#     update_values_portfolio(connection=connection, portfolio_data=portfolio)
#
#
# user_portfolio = show_portfolio()  # <class 'list'>