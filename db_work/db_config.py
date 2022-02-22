import os
import sqlite3
from sqlite3 import Error

current_dir = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(current_dir, 'sql_investor.db')
print(db_file)


def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
