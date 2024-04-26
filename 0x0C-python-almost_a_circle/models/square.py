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
        super().__init__(x=x, y=y, width=size, height=size, id=id)
        self.size = size

    @property
    def size(self):
        """ Getter and setter for width """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """returning the values"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        if args:
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                else:
                    continue

        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    iself.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                # removed the break statement, incase
                # than 5, and one of the attributes is at the end
