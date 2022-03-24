"""
portfolio_db module creates DB and shows the current portfolio of a user"""

from db_work.db_config import create_connection
from moex_api.get_prices import get_market_price

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
    cursor.execute("SELECT DISTINCT ticker FROM Transactions;")
    result = cursor.fetchall()
    print(result)
    for r in result:
        ticker_list.append(r[0])
    print("Total {} tickers in portfolio: ".format(len(ticker_list)), ticker_list)
    print(ticker_list)
    return ticker_list


def get_possess_qty(secid, connection=connection, ) -> int:
    """
    Gets current quantity of possessed shares
    :return:
    """
    cursor = connection.cursor()
    secid_tuple = ()
    secid_tuple = secid_tuple + (secid,)
    cursor.execute("""SELECT SUM(qty) FROM Transactions WHERE ticker=?""", tuple(secid_tuple))
    shares_qty = cursor.fetchone()
    print(shares_qty[0])
    return shares_qty


def calculate_average_price(secid) -> float:
    secid_tuple = ()
    secid_tuple = secid_tuple + (secid,)
    cursor = connection.cursor()
    cursor.execute("""SELECT SUM(qty) / COUNT(ticker)"
                   "FROM Transactions"
                   "WHERE ticker=?""", secid_tuple)
    average_price = cursor.fetchone()
    # print("average")
    # print(average_price[0])
    return average_price[0]


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
                                    qty INTEGER NOT NULL,
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


def show_portfolio():
    cursor = connection.cursor()
    cursor.execute("SELECT * from Portfolio")
    result = cursor.fetchall()
    print("My portfolio ")
    for r in result:
        print(r)
    return result


def portfolio_save_to_csv():
    """
    Save current portfolio data to CSV file
    :return: csf format file
    """
    pass


if __name__ == "__main__":
    print("Running portfolio_db.py")
    create_table_portfolio(connection=connection)
    tickers = get_tickers(connection=connection)
    for ticker in tickers:
        shortname = 'short'
        qty = get_possess_qty(secid=ticker, connection=connection)
        avg_price = calculate_average_price(secid=ticker)
        cur = "RUB"
        market_price = 333
        # market_price = get_market_price(ticker)
        div_total = 100
        div_percent_total = '10%'
        total_margin = 100
        total_margin_percent = "10%"
        weight = '5%'

        portfolio = (ticker, shortname,
                        qty, avg_price,
                        cur, market_price,
                        div_total, div_percent_total,
                        total_margin, total_margin_percent,
                     weight)
        print(portfolio)
        portfolio_sum = 10000
        print('Total portfolio value: ', portfolio_sum)
        update_values_portfolio(connection=connection, portfolio_data=portfolio)
        show_portfolio()


# user_portfolio = show_portfolio()  # <class 'list'>