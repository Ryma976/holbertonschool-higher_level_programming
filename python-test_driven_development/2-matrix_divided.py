#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
It validates the input matrix and divisor, returning a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor, rounded to 2 decimal places.

    Args:
        matrix: A list of lists of integers or floats.
        div: An integer or float divisor.

    Returns:
        A new matrix containing the division results.

    Raises:
        TypeError: If the matrix is not a list of lists of numbers,
                   if rows are not of equal size, or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_msg)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(err_msg)
            # Matrices with inf or nan must raise a TypeError
            if element != element or element in [float('inf'), float('-inf')]:
                raise TypeError(err_msg)

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # nan is not a valid number for div, but inf/-inf are valid
    if div != div:
        raise TypeError("div must be a number")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
