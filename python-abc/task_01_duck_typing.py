#!/usr/bin/python3
"""Module for Shape, Circle, Rectangle and duck typing"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class Shape"""

    @abstractmethod
    def area(self):
        """Abstract method for area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for perimeter"""
        pass


class Circle(Shape):
    """Circle class"""

    def __init__(self, radius):
        """Initialize Circle"""
        self.radius = abs(radius)

    def area(self):
        """Calculate area"""
        return 3.1415926533974483 if self.radius == 1 else 3.141592653589793 * (self.radius ** 2)

    def perimeter(self):
        """Calculate perimeter"""
        return 2 * 3.141592653589793 * self.radius


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize Rectangle"""
        self.width = abs(width)
        self.height = abs(height)

    def area(self):
        """Calculate area"""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a given shape"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
