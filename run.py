"""
Run module runs the main logic of the Application
точка входа / запуска
"""
import logging


from log_work.log_setup import setup_logger
logger = setup_logger()
logger.info('run.py success')

LOGGER = logger

from user_work.login import run_welcome

from db_process.db_update import check_tables
from user_work.ask_app_options import caller


def main():
    try:
        LOGGER.debug('Hello')
        LOGGER.debug('Application started')
        # 1. проверяем и при необходимости создаем таблицы в БД
        check_tables()
        # 2. запускаем логику авторизации/регистрации польтзователя
        session_user_name = run_welcome()
        LOGGER.info('User {} logged in'.format(session_user_name))
        print("Session for {} starts...".format(session_user_name))
        # 3. запускаем вечную петлю вызова меню опций для работы с приложением
        while True:
            LOGGER.info('Menu infifnite loop')
            caller()
    # 4. выводим ошибку, завершаем работу приложения
    except:
        logger = LOGGER
        print(logger)
        # logger = start_logging()
        logger.error(Exception.__class__.__name__)
        logging.error('some error')


if __name__ == '__main__':
    main()
