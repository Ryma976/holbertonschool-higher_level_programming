#!/usr/bin/python3
"""
Module for Shape, Circle, Rectangle classes and duck typing function.
Handles negative input values by converting them to positive absolute values.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape."""

    def __init__(self, radius):
        """Initialize Circle, ensuring radius is always positive."""
        self.radius = abs(radius)

    def area(self):
        """Calculate and return circle area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return circle perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""

    def __init__(self, width, height):
        """Initialize Rectangle, ensuring dimensions are always positive."""
        self.width = abs(width)
        self.height = abs(height)

    def area(self):
        """Calculate and return rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a given shape using duck typing.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
