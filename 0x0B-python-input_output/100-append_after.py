#!/usr/bin/python3

""" append after module"""


def append_after(filename="", search_string="", new_string=""):
    """append after function"""
    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            if search_string in line:
                line = line + new_string
            f.write(line)
