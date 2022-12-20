#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes the new square.

        Args:
            size: The size (int) of the square set to 0
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Returns the area of the square."""

        square_area = self.__size ** 2
        return square_area
