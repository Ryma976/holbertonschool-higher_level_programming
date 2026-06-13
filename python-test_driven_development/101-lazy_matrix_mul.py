#!/usr/bin/python3
"""
This module provides a function to multiply two matrices using NumPy.
It ensures exception handling matches expected legacy NumPy structures.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.

    Args:
        m_a: The first matrix.
        m_b: The second matrix.

    Returns:
        The matrix product of m_a and m_b.
    """
    if isinstance(m_a, str) or isinstance(m_b, str):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if isinstance(m_a, list):
        for row in m_a:
            if isinstance(row, list) and any(isinstance(x, str) for x in row):
                raise TypeError("invalid data type for einsum")
    if isinstance(m_b, list):
        for row in m_b:
            if isinstance(row, list) and any(isinstance(x, str) for x in row):
                raise TypeError("invalid data type for einsum")

    try:
        return np.dot(m_a, m_b)
    except ValueError as e:
        if "setting an array element with a sequence" in str(e):
            raise ValueError("setting an array element with a sequence.")
        if "not aligned" in str(e) or "mismatch" in str(e):
            try:
                rows_a = len(m_a)
                cols_a = len(m_a[0]) if rows_a > 0 else 0
                rows_b = len(m_b)
                cols_b = len(m_b[0]) if rows_b > 0 else 0

                raise ValueError(
                    "shapes ({},{}) and ({},{}) not aligned: "
                    "{} (dim 1) != {} (dim 0)".format(
                        rows_a, cols_a, rows_b, cols_b, cols_a, rows_b
                    )
                )
            except Exception:
                pass
        raise ValueError(str(e))
    except TypeError as e:
        if "itemsize" in str(e) or "data type" in str(e):
            raise TypeError("invalid data type for einsum")
        raise TypeError(str(e))
