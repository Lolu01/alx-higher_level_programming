#!/usr/bin/python3
"""Rectangle class module"""


geo_class = __import__('7-base_geometry').BaseGeometry


class Rectangle(geo_class):
    """Rectangle class"""

    def __init__(self, width, height):
        """init method"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
