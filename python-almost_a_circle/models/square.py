#!/usr/bin/python3
'''Writing a Square subclass'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square is a subclass'''
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''size private instance'''
        return (self.__width)

    @size.setter
    def size(self, value):
        '''Set attribute value.'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def __str__(self) -> str:
        '''Overriding the square class'''
        return f"[Square] ({self.id})\
 {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        '''Assigns an argument to each attribute'''
        if args:
            len_args = len(args)
            if len_args == 1:
                self.id = args[0]
            if len_args == 2:
                self.size = args[1]
            if len_args == 3:
                self.x = args[2]
            if len_args == 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)