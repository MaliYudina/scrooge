"""
Get_coupons_value_tink module resolves FIGI id for a bond and
calls Tinkoff API to receive bond coupons
"""

from tinkoff.invest import Client
from tinkoff.invest.token import TOKEN
from tinkoff.invest.schemas import InstrumentIdType
from datetime import datetime, timedelta


def resolve_figi_for_bond(ticker_name, class_code):
    """
    Resolves FIGI id base on ticker name and class_code

    :param ticker_name: str ticker name for a bond
    :param class_code: type of
    :return: str figi value
    """
    with Client(TOKEN) as client:
        bond = client.instruments.bond_by(id_type=InstrumentIdType(2),
                                          class_code=class_code,
                                          id=ticker_name)
        figi = bond.instrument.figi
        return figi


def get_bonds_coupon(figi):
    """
    :param figi: str figi id
    :return: tuple of coupon data (value, payment date etc)
    """
    with Client(TOKEN) as client:
        start_date = datetime.utcnow() - timedelta(days=10000)
        end_date = datetime.utcnow()
        coupons = client.instruments.get_bond_coupons(figi=figi,
                                                      from_=start_date,
                                                      to=end_date)
        print("start date {}, end date {}".format(start_date, end_date))
        print("Figi: {}".format(figi))
        for c in coupons.events:
            coupon_tuple = (c.coupon_date.date(),
                            c.coupon_end_date.date(),
                            c.coupon_number,
                            c.coupon_period,
                            c.coupon_start_date,
                            c.coupon_type.value,
                            c.figi,
                            c.fix_date,
                            # c.pay_one_bond
                            (c.pay_one_bond.units,
                             c.pay_one_bond.nano,
                             c.pay_one_bond.currency)
                            )
            print(coupon_tuple)
            return coupon_tuple


if __name__ == '__main__':
    bond_ticker_name = "RU000A101P92"
    bond_class_code = "TQIR"
    bond_figi = resolve_figi_for_bond(ticker_name=bond_ticker_name,
                                      class_code=bond_class_code
                                      )
    get_bonds_coupon(figi=bond_figi)
