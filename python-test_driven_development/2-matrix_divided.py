#!/usr/bin/python3
"""Module for matrix division."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a number.

    Args:
        matrix: A list of lists containing integers or floats.
        div: The number used to divide each matrix element.

    Returns:
        A new matrix with all values divided by div, rounded to 2 decimals.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_size = len(matrix[0])

    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for number in row:
            if not isinstance(number, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(number / div, 2) for number in row] for row in matrix]
