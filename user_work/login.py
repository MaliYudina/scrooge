"""
Login module:
  - registration of new users;
  - authorization of registered users
"""
# import pdb; pdb.set_trace()
from datetime import datetime
from db_process.db_connection import create_connection
from db_process.db_update import validate_login_pass, update_values_user, update_values_sessions


def hi_user() -> str:
    """
    Asks user if he want to register or log in
    :return: string value of the choice var:start_input
    """
    start_input = input("WELCOME TO INVESTOR SCROOGE! -- \nPlease type \n  'l' for login or "
                        "\n  'r' for registration\n")

    # loop in case the user mistyped
    while start_input not in ['l', 'r']:
        start_input = input("Please be careful! Only 2 options available: \n  'l' for login or "
                            "\n  'r' for registration\n")
    return start_input


def login_user() -> tuple:
    """
    login_user asks the user to enter the pair of login & password
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
        conf_password = input('!!! Please CHECK your password again: ')
    now = datetime.now()
    now = now.strftime("%Y-%m-%d")
    new_user_data = (email, name, surname, password, broker_name, now)
    print("A new user will be registered and added to DB\n", new_user_data)
    # <class 'tuple'> ('test@email.ru', 'kate', 'smirnova', 'kat123', 'Finam', '2022-02-15')
    return new_user_data


def authorize_user(email, password, db_email, db_password):
    """
    Authorization of registration data
    :param email:
    :param password:
    :param db_email:
    :param db_password:
    :return:
    """
    if email in db_email:  # str email in db_email tuple
        if password == db_password:
            print("Welcome back, {}!. You are successfully signed in!".format(email))
        else:
            print("Sorry, {}! Login data is wrong.\nPlease register new account or check login data.".format(email))
            hi_user()


# function to keep the active session name
# create table Sessions to keep all session names and time
def write_down_active_user_name(user_name):
    # update_values_sessions(create_connection(), session = (user_name, start_time, end_time))
    filename = 'active_user_name.txt'
    with open(filename, 'w') as f:
        f.write(user_name)
        f.close()


def run_welcome() -> str:
    """
    Launch of login, registration and authorization logics
    :return: user_name string value
    """
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
        user_name = input_email
        # print(user_name)
        write_down_active_user_name(user_name)
        return user_name
    if login_or_register == 'r':
        new_user = register_user()
        print("----- New user data: -----\n", new_user)
        update_values_user(connection=create_connection(),
                           user_data=new_user)
        user_name = new_user[0]
        # print(user_name)
        write_down_active_user_name(user_name)
        return user_name


if __name__ == "__main__":
    run_welcome()
