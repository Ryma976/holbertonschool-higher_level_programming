#!/usr/bin/env python3
"""Defines Shape, Circle, Rectangle, and shape_info."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Represents a circle."""

    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
