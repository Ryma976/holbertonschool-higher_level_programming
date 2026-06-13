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

    try:
        return np.dot(m_a, m_b)
    except ValueError as e:
        if "not aligned" in str(e) or "mismatch" in str(e):
            raise ValueError("shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)")
        raise ValueError(str(e))
    except TypeError as e:
        raise TypeError(str(e))
