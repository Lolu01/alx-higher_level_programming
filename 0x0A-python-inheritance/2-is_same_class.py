#!/usr/bin/python3

""" Function that returns  true if the object is an instance of a class that"""


def is_same_class(obj, a_class):
    """ Function that returns  true if the object is an instance of a class"""
    if type(obj) is a_class:
        return True
    else:
        return False
