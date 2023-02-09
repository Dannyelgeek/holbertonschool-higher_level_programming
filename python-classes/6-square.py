#!/usr/bin/python3
'''print the square in Square class.'''


class Square:
    '''Get and set the square's size.'''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''Get the position's value'''
        return(self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for items in value:
            if type(items) != int or items < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Return the square's area.'''
        return (self.__size * self.__size)

    def my_print(self):
        hash = "#"
        if self.size == 0:
            print()
        else:
            for ind_1 in range(self.position[1]):
                print()
            for ind_2 in range(self.size):
                print(" " * (self.position[0]) + hash, end="")
                print(hash * (self.size - 1))
