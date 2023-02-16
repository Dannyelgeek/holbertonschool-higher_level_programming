#!/usr/bin/python3
'''BaseGeometry class inheritance practice.'''


class BaseGeometry():
    '''This is a superclass.'''
    def area(self):
        '''Raise a exception'''
        raise Exception("area() is not implemented")
