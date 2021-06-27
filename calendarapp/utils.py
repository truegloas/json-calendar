import json


def open_json_file(path_to_file):
    with open(path_to_file, encoding='utf-8') as f:
        data = json.load(f)
        pass
    return data