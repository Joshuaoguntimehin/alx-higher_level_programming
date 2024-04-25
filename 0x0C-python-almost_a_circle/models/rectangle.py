#!/usr/bin/python3
""" importing from base.py """
from models.base import Base


class Rectangle(Base):
    """Class Doc."""
    def __init__(self, width, height, x=0, y=0,id=None):
        super().__init__()
        if id is None:
            self.id = id 
        else:

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Getter and setter for height"""
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Getter and setter for height"""
        return self.__height

    @height.setter
    def set_height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter and setter for height"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
                raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter and setter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif y < 0:
                raise ValueError("y must be >= 0")
        self.__y = value