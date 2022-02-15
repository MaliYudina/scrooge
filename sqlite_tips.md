(.venv) mini:investor mali$ sqlite3 sql_investor.db

sqlite> .header on
sqlite> .mode column
sqlite> SELECT * FROM Tickers;

id  ticker  name       date        price
--  ------  ---------  ----------  -------
4   YNDX    Yandex     2019-01-14  10800.0
5   SBER    Sberbank   2019-05-15  7600.2
6   VISA    Visa card  2019-03-27  84.0

Tickers:
