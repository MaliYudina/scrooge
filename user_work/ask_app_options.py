"""
ask_app_options module gives to an authorized user the choice of app menu options -
start menu of entire application,
"""
import logging.config
 # если закоментировать импорт этих библиотек, то программа не будет падать
from extra_features.news import show_news
from extra_features.show_graph import show_graph
from calculations.run_coupons_job import get_coupons
from db_process.portfolio_db import show_portfolio
from user_work.exit_application import exit_app
from user_work.get_user_csv import call_add_new_transactions

# from log_work.log_config import get_logging_dict_config
#
# logging.config.dictConfig(get_logging_dict_config())



logging.basicConfig(
    level=logging.DEBUG,
    filename="mylog.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    )

logger = logging.getLogger('ASK APP run.py ')


def ask_app_options():
    """
    ask_app_options function shows to a user menu of available actions,
    asks to enter string symbol, equivalent to calling fucntion
    :return:
    """
    print("-- Let's start investing. Please choose option: --")
    option_number = input(
        "Show my portfolio : 1\n"
        "Add new transactions : 2\n"
        "Update coupons and dividends : 3\n"
        # "Show dividend & coupons calendar : 4\n"
        "Read news : 5\n"
        "Show graph : 6\n"
        "Exit app : 7\n"
    )
    options_choice = {'1': show_portfolio,
                      '2': call_add_new_transactions,  # TODO сюда надо передать имя пользователя
                      '3': get_coupons,
                      # '4': get_calendar,
                      '5': show_news,
                      '6': show_graph,
                      '7': exit_app,
                      }
    print("Your choice: ", option_number)
    logger.info(f"User choice: ")

    func_pointer = options_choice[option_number]  # func_pointer <class 'function'>
    return func_pointer


def caller():
    ask_app_options()()


if __name__ == "__main__":
    caller()
