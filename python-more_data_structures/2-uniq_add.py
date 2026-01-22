#!/usr/bin/python3
"""
2-uniq_add
Module that provides a function to sum all unique integers in a list.
"""


def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once per integer).

    Args:
        my_list (list): List of integers

    Returns:
        int: Sum of unique integers
    """
    # Convert the list to a set to keep only unique values, then sum
    return sum(set(my_list))
