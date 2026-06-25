#!/usr/bin/env python3
"""Defines Shape, Circle, Rectangle, and shape_info."""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
"""Abstract shape class."""

```
@abstractmethod
def area(self):
    """Calculate area."""
    pass

@abstractmethod
def perimeter(self):
    """Calculate perimeter."""
    pass
```

class Circle(Shape):
"""Circle class."""

```
def __init__(self, radius):
    self.radius = radius

def area(self):
    return math.pi * (self.radius ** 2)

def perimeter(self):
    return 2 * math.pi * self.radius
```

class Rectangle(Shape):
"""Rectangle class."""

```
def __init__(self, width, height):
    self.width = width
    self.height = height

def area(self):
    return self.width * self.height

def perimeter(self):
    return 2 * (self.width + self.height)
```

def shape_info(shape):
"""Print area and perimeter."""
print(f"Area: {shape.area()}")
print(f"Perimeter: {shape.perimeter()}")
