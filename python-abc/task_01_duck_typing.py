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
<<<<<<< HEAD
    """
    Prints the area and perimeter of a given shape using duck typing.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
=======
"""Print area and perimeter."""
print(f"Area: {shape.area()}")
print(f"Perimeter: {shape.perimeter()}")
>>>>>>> ead3a0d91ca24bbf4d20b97fdd535e66cfede865
