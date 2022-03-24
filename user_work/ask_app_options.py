"""
This module gives user choice of app options and calls them
from another modules
"""
import logging
from extra_features.news import show_news
from db_work.portfolio_db import show_portfolio
from moex_api.get_coupons import get_coupons
from extra_features.show_graph import show_graph
from user_work.exit_application import exit_app
from user_work.get_user_csv import add_new_transactions


logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger('ask_app_options')


def ask_app_options():
    """
    ask_input function gives the logged user choice of further actions,
    such as checking portfolio or adding some new data
    :return:
    """
    print("-- Let's start investing. Please choose option: --")
    option_number = input(
        "Show my portfolio : 1\n"
        "Add transactions : 2\n"
        "Check coupons transactions : 3\n"
        "Read news : 4\n"
        "Show graph : 5\n"
        "Exit app : 6\n"
    )
    options_choice = {'1': show_portfolio,
                      '2': add_new_transactions,
                      '3': get_coupons,
                      '4': show_news,
                      '5': show_graph,
                      '6': exit_app,
                      }
    print("Your choice: ", option_number)
    func_pointer = options_choice[option_number]
    return func_pointer


def caller():
    ask_app_options()()


if __name__ == "__main__":
    caller()
