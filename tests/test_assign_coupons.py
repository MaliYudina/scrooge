import unittest
# TODO create test_base.db  https://habr.com/ru/post/677598/

from calculations.assign_coupons import resolve_dividends_interval, \
    group_transactions_per_period


class TestResolveDividends(unittest.TestCase):
    def test_resolve_dividends_period(self):
        assert resolve_dividends_interval("ALRS") == [('2021-07-01 00:00:00', '2021-10-16 00:00:00', 8.79),
                                                      ('2020-07-10 00:00:00', '2021-07-01 00:00:00', 9.54),
                                                      ('2019-10-11 00:00:00', '2020-07-10 00:00:00', 2.63),
                                                      ('2019-07-12 00:00:00', '2019-10-11 00:00:00', 3.84),
                                                      ('2018-10-12 00:00:00', '2019-07-12 00:00:00', 4.11),
                                                      ('2018-07-11 00:00:00', '2018-10-12 00:00:00', 5.93),
                                                      ('2017-07-17 00:00:00', '2018-07-11 00:00:00', 5.24),
                                                      ('2016-07-16 00:00:00', '2017-07-17 00:00:00', 8.93),
                                                      ('2015-07-12 00:00:00', '2016-07-16 00:00:00', 2.09),
                                                      ('2014-07-15 00:00:00', '2015-07-12 00:00:00', 1.47)]

    def test_group_transactions_per_period(self):
        assert group_transactions_per_period(secid="ALRS",
                                             last_purch_date="2018-10-16 00:00:00",
                                             prev_last_purch_date="2022-07-01 00:00:00"
                                             ) == []
