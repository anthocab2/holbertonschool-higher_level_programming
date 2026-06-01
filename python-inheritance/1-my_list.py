#!/usr/bin/python3
"""This module defines a custom list class."""


class MyList(list):
    """A class that inherits from list."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
