#!/usr/bin/python3
'''Set the width and height attributes.'''


class Rectangle:
    '''width will be a private attribute'''
    def __init__(self, width=0, height=0):
        self.width == width
        self.height == height 

    @property
    def width(self):
        '''Width attribute privacy.'''
        return (self.__width)

    @property
    def height(self):
        '''height attribute privacy'''
        return (self.__height)

    @width.setter
    def width(self, value):
        '''Set width value.'''
        if isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width == value

    @height.setter
    def height(self, value):
        '''Set height value.'''
        if isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
