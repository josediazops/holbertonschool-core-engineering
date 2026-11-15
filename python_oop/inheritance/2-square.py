#!/usr/bin/env python3
"""Defines the Square class."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize a square with a validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the square's area."""
        return self.__size * self.__size

    def __str__(self):
        """Return a readable description of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
