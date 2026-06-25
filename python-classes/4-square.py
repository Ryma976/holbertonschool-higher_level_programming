#!/usr/bin/python3
"""
This module defines a class Square with properties for getter and setter logic.
"""


class Square:
    """
    A class that defines a square by its size, with property-based validation.
    """

    def __init__(self, size=0):
        """
        Initializes the square with an optional size.

        Args:
            size (int): The size of the square's sides. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the private size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the private size attribute with type and value validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the current area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2
