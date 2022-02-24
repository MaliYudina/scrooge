
from user_work.login import hi_user, login_user, register_user, authorize_user
from user_work.get_user_input import caller
from db_work.db_config import create_connection
from db_work.db_update import validate_login_pass, read_users_table, update_values_user

import pdb


def main():
    try:
        login_or_register = hi_user()
        if login_or_register == 'l':
            input_email_pass = login_user()
            input_email = input_email_pass[0]
            input_password = input_email_pass[1]

            stored_email_pass = validate_login_pass(search_login=input_email)
            stored_db_email = stored_email_pass[0]
            stored_db_pass = stored_email_pass[1]
            authorize_user(email=input_email,
                           password=input_password,
                           db_email=stored_db_email,
                           db_password=stored_db_pass
                           )
            caller()
        if login_or_register == 'r':
            new_user = register_user()
            print("----- New user data: -----", new_user)
            update_values_user(connection=create_connection(), user_data=new_user)
            print("-----Let's see the User Table: -----")
            read_users_table()
    except:
        hi_user()


if __name__ == '__main__':
    main()
