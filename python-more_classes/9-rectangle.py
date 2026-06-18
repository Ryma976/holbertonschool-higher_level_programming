#!/usr/bin/python3
"""
This module defines a Rectangle with a class method for square creation.
"""


class Rectangle:
    """
    Defines a rectangle with custom properties, counters, and factory methods.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle and increments the instance counter.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retrieves the private width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width with integer validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the private height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height with integer validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles based on their area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance representing a square.

        Args:
            size (int): The width and height of the square.

        Returns:
            Rectangle: A new Rectangle instance where width == height == size.
        """
        return cls(size, size)

    def __str__(self):
        """Returns a string representation using the print_symbol attribute."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol_str = str(self.print_symbol)
        rect_lines = [symbol_str * self.__width for _ in range(self.__height)]
        return "\n".join(rect_lines)

    def __repr__(self):
        """Returns a string representation to recreate the instance."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message and decrements the counter upon deletion."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
