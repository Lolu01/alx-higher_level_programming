#!/usr/bin/python3

""" Json string to object"""


def from_json_string(my_str):
    """ Json string to object"""
    import json
    return json.loads(my_str)
