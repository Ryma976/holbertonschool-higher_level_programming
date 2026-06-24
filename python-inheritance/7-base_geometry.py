#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value=None):
        """Validate a parameter as an integer."""
        if value is None and type(name) is str:
            raise TypeError("{} must be an integer".format(name))
        if type(value) is not int or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
