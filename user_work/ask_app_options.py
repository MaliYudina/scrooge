"""
This module gives to an authorized user the choice of app menu options
"""
import logging

from db_process.portfolio_db import show_portfolio
from extra_features.news import show_news
from extra_features.show_graph import show_graph
from calculations.run_coupons_job import get_coupons
from user_work.exit_application import exit_app
from user_work.get_user_csv import call_add_new_transactions


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
        "Update coupons and dividends : 3\n"
        # "Show dividend & coupons calendar : 4\n"
        "Read news : 5\n"
        "Show graph : 6\n"
        "Exit app : 7\n"
    )
    options_choice = {'1': show_portfolio,
                      '2': call_add_new_transactions,  # TODO сюда надо передать имя пользователя
                      '3': get_coupons,
                      # '4': get_coupons,
                      '5': show_news,
                      '6': show_graph,
                      '7': exit_app,
                      }
    print("Your choice: ", option_number)
    func_pointer = options_choice[option_number]
    return func_pointer


def caller():
    ask_app_options()()


if __name__ == "__main__":
    caller()
