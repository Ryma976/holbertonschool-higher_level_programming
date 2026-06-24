#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance of,
or inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        bool: True if obj is an instance or subclass instance, otherwise False.
    """
    return isinstance(obj, a_class)
