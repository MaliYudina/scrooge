"""
Login module:
  - registration of new users;
  - authorization of registered users
"""
from datetime import datetime


def hi_user():
    start_input = input("--Hello, user! \nPlease type 'l' for login or 'r' for registration\n")
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
            return True
        else:
            print("Sorry, {}! Login data is wrong.\nPlease register new account or check login data.".format(email))
            register_user()

