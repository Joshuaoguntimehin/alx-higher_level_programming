#!/usr/bin/python3
class Rectangle:
    def __init__(self, width):
        self.width = _width
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
    
    def __init__(self, height):
        self.height = height
    @property
    def height(self):
        self.height = _height
        return self.height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
    
    def __init__(self, width=0, height=0):
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative")
        self._width = width
        self._height = height
