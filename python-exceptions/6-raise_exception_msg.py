#!/usr/bin/python3
"""
6-raise_exception_msg.py
Module to raise a NameError exception with a custom message.
"""


def raise_exception_msg(message=""):
    """
    Raises a NameError exception with the given message.

    Args:
        message (str): message for the exception
    """
    raise NameError(message)
