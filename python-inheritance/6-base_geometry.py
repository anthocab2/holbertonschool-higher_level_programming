#!/usr/bin/python3
"""This module defines a geometry base class."""


class BaseGeometry:
    """A base geometry class with an area method."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")
