"""
portfolio_db module creates DB and shows the current portfolio of a user
сделать апдейт в фоновом режиме
"""
import datetime

from db_process.db_connection import create_connection
# from moex_api.get_prices import get_market_price
from calculations.assign_coupons import show_total_divs

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
    shares_qty = shares_qty[0]
    return shares_qty


def calculate_average_price(secid) -> float:
    secid_tuple = ()
    secid_tuple = secid_tuple + (secid,)
    cursor = connection.cursor()
    cursor.execute("""SELECT SUM(qty) / COUNT(ticker)"
                   "FROM Transactions"
                   "WHERE ticker=?""", secid_tuple)
    average = cursor.fetchone()
    average_price = average[0]
    print(f"average price for {secid_tuple[0]} : {average_price}")

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
                                    user_email TEXT,
                                    ticker TEXT UNIQUE,
                                    shortname,
                                    qty INTEGER,
                                    avg_price,
                                    cur,
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


def update_values_portfolio(connection):
    tickers = get_tickers(connection=connection)
    for ticker in tickers:
        user_email = 'sys'
        shortname = ticker
        qty = get_possess_qty(secid=ticker, connection=connection)
        avg_price = calculate_average_price(secid=ticker)
        cur = "RUB"
        market_price = 333
        # market_price = get_market_price(ticker)
        div_total = show_total_divs(secid=ticker)
        div_total = div_total[0][0]
        print(f'div total to write: {div_total}')
        div_percent_total = '10%'
        total_margin = 100
        total_margin_percent = "10%"
        weight = '5%'

        portfolio_data = (user_email, ticker, shortname,
                     qty, avg_price,
                     cur, market_price,
                     div_total, div_percent_total,
                     total_margin, total_margin_percent,
                     weight)
        print(portfolio_data)
        try:
            cursor = connection.cursor()
            sqlite_insert_query = """INSERT OR REPLACE INTO Portfolio
                                  (user_email, ticker, shortname, qty, avg_price, 
                                  cur, market_price, dividend_total, dividend_percent_total, 
                                  total_margin_rub, total_margin_percent, weight) 
                                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
            print("Data to insert: ", portfolio_data)
            cursor.execute(sqlite_insert_query, portfolio_data)
            connection.commit()
            cursor.close()
            print("---- Successfully added to Portfolio Table! ----")
        except sqlite3.Error as error:
            print("Failed to insert record into sqlite table Portfolio", error)
        finally:
            if connection:
                connection.commit()


def show_header():
    user_name = 'Test user SYS'
    portfolio_cost = 34894.98
    now = datetime.datetime.now()
    print(f"Header will be here\n {user_name} {portfolio_cost} {now}")


def show_footer():
    ticker_num = 'total 11 tickers'
    portfolio_cost = 34894, 98
    print(f"Footer will be here\n {ticker_num} {portfolio_cost}")


def show_portfolio():
    cursor = connection.cursor()
    create_table_portfolio(connection=connection)
    update_values_portfolio(connection)
    cursor.execute("SELECT * from Portfolio")
    print("--- My portfolio --- ")
    result = cursor.fetchall()
    show_header()
    field_names = [i[0] for i in cursor.description]
    print(field_names)
    for r in result:
        print(r)
    show_footer()
    return result


def portfolio_save_to_csv():
    """
    Save current portfolio data to CSV file
    :return: csf format file
    """
    pass


if __name__ == "__main__":
    print("Running portfolio_db.py")
    show_portfolio()



# user_portfolio = show_portfolio()  # <class 'list'>