from user_work.login import *
# from user_work.get_user_input import ask_input
from db_work.db_update import validate_login_pass


def main():
    login_or_register = hi_user()
    if login_or_register == 'l':
        input_email_pass = login_user()
        input_email = input_email_pass[0]
        print('1. Input email ', type(input_email)) # str
        input_password = input_email_pass[1]
        print('2. Input pass ', input_password)

        stored_email_pass = validate_login_pass(search_login=input_email)
        stored_db_email = stored_email_pass[0]
        stored_db_pass = stored_email_pass[1]
        print(input_email, input_password, stored_db_email, stored_db_pass)
        authorize_user(email=input_email,
                       password=input_password,
                       db_email=stored_db_email,
                       db_password=stored_db_pass
                       )
    if login_or_register == 'r':
        register_user()
    else:
        hi_user()

    # authorized_user = find_login_pass(received_login=login_to_authorize[0])
    # print(authorized_user)
    #
    # if authorized_user is True:
    #     ask_input()
    # else:
    #     register_user()
    #
    # read_users_table()
    #
    # validate_email_and_password = login_user()
    #
    # login_to_validate = validate_email_and_password[0]
    # pass_to_validate = validate_email_and_password[1]
    # print("login and pass_to_validate: ")
    # print(login_to_validate, pass_to_validate)
    #
    #
    # # if login_to_validate is True:
    # #     result_tuple = find_login_pass(received_login=login_to_validate)
    # #     print(result_tuple)
    # #     db_email = result_tuple[0]
    # #     db_password = result_tuple[1]
    # #     print(db_email, db_password)
    # #     authorize_user(email=login_to_validate,
    # #                    password=pass_to_validate,
    # #                    db_email=db_email,
    # #                    db_password=db_password)
    # # else:
    # #     register_user()
    #
    # print('Read all users data: ')
    # read_users_table()


if __name__ == '__main__':
    main()
