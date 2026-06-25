#!/usr/bin/env python3
"""
Module for Shape, Circle, Rectangle and shape_info
Using ABC and Duck Typing
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class representing a generic Shape"""

    @abstractmethod
    def area(self):
        """Abstract method to calculate area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate perimeter"""
        pass


class Circle(Shape):
    """Concrete class representing a Circle"""

    def __init__(self, radius):
        """Initialize Circle with radius"""
        self.radius = radius

    def area(self):
        """Calculate and return circle area"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return circle perimeter"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class representing a Rectangle"""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return rectangle perimeter"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape using duck typing.
    No isinstance check is performed.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
