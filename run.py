from db_work.db_update import read_users_table
from user_work.login import *


def main():

    hi_user()

    validate_email_and_password = login_user()

    login_to_validate = validate_email_and_password[0]
    pass_to_validate = validate_email_and_password[1]
    print(login_to_validate, pass_to_validate)

    if login_to_validate is True:
        validate_user(email=login_to_validate,
                      password=pass_to_validate,
                      db_email='mali',
                      db_password='11')
    else:
        register_user()

    print('Read all users data: ')
    read_users_table()


if __name__ == '__main__':
    main()
