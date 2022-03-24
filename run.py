
from user_work.login import run_welcome
from user_work.ask_app_options import caller
from db_work.db_config import create_connection
from db_work.db_update import validate_login_pass, read_users_table, update_values_user


import pdb


def main():
    try:
        # TODO сделать проверку-запуск create tables
        session_user_name = run_welcome()
        print("Session for {} starts...".format(session_user_name))
        caller()
    except:
        print(Exception)


if __name__ == '__main__':
    main()
