#!/usr/bin/python3
"""Module defines BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value"""
        if type(value) i            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))






