"""Challenge Question Class."""
from __future__ import annotations


class Point:
    """Class to represent (x,y) coordinate point."""
    
    x: float
    y: float
    
    def __init__(self, init_x: float = 0.0, init_y: float = 0.0):
        """Construct a point."""
        self.x = init_x
        self.y = init_y
    
    def scale_by(self, factor: int) -> None:
        """Modify (or mutate) a point."""
        self.x *= factor
        self.y *= factor
        
    def scale(self, factor: int) -> Point:
        """Make a new point."""
        return Point(self.x * factor, self.y * factor)
    
    def __str__(self) -> str:
        """Printable string."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point:
        """Make a new point."""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, factor: int | float) -> Point:
        """Make a new point."""
        return Point(self.x + factor, self.y + factor)
    
