#!/usr/bin/python3
"""
This is a geometry module where we validate data types.
"""


class BaseGeometry:
    """
    A geometry class that has methods for area and validation.
    """

    def area(self):
        """
        This method will raise an error because it is not built yet.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method checks if the value is a valid positive integer.
        """
        if type(value) is bool or type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
