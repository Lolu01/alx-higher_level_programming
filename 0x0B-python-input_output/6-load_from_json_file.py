#!/usr/bin/python3

""" Load json module """


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file” """
    import json
    with open(filename, 'r') as f:
        return json.load(f)
