"""
checks if transaction is ok to apply dividend coupons
"""
from db_process.db_connection import create_connection
from db_process.db_update import update_dividends_values_paid, update_dividends_filtered_trans_id
from pprint import pprint
from functools import reduce

connection = create_connection()


def resolve_dividends_interval(secid) -> list:
    """
    Делаем выборку по тикеру из таблицы Dividends
    циклом создаем интервалы:
    начало периода - конец периода - сумма дивидендных выплат за период
    :param secid:
    :return:
    """
    cur = connection.cursor()
    cur.execute("""SELECT last_purch_date, value from Dividends 
        WHERE ticker == ?""", (secid,))
    result = cur.fetchall()
    n = len(result)
    interval_list = []
    while n >= 2:
        n -= 1
        # начало периода - конец периода - сумма дивидендных выплат
        start_end_dates = (result[n - 1][0], result[n][0], result[n][1])
        interval_list.append(start_end_dates)
    return interval_list


def group_transactions_per_period(secid, last_purch_date, prev_last_purch_date):
    """
    На основе входящих дивидендных интервалов группируем транзакции
    по датам в пределах дивидендного периода
    (secid, last_purch_date, prev_last_purch_date)
    :param secid:
    :param last_purch_date:
    :param prev_last_purch_date:
    :return:
    """
    cur = connection.cursor()
    # потом первую строчку заменить на
    # SELECT _id, ticker, date, SUM (qty) from Transactions
    # чтобы получать только число акций
    cur.execute("""SELECT _id, ticker, date, qty from Transactions 
    WHERE ticker == ?
    AND date <= ? 
    AND date >= ?""", (secid, last_purch_date, prev_last_purch_date))
    tickers_result = cur.fetchall()
    print(f'Grouped transactions\n tickers_result for {prev_last_purch_date} / {last_purch_date}. Total {len(tickers_result)}')
    filtered_trans_id = []
    for t in tickers_result:
        filtered_trans_id.append(t[0])
    # print(filtered_trans_id)
    print(tickers_result)
    return tickers_result


def extract_sell_qty(transactions):
    """
    Extract sell quantity within interval
    :return:
    """
    qty_list = []
    for t in transactions:
        qty_list.append(t[3])
    # print(qty_list)
    total_qty = sum(qty_list)
    # print(total_qty)
    return total_qty


def charge_dividends_payment(qty, value):
    """
    Charge payment for each transaction, groupped by transaction period
    :param secid:
    :param transactions_list:
    :param fact_payment_date:
    :return:
    """

    div_sum = qty * value
    # print(f'{div_sum=}')
    return div_sum


def subtotal(secid):
    interval_data = resolve_dividends_interval(secid=secid)
    # pprint(dates)
    n = 0
    result_list = []
    print(result_list)
    print('SUBTOTAL')
    if len(interval_data) > 0:
        for date in interval_data:
            print('date')
            print(date)
            n = n + 1
            last_purch_date = date[1]
            prev_last_purch_date = date[0]
            transactions = group_transactions_per_period(secid=secid,
                                                         last_purch_date=last_purch_date,
                                                         prev_last_purch_date=prev_last_purch_date)

            print('transactions')
            print(transactions)
            shares_qty = extract_sell_qty(transactions)
            div_value = date[2]
            div_total = charge_dividends_payment(qty=shares_qty, value=div_value)
            print(f'div_total={div_total}')
            if transactions is not None:
                print(f'shares_qty={shares_qty}')
                for t in transactions:
                    trans_id = t[0]
                    print(f'trans_id={t[0]}, shares_qty={shares_qty}, div_total={div_total} ')
                    update_dividends_filtered_trans_id(connection, secid, last_purch_date,
                                                       trans_id=trans_id, div_paid=div_total)


            filtered_trans_id = []
            for t in transactions:
                filtered_trans_id.append(t[0])
            div_payment_data = (n, prev_last_purch_date, last_purch_date, div_total, shares_qty, filtered_trans_id)
            print(f'div_payment_data={div_payment_data}')
            result_list.append(div_payment_data)
            result_list = sorted(result_list, reverse=True)
        # print(result_list)
        shares_qty_list = [i[4] for i in result_list]
        div_value_list = [i[3] for i in result_list]

        # print(shares_qty_list)
        start_date = result_list[0][1]
        print(start_date)
        print(f'Start date {start_date}')
        end_dates_list = [i[2] for i in result_list]
        # print(end_dates_list)

        num = 0
        print('div_subresults')
        print('order_num, start_date, end, sum(qty), sum(div_value2), '
              '(div_value * sum(qty)), ({} per share)')
        pay_results = []
        while num < len(result_list):
            num += 1
            order_num = str(f'{num} / {len(result_list)}')
            end = end_dates_list[num - 1]
            qty = shares_qty_list[:num]
            div_value2 = div_value_list[:num]
            div_value = div_value_list[num-1]
            div_subresult = (order_num, start_date, end, sum(qty), sum(div_value2),
                             (div_value * sum(qty)))
            print(f'{order_num}, {start_date}, {end}, {sum(qty)} pcs, {sum(div_value2)}, '
                  f'{(div_value * sum(qty))}, {div_value}, per share')
            pay_results.append(div_subresult)

        print('pay_results')
        for p in pay_results:
            print(p)
        return pay_results
    else:
        print("No SUBTOTAL")
        pass


def pay_divs(secid):
    print(f'pay_divs for {secid=}')
    answer = subtotal(secid)
    print('Subtotal answer', answer)
    return answer


def show_total_divs(secid) -> int:
    cur = connection.cursor()
    print(f'show_total_divs(secid) {secid}, {type(secid)}')
    cur.execute("""SELECT sum(div_paid) from Dividends 
        WHERE ticker == ?""", (secid,))
    div_total = cur.fetchall()
    return div_total


# if __name__ == '__main__':
#     pay_divs()
