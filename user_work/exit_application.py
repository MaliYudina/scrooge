"""
Exit_application_app closes the application
"""

# TODO make module with global variables
ACTIVE_USER_NAME = "test_user_name"
user_name = ACTIVE_USER_NAME


def exit_app():
    """
    Quit application
    :return: None
    """
    print(f'{user_name}, bye bye!')
    answer = input("Are you sure to quit? (y/n) ")
    if answer == 'y':
        action = quit()
        return action
    else:
        # call app menu again
        pass


