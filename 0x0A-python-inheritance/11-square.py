#!/usr/bin/python3

"""Square class module"""


rectangle_class = __import__('9-rectangle').Rectangle


class Square(rectangle_class):
    """Square class"""

    def __init__(self, size):
        """init method"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """area method"""
        return self.__size ** 2

    def __str__(self):
        """str method"""
        return "[Square] {}/{}".format(self.__size, self.__size)
