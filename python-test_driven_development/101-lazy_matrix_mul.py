#!/usr/bin/python3
"""
This module provides a function to multiply two matrices using NumPy.
It leverages NumPy's built-in vectorization and validation mechanisms.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.

    Args:
        m_a: The first matrix (list of lists of integers/floats).
        m_b: The second matrix (list of lists of integers/floats).

    Returns:
        The matrix product of m_a and m_b as a NumPy array.
    """
    return np.matmul(m_a, m_b)
