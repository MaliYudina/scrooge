"""
Login module:
  - registration of new users;
  - authorization of registered users
"""
from datetime import datetime
from db_work.db_config import create_connection
from db_work.db_update import validate_login_pass, read_users_table, update_values_user


def hi_user():
    start_input = input("-- Hello, user! -- \nPlease type \n  'l' for login or \n  'r' for registration\n")
    return start_input


def login_user() -> tuple:
    """
    login_user asks user to enter login email and password
    :param no params required
    :return: tuple email and password pair
    """
    print("Login form: ")
    email = input('Please input your login: ')
    password = input('Please input your password: ')
    return email, password


def register_user() -> tuple:
    """
    register_user gets a new user input as string
    :return: tuple email and password pair
            """
    print("Registration form: ")
    email = input('Please input your email login: ')
    name = input('Please input your name: ')
    surname = input('Please input your surname: ')
    broker_name = input('Please input your broker_name: ')
    password = input('Please input your password: ')
    conf_password = input('Please confirm your password: ')
    while conf_password != password:
        conf_password = input('Please CHECK your password again: ')
    now = datetime.now()
    now = now.strftime("%Y-%m-%d")
    new_user_data = (email, name, surname, password, broker_name, now)
    print("New user will be registered and added to DB\n", new_user_data)
    # <class 'tuple'> ('test@email.ru', 'kate', 'smirnova', 'kat123', 'Finam', '2022-02-15')
    return new_user_data


def authorize_user(email, password, db_email, db_password):
    if email in db_email:  # str email in db_email tuple
        if password == db_password:
            print("Welcome back, {}!. You are successfully signed in!".format(email))
            return email
        else:
            print("Sorry, {}! Login data is wrong.\nPlease register new account or check login data.".format(email))
            hi_user()


def run_welcome():
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
    if login_or_register == 'r':
        new_user = register_user()
        print("----- New user data: -----", new_user)
        update_values_user(connection=create_connection(),
                           user_data=new_user)
        print("-----Let's see the User Table: -----")


run_welcome()
