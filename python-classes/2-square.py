#!/usr/bin/python3
"""
This module defines a class Square with an optional size and type validation.
"""


class Square:
    """
    A class that defines a square by its size with input validation.
    """

    def __init__(self, size=0):
        """
        Initializes the square with validation.

        Args:
            size (int): The size of the square's sides. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
