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
        # 1. проверяем и создаем при необходимости таблицы в БД
        check_tables()
        # 2. запускаем логику авторизации/регистрации польтзователя
        session_user_name = run_welcome()
        logging.info('User {} logged in'.format(session_user_name))
        print("Session for {} starts...".format(session_user_name))
        # 3. запускаем вечную петлю вызова меню опций для работы с приложением
        while True:
            logging.info('Menu infifnite loop')
            caller()
    # 4. выводим ошибку, завершаем работу приложения
    except:
        logging.error(Exception.__class__.__name__)


if __name__ == '__main__':
    main()
