"""
Run module runs the main logic of the applications
точка входа / запуска
"""
from user_work.login import run_welcome
from user_work.ask_app_options import caller
from db_process.db_update import check_tables
import logging


def main():
    try:
        logging.info('Application started')
        check_tables()
        session_user_name = run_welcome()
        logging.info('User {} logged in'.format(session_user_name))
        print("Session for {} starts...".format(session_user_name))
        caller()
        logging.info('Application work finished')
    except:
        logging.error(Exception.__class__.__name__)


if __name__ == '__main__':
    main()
