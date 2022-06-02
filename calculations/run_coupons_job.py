from db_process.dividend_work import tickers_caller
from db_process.db_connection import create_connection
from db_process.db_update import update_values_dividends, update_dividends_values_paid
from moex_api.call_moex_api_coupons import get_share_divs_from_moex
from tink_api.get_dividends_value_tink import resolve_share_figi, call_share_divs_from_tink
from .assign_coupons import pay_divs
from datetime import datetime, timedelta
import logging
from tinkoff.invest.exceptions import InvestError, StatusCode

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger('run_coupons_job')


def call_share_divs_from_api(secid):
    """
    Calls MOEX or TINK API to get information about dividends data for shares
    :param tickers_list:
    :return:
    """
    logging.info('--- call_share_divs_from_api started')
    # import pdb; pdb.set_trace()
    try:
        logging.info('Step 1 moex_api_answer started')
        dividends = get_share_divs_from_moex(secid=secid)
        if dividends is None:
            logging.info('Step 2 tink_api_answer started')
            resolved_figi = resolve_share_figi(ticker_name=secid, class_code='TQBR')
            start_date = datetime.utcnow() - timedelta(days=10000)
            # start_date = resolve_start_date() TODO реализовать дату (но от какой даты отталкиваться?)
            end_date = datetime.utcnow()
            dividends = call_share_divs_from_tink(resolved_figi, start_date, end_date)
            return dividends
        return dividends
    except InvestError as e:
        print(e.__class__.__name__)
    except StatusCode.NOT_FOUND as s:
        print(s)


def call_bond_coupons_from_api(bonds_list):
    """
    Calls MOEX or TINK API to get coupons for bonds
    :param bonds_list:
    :return:
    """
    pass


def run_pay_divs(secid):
    paid_divs = pay_divs(secid)
    return paid_divs


def get_coupons():
    """
    Runs calling for dividends and coupons
    :return:
    """
    list_of_tickers = tickers_caller()
    print(list_of_tickers)
    for item in list_of_tickers:
        secid = item[0]
        div_result = call_share_divs_from_api(secid=secid)
        if div_result is not None:
            update_values_dividends(connection=create_connection(), dividends=div_result)
            div_paid = run_pay_divs(secid=secid)
            if div_paid is not None:
                for d in div_paid:
                    start_date = d[1],
                    end_date = d[2],  # TODO вааажно
                    last_purch_date = d[1]
                    div_paid_value = d[6]
                    print(f'!!!! secid={secid}, date={last_purch_date}'
                          f' start / end {start_date}/{end_date}, money total={div_paid_value}')
                    update_dividends_values_paid(connection=create_connection(),
                                                 secid=secid,
                                                 last_purch_date=last_purch_date,
                                                 start_date=start_date,
                                                 end_date=end_date,
                                                 div_paid_value=div_paid_value
                                                 )
        else:
            print(Exception.__class__.__name__)
            print("No record added to DB (dividends empty)")
            pass
    # return div_result



if __name__ == '__main__':
    get_coupons()
    # run_pay_divs()

    # print("dividends_to_write")
    # print(dividends_to_write)





