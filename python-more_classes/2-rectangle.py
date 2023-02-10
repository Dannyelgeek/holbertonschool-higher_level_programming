#!/usr/bin/python3
'''Calculate the area and the perimeter of the rectangle'''


class Rectangle:
    '''width will be a private attribute'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Width attribute privacy.'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''Set width value.'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''height attribute privacy'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''Set height value.'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Rectangle area.'''
        area_w = self.__width
        area_h = self.__height
        return (area_w * area_h)

    def perimeter(self):
        '''Rectangle perimeter'''
        per_w = self.__width
        per_h = self.__height
        if per_h == 0 or per_w == 0:
            return 0
        else:
            return (2 * (per_w + per_h))
