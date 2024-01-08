#!/usr/bin/python3

""" Add attribute module """


def add_attribute(obj, name, value):
    """ Adds a new attribute to an object if it’s possible """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
