#!/usr/bin/python3
"""
1-safe_print_integer.py
Module to safely print an integer using try/except.
"""


def safe_print_integer(value):
    """
    Prints an integer using "{:d}".format() safely.

    Args:
        value: value to print

    Returns:
        True if value was an integer and printed, False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
