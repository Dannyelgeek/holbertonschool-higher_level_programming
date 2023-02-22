#!/usr/bin/python3
'''Writing a Rectangle subclass'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle is a subclass'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        '''Width private instance'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''Set attribute value.'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Height private instance'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''Set attribute value.'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''X private instance'''
        return (self.__x)

    @x.setter
    def x(self, value):
        '''Set attribute value.'''
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Y private instance'''
        return (self.__y)

    @y.setter
    def y(self, value):
        '''Set attribute value.'''
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Returns rectangle's area'''
        area_w = self.__width
        area_h = self.__height
        return (area_w * area_h)

    def display(self):
        '''Prints a rectangle in stdout'''
        rect_w = self.__width
        rect_h = self.__height
        for ind in range(rect_h):
            print("#" * rect_w)
