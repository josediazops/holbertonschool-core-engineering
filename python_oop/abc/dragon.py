#!/usr/bin/env python3
"""Demonstrates mixins using a Dragon class."""


class SwimMixin:
    """Provides swimming behavior."""

    def swim(self):
        """Print the swimming behavior."""
        print("The creature swims!")


class Flymixin:
    """Provides flying behavior."""

    def fly(self):
        """Print the flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, Flymixin):
    """Represents a dragon with swimming and flying abilities."""

    def roar(self):
        """Print the dragon's roar."""
        print("The dragon roars!")
