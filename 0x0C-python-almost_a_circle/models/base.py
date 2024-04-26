#!/usr/bin/python3
"""
Defines a base model class.
"""
import json


class Base:
    """
    Represents the base model
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None:
            return"[]"
        to_json = json.dumps(list_dictionaries)

        return to_json
