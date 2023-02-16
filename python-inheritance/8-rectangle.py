#!/usr/bin/python3
'''BaseGeometry class inheritance practice.'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''This is a subclass'''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        bg = BaseGeometry()

        bg.integer_validator("width", self.__width)
        bg.integer_validator("height", self.__height)
