#!/usr/bin/python3
"""
This module provides the print_square function.
It validates a size input and prints a square using the '#' character.
"""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size: The side length of the square. Must be an integer.

    Raises:
        TypeError: If size is not an integer (or if it's a negative float).
        ValueError: If size is less than 0.
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
