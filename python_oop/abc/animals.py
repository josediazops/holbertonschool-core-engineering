#!/usr/bin/env python3
"""Defines an abstract Animal class and its subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound made by an animal."""
        pass


class Dog(Animal):
    """Represents a dog."""

    def sound(self):
        """Return the dog's sound."""
        return "Bark"


class Cat(Animal):
    """Represents a cat."""

    def sound(self):
        """Return the cat's sound."""
        return "Meow"
