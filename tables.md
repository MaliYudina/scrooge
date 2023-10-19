mini:db_process mali$ sqlite3 sql_investor.db

.tables
.headers ON
.mode column

.schema Users


SELECT * FROM Transactions;

SELECT * FROM Transactions where user_email='mali';

add new lines to Transactions:

INSERT INTO Transactions (user_email, ticker, trans_type, type_code, date, cur, qty, price, total_price, commission)
VALUES ('test_user', 'MSFT', 'Buy', 'B', '2023-10-20', 'USD', 10, 150.0, 1500.0, 10.0);




