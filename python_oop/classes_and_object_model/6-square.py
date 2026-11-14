#!/usr/bin/env python3
"""Defines a square class with size validation"""


class Square:
    """Represents a square."""

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

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a validated size and position."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    @property
    def position(self):
        """Retrieves the square postion."""
        return self.__position

    @position.setter
    def position(self, pvalue):
        """Sets the square position."""
        if not isinstance(pvalue, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(pvalue) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(pvalue[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if pvalue[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(pvalue[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if pvalue[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = pvalue

    def my_print(self):
        """Prints the square using the "#" character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns the square as a string."""
        if self.__size == 0:
            return ""
        result = ""
        for i in range(self.__position[1]):
            result += "\n"
        for i in range(self.__size):
            if i > 0:
                result += "\n"
            result += " " * self.__position[0] + "#" * self.__size
        return result
