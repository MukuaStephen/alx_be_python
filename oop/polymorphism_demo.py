import math

class Shape:
    """A base class for different shapes."""
    
    def area(self):
        """Calculate the area of the shape."""
        raise NotImplementedError("Subclasses must override area()")


class Rectangle(Shape):
    """A class to represent a rectangle, inheriting from Shape."""
    
    def __init__(self, length: float, width: float):
        """Initialize a Rectangle instance."""
        self.length = length
        self.width = width

    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """A class to represent a circle, inheriting from Shape."""
    
    def __init__(self, radius: float):
        """Initialize a Circle instance."""
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)


