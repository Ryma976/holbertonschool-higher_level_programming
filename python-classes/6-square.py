#!/usr/bin/python3
"""
This module defines a class Square with size and position validations.
"""


class Square:
    """
    A class that defines a square by its size and position offset.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with validation directly inside init.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the private size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the private size attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the private position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the private position attribute with validation."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' with positional spacing."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
