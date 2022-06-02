from tinkoff.invest import Client, InvestError, RequestError
from tinkoff.invest.token import TOKEN
from datetime import datetime, timedelta


def resolve_share_figi(ticker_name, class_code) -> str:
    """
    Идентификация торговых инструментов

    Для точного определения различных торговых инструментов используются различные идентификаторы:

    Isin(англ.: International Security Identification Number) — международный идентификационный номер ценной бумаги, состоит из 12 символов цифр и латинских букв, которые начинаются, как правило, с 2-буквенного кода страны эмитента ценной бумаги.
    Ticker — краткое (1-5 букв) наименование ценной бумаги на конкретной бирже. Без указания биржи и режима торгов, по сути, является бессмысленным набором букв. Для этого на российских биржах MOEX и SBPExchange используется специальный признак "Режим торгов", который соответствует техническому термину "class_сode".
    FIGI(англ.: Financial Instrument Global Identifier) — глобальный идентификатор финансового инструмента. Представляет собой 12-символьный код из латинских букв и цифр, определяется как идентификатор ценной бумаги на торговой площадке (бирже), которая является некоторым "источником цен".
    Основным идентификатором торгового инструмента при работе с TINKOFF INVEST API является FIGI.
    секция торгов class-code
    :param ticker_name:
    :param class_code: str режим торгов ('TQBR', etc)
    :return:
    """
    # BBG004730RP0 Газпром
    with Client(TOKEN) as client:
        # search_by_ticker = client.market.market_search_by_ticker_get("ROSN")
        # print(search_by_ticker)
        instr_response = client.instruments.get_instrument_by(id=ticker_name,
                                                              class_code=class_code,
                                                              id_type=2)

        # instr_response = client.instruments.get_instrument_by(id=ticker_name,
        #                                                       class_code=class_code,
        #                                                       id_type=2)
        figi = instr_response.instrument.figi
        # print(ticker_name, '////', figi)
    return figi


def call_share_divs_from_tink(figi, start_date, end_date) -> tuple:
    div_list_answer = []
    try:
        with Client(TOKEN) as client:
            dividends_response = client.instruments.get_dividends(figi=figi,
                                                                  from_=start_date,
                                                                  to=end_date
                                                                  )
            div = dividends_response.dividends
            for d in div:
                # print(d)
                # Dividend(dividend_net=MoneyValue(currency='usd', units=0, nano=240000000),
                #          payment_date=datetime.datetime(2021, 4, 1, 0, 0, tzinfo=datetime.timezone.utc),
                #          declared_date=datetime.datetime(2021, 3, 11, 0, 0, tzinfo=datetime.timezone.utc),
                #          last_buy_date=datetime.datetime(2021, 3, 24, 0, 0, tzinfo=datetime.timezone.utc),
                #          dividend_type='Regular Cash',
                #          record_date=datetime.datetime(2021, 3, 26, 0, 0, tzinfo=datetime.timezone.utc),
                #          regularity='Quarter', close_price=MoneyValue(currency='usd', units=4302, nano=0),
                #          yield_value=Quotation(units=0, nano=430000000),
                #          created_at=datetime.datetime(2021, 12, 17, 2, 6, 0, 562219, tzinfo=datetime.timezone.utc))
                #
                # print(dir(d))
                # 'close_price', 'created_at', 'declared_date',
                #  'dividend_net', 'dividend_type', 'last_buy_date',
                #  'payment_date', 'record_date', 'regularity',
                #  'yield_value']
                ticker = figi
                figi = figi
                last_purch_date = d.last_buy_date
                reg_close_date = 'n/a'  # у тинькова нет этой даты
                fact_paym_date = d.payment_date
                cur = d.currency
                value = int(d.dividend_net.units, d.dividend_net.nano)
                filtered_trans_id = 'tink664550'
                div_answer = (ticker, figi, last_purch_date,
                              reg_close_date, fact_paym_date, cur, value, filtered_trans_id)
                print("Tinkoff div answer: \n{}".format(div_answer))
                div_list_answer.append(div_answer)
            # print(div_tuple_answer)
            # print(type(div_tuple_answer), div_tuple_answer)
            print("Tinkoff div TUPLE answer: \n{}".format(tuple(div_list_answer)))
            return tuple(div_list_answer)
    except RequestError as e:
        print("RequestError happened")
        print(e.__class__.__name__)
    finally:
        return tuple(div_list_answer)



# def additional_features():
#         'close_price', 'created_at', 'declared_date', 'dividend_net',
#         'dividend_type', 'last_buy_date', 'payment_date', 'record_date', 'regularity', 'yield_value'
#
#         account = client.sandbox.open_sandbox_account()
#         print(account) account_id='29d1de32-5c32-4102-9544-757bb46adf9a'
#         check_account = client.sandbox.get_sandbox_accounts()
#         pprint(check_account)
#         dir(client.sandbox.post_sandbox_order)
#
#
#         my_account_id = "29d1de32-5c32-4102-9544-757bb46adf9a"
#
#
#         #
#         add_money = client.sandbox.sandbox_pay_in(account_id=my_account_id,
#                                                   amount=MoneyValue(
#                                                       currency='rub', units=777700, nano=80000))
#
#
#         print(add_money.balance)
#
#         post = client.sandbox.post_sandbox_order(figi="BBG004730RP0",
#                                                  quantity=10,
#                                                  # price=12300,
#                                                  direction=OrderDirection(1),
#                                                  account_id='29d1de32-5c32-4102-9544-757bb46adf9a',
#                                                  order_type=OrderType(2))
#         get_sandbox_orders = client.sandbox.get_sandbox_orders(
#             account_id=my_account_id)
#         pprint(get_sandbox_orders)
#         get_sandbox_positions = client.sandbox.get_sandbox_positions(
#             account_id=my_account_id)
#         print(get_sandbox_positions)
#         get_sandbox_portfolio = client.sandbox.get_sandbox_portfolio(account_id=my_account_id)
#         for p in get_sandbox_portfolio.positions:
#             pprint(p)
#         'expected_yield',
#         'positions',
#         'total_amount_bonds',
#         'total_amount_currencies',
#         'total_amount_etf',
#         'total_amount_futures',
#         'total_amount_shares'
#         pprint(check_account)
#
#         print(client.users.get_accounts())

#
# def call_tink_function():
#
# if __name__ == '__main__':
#     # share_ticker_name = 'GAZP'
#     # share_class_code = 'TQBR'
#     share_figi = resolve_share_figi(ticker_name=share_ticker_name,
#                                     class_code=share_class_code
#                                     )
#     get_dividends_from_tinkoff(figi=share_figi)
