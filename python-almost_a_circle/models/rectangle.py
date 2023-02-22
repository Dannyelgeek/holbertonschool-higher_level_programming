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
        self.__width = value

    @property
    def height(self):
        '''Height private instance'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''Set attribute value.'''
        self.__height = value

    @property
    def x(self):
        '''X private instance'''
        return (self.__x)

    @x.setter
    def x(self, value):
        '''Set attribute value.'''
        self.__x = value

    @property
    def y(self):
        '''Y private instance'''
        return (self.__y)

    @y.setter
    def y(self, value):
        '''Set attribute value.'''
        self.__y = value
