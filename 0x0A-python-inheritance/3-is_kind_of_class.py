#!/usr/bin/python3
'''Module for is_kind_of_class method.'''


def is_kind_of_class(obj, a_class):
    '''Determines if an object is a subclass of a class.'''
    if isinstance(obj, a_class):
        return True
    else:
        return False

