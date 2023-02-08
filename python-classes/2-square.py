#!/usr/bin/python3
'''Instantinate size in the Square class.'''


class Square:
    '''Instatinate size with a value.'''
    def __init__(self, size=0):
        try:
            self.__size = size
        except ValueError:
            raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
