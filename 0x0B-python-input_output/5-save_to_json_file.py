#!/usr/bin/python3

""" Save json to file """


def save_to_json_file(my_obj, filename):
    """ Save json to file """
    import json
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
