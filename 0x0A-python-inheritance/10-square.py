#!/usr/bin/python3
'''Module for Rectangle class.'''


class Rectangle:
    pass


class Square(Rectangle):
    '''A subclass representing a rectangle.'''
    def __init__(self, size):
        self._size = size
        if type(size) != int:
            raise TypeError("size must be an integer")

    def area(self):
        '''Method for area of square.'''
        return self._size ** 2

    def __str__(self):
        return f"[Square] {self._size}/{self._size}"

