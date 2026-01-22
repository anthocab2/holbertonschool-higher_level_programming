#!/usr/bin/python3
"""
6-print_sorted_dictionary
Module that provides a function to print a dictionary
by ordered keys (alphabetically) at the first level only.
"""


def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys (alphabetically).

    Args:
        a_dictionary (dict): The dictionary to print
    """
    # Get the sorted keys
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
