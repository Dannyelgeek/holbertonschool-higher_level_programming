#!/usr/bin/python3
'''Find the area in the Square class.'''


class Square:
    '''Return area of the square.'''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):

        return self.__size * self.__size
