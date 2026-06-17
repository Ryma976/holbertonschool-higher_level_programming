#!/usr/bin/python3
"""
This module defines a class Square with size and position validations.
"""


class Square:
    """
    A class that defines a square by its size and position offset,
    and prints it to stdout.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with an optional size and position offset.

        Args:
            size (int): The size of the square's sides. Default is 0.
            position (tuple): A tuple of two positive integers for spacing.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the private position attribute.

        Returns:
            tuple: The position tuple of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the private position attribute with verification checks.

        Args:
            value (tuple): A tuple containing exactly two positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the current area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character, taking into account
        the position horizontal and vertical offsets.
        """
        if self.__size == 0:
            print()
            return

        # Print vertical empty lines (position[1])
        for _ in range(self.__position[1]):
            print()

        # Print each row with horizontal spaces (position[0])
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
