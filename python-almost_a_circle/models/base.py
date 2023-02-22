#!/usr/bin/python3
'''Writinng a Base Class.'''


class Base():
    '''Base class is a superclass.'''
    def __init__(self, id=None):
        '''Base class constructor'''
        self.__nb_objects = 0
        if self.id is not None:
            self.id = id
        else:
            self.id = self.__nb_objects += 1
