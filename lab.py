from functools import reduce
orig_list = [(7, '2014-05-14 00:00:00', '2015-06-20 00:00:00', 15.75, 5),
                 (6, '2015-05-14 00:00:00', '2016-06-20 00:00:00', 0.0, 10),
                 (5, '2016-05-14 00:00:00', '2017-06-20 00:00:00', 0.0, 15),
                 (4, '2017-05-14 00:00:00', '2018-06-20 00:00:00', 36.0, -5),
                 (3, '2018-05-14 00:00:00', '2019-06-20 00:00:00', 160.0, 20),
                 (2, '2019-05-14 00:00:00', '2020-10-20 00:00:00', 3.5, 5),
                 (1, '2020-05-14 00:00:00', '2021-05-20 00:00:00', 7, 5)]
shares_qty_list = [i[4] for i in orig_list]
div_value_list = [i[3] for i in orig_list]

# print(sum([5, 10, 15, -5, 20, 5, 5]))  # 55


def my_func():

    print(shares_qty_list)
    start_date = orig_list[0][1]
    print(f'Start date {start_date}')
    end_dates_list = [i[2] for i in orig_list]
    print(end_dates_list)


    num = 0
    while num < len(orig_list):
        num += 1
        print(f'{num} / {len(orig_list)}')
        end = end_dates_list[num-1]
        qty = shares_qty_list[:num]
        div_subresult = (start_date, end, sum(qty))
        print(div_subresult)
    # subsum = reduce(lambda x, y: x + y, map(int, shares_qty_list))
    # print(subsum)

my_func()

def chain_sum(number):
    result = number

    def wrapper(number2=None):
        nonlocal result
        if number2 is None:
            return result
        result += number2
        return wrapper
    return wrapper



# print(chain_sum(5)())
# print(chain_sum(5)(2)())
# print(chain_sum(5)(100)(-10)())

def test_args(*args):
    print(type(args))


test_args('loh', 5, None)
