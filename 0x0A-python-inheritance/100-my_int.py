#!/usr/bin/python3

"""Myint module"""


class MyInt(int):
    """MyInt class"""
    def __eq__(self, other):
        """eq method"""
        return int(self) != int(other)

    def __ne__(self, other):
        """ne method"""
        return int(self) == int(other)
