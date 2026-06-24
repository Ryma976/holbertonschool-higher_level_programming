#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        To satisfy the checker validation:
        integer_validator()
        integer_validator("age")
        integer_validator("age", 1)
        integer_validator("age", 0)
        integer_validator("age", -4)
        integer_validator("age", "4")
        integer_validator("age", (4,))
        integer_validator("age", [3])
        integer_validator("age", True)
        integer_validator("age", {3, 4})
        integer_validator("age", None)
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
