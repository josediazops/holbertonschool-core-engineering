#!/usr/bin/env python3
"""Demonstrates multiple inheritance using Fish and Bird."""


class Fish:
    """Represents a fish."""

    def swim(self):
        """Print the fish's swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """Represents a bird."""
    def fly(self):
        """Print the bird's flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a fish that can fly."""

    def fly(self):
        """Print the flying fish's flying behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print the flying fish's flying behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the flying fish's swimming behavior."""
        print("The flying fish lives both in water and the sky!")
