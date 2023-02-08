#!/usr/bin/python3
'''Instantinate size in the Square class.'''


class Square:
    '''Instatinate size with a value.'''
    def __init__(self, size=0):
        if size == int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
