import json
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'json_input.json')


def read_json(json_file):
    """
    Read JSON file as a dict data, extract the necessary ticker info
    :param file name:
    :return: dictionary
    """
    with open(json_file, 'r') as f:
        json_str = f.read()
        list_dump = json.loads(json_str)
    # print(type(list_dump))
    # print(list_dump[0])
    return list_dump


read_json(json_file=file_path)
