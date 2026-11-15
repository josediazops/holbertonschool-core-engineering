#!/usr/bin/env python3
"""Demonstrates inheritance and polymorphism."""


class Animal:
    """Represents a generic animal."""

    def speak(self):
        """Return a generic animal sound."""
        return "Some sound"


class Dog(Animal):
    """Represents a dog."""

    def speak(self):
        """Return the dog's sound."""
        return "Woof"


class Cat(Animal):
    """Represents a cat."""

    def speak(self):
        """Return the cat's sound."""
        return "Meow"


animals = [Dog(), Cat(), Dog()]


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

print(issubclass(Dog, Animal))
