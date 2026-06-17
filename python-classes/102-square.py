#!/usr/bin/python3
"""
This module defines a class Square with numeric size validation
and full rich comparison operator capabilities based on area.
"""


class Square:
    """
    Defines a square by its size and allows comparison based on its area.
    """

    def __init__(self, size=0):
        """
        Initializes the square with an optional size.

        Args:
            size (int or float): The size of the square's sides.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the private size attribute.

        Returns:
            int or float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the private size attribute with float/integer number validation.

        Args:
            value (int or float): The new size of the square.

        Raises:
            TypeError: If value is not a float or an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the current area of the square.

        Returns:
            int or float: The area of the square (size squared).
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Handles the == comparison based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Handles the != comparison based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Handles the < comparison based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Handles the <= comparison based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Handles the > comparison based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Handles the >= comparison based on area."""
        return self.area() >= other.area()
