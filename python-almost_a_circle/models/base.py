#!/usr/bin/python3
'''Writinng a Base Class.'''
import json


class Base():
    '''Base class is a superclass.'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Base class constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
