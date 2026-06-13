#!/usr/bin/python3
"""
This module provides a simple function to add two numbers.
It includes validation checks to ensure both arguments are integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (casted to integers).

    Args:
        a: The first number. Must be an int or float.
        b: The second number. Must be an int or float. Defaults to 98.

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an integer or float,
                   or if they are NaN or Infinity.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for NaN or Infinity without importing math
    if a != a or a in [float('inf'), float('-inf')]:
        raise TypeError("a must be an integer")
    if b != b or b in [float('inf'), float('-inf')]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
