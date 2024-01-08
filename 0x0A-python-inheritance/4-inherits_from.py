#!/usr/bin/python3

"""returns true if object is an instance of class"""


def inherits_from(obj, a_class):
    """returns true if object is an instance of class"""
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
