#!/usr/bin/python3
'''Module for Rectangle class.'''


class BaseGeometry:
    pass


class Rectangle(BaseGeometry):
    '''A subclass representing a rectangle.'''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        if type(height) != int:
            raise TypeError("height must be an integer")
