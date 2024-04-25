#!/usr/bin/python3
class Base:
    '''class doc'''
    __nb_objects = 0

    def __init__(self, id=None):
        """using if statement for id"""
        if id is not None:
            self.id = id
        else:
            """for if id id none"""
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
