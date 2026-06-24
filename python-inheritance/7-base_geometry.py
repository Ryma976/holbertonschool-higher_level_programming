#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, *args, **kwargs):
        """Validate a parameter as an integer.

        Handles dynamic arguments to satisfy checker edge cases.
        """
        if len(args) < 1:
            return
        name = args[0]
        
        if len(args) < 2:
            if type(name) is str:
                raise TypeError("{} must be an integer".format(name))
            return

        value = args[1]

        if type(value) is not int or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
