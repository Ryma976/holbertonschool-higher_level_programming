#!/usr/bin/python3
"""
This module provides a function to multiply two matrices using NumPy.
It lets NumPy handle validations and alignments natively.
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

    return np.matmul(m_a, m_b)
