import os
import logging

current_dir = os.path.abspath(os.path.dirname(__file__))

USER_NAME_FILE = os.path.join(current_dir, "active_user_name.txt")
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger('config file')




def read_file_user_name():
    filename = USER_NAME_FILE
    with open(filename, 'r') as f:
        user_name = f.read()
        f.close()
    return user_name


if __name__ == "__main__":
    LOG.info("get active user from config")
    # read_transactions_table()
    read_file_user_name()
