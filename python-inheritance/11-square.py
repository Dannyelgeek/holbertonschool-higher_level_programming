#!/usr/bin/python3
'''BaseGeometry class inheritance practice.'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''This is another subclass'''
    def __init__(self, size):
        self.__size = size

        bg = BaseGeometry()

        bg.integer_validator("size", self.__size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        return (self.__size * self.__size)
