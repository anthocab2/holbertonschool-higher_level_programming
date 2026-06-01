#!/usr/bin/python3
"""Defines mixins and a Dragon class."""


class SwimMixin:
    """Mixin that adds swimming behavior."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying behavior."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim, fly, and roar."""

    def roar(self):
        """Print dragon roaring behavior."""
        print("The dragon roars!")
