#!/usr/bin/python3
"""
Defines a square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represent a square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square.
        """
        self.size = size
        super().__init__(x=x, y=y, width=size, height=size, id=id)

    def __str__(self):
        """returning the values"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
