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


CREATE TABLE IF NOT EXISTS Tickers (_id INTEGER PRIMARY KEY, user_id INTEGER, ticker TEXT NOT NULL UNIQUE, name text NOT NULL, isin INTEGER, group text NOT NULL, type text NOT NULL, groupname text NOT NULL, typename text NOT NULL);

insert in terminal:
INSERT INTO Dividends (ticker, date, price) values ('AAPL', '2022-10-10', 1800);
INSERT INTO Transactions (user_email, ticker, trans_type, type_code, date, cur, qty, price, total_price, commission, est_taxes) values ('petr', 'SBER', 'buy', 1, '2014-06-20', 'RUB', 10, 1800, 18000, 8);
INSERT OR IGNORE INTO Dividends (ticker, isin, last_purch_date, reg_close_date, fact_paym_date, cur, value, filtered_trans_id) VALUES ('ROSN', 'RUAS8980555', '2020-10-10','2020-10-10','2020-10-10','CNY', 670, 888);

INSERT INTO Transactions (user_email, ticker, trans_type, type_code, date, cur, qty, price, total_price, commission, est_taxes) values ('samantha', 'NVTK', 'buy', 1, '2021-06-10', 'usd', 10, 1800, 18000, 8);