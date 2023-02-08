#!/usr/bin/python3
'''print the square in Square class.'''


class Square:
    '''Get and set the square's size.'''
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        '''Get the size's value.'''
        return(self.__size)

    @size.setter
    def size(self, value):
        '''Set the size's value'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Return the square's area.'''
        return (self.__size * self.__size)

    def my_print(self):
        hash = "#"
        if self.size == 0:
            print()
        else:
            for ind in range(self.size):
                print(hash, end="")
                print(hash * (self.size - 1))
