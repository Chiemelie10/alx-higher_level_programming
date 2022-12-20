#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the square

        Args:
            size: The size (int) of the new square.
        """
        self.size = size
    
    @property
    def size(self):
        """Retrieves the size of the square."""

        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square."""

        self.__size = value
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Returns the area of the square."""
    
        return (self.__size ** 2)
