# polymorphism_demo.py

import math

class Shape:
    """A base class representing a generic shape."""

    def area(self):
        """Calculate the area of the shape. To be overridden by derived classes."""
        raise NotImplementedError("The area method must be overridden by the subclass")

class Rectangle(Shape):
    """A class representing a rectangle, inheriting from Shape."""

    def __init__(self, length, width):
        """Initialize the Rectangle instance with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """A class representing a circle, inheriting from Shape."""

    def __init__(self, radius):
        """Initialize the Circle instance with radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2
