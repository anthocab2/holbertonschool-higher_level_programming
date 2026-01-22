#!/usr/bin/python3
"""
3-common_elements
Module that provides a function to return a set of common elements
between two sets.
"""


def common_elements(set_1, set_2):
    """
    Returns a set of elements present in both set_1 and set_2.

    Args:
        set_1 (set): First set
        set_2 (set): Second set

    Returns:
        set: Set of common elements
    """
    # Using set intersection to find common elements
    return set_1 & set_2
