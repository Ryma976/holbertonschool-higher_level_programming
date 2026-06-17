#!/usr/bin/python3
"""
This module defines a class Square with custom string representation.
"""


class Square:
    """
    Defines a square by its size and position offset,
    and supports direct string printing representation.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with size and position.
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
        """Prints the square using '#' with positional spacing to stdout."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Defines the printable behavior of the Square instance.
        Returns a string representation matching my_print output.
        """
        square_str = ""
        if self.__size == 0:
            return square_str

        # إضافة السطور الفارغة العمودية
        for _ in range(self.__position[1]):
            square_str += "\n"

        # بناء أسطر المربع مع المسافات الأفقية
        for i in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size
            if i < self.__size - 1:
                square_str += "\n"

        return square_str
