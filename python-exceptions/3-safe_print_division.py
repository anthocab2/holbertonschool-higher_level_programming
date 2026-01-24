#!/usr/bin/python3
"""
3-safe_print_division.py
Module to safely divide two integers with debug output.
"""


def safe_print_division(a, b):
    """
    Divides two integers and prints the result safely.

    Args:
        a (int): numerator
        b (int): denominator

    Returns:
        float or None: result of division, or None if error
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
