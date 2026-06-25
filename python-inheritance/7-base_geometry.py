#!/usr/bin/python3
"""Module for BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
