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
        vector_y = self.__y
        vector_x = self.__x
        for ind_vec in range(vector_y):
            print("")
        for ind in range(rect_h):
            print(" " * vector_x + "#" * rect_w)

    def __str__(self) -> str:
        '''Overriding the rectangle class'''
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}"

    def update(self, *args):
        '''Assigns an argument to each attribute'''
        len_args = len(args)
        if len_args == 1:
            self.id = args[0]
        if len_args == 2:
            self.width = args[1]
        if len_args == 3:
            self.height = args[2]
        if len_args == 4:
            self.x = args[3]
        if len_args == 5:
            self.y = args[4]
