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

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes the JSON string representation of list_objs to a file'''
        class_list = []
        if list_objs is None:
            list_objs = []
        for ind in list_objs:
            class_list.append(ind.to_dictionary())
        with open(f"{cls.__name__}.json", mode='w', encoding="utf-8") as file:
            file.write(cls.to_json_string(class_list))