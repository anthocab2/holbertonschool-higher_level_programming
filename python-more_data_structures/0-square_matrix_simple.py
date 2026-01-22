#!/usr/bin/python3
"""
0-square_matrix_simple
Module that provides a function to compute
the square of all integers in a matrix.
"""


def square_matrix_simple(matrix=[]):
    """
    Computes the square of all integers in a 2D matrix.

    Args:
        matrix (list of lists): 2D list of integers.

    Returns:
        list of lists: new 2D matrix with squared values.
    """
    # Using list comprehension to create a new matrix
    return [[value ** 2 for value in row] for row in matrix]
