#!/usr/bin/env python3
"""Defines a square class with size validation"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a square with a validated size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieves the square size."""
        return self.__size

    @size.setter
    def size(self, svalue):
        """Sets the square size."""
        if not isinstance(svalue, int):
            raise TypeError("size must be an integer")
        if svalue < 0:
            raise ValueError("size must be >= 0")
        self.__size = svalue

    def my_print(self):
        """Prints the square using the "#" character."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
