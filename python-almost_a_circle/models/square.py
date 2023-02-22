#!/usr/bin/python3
'''Writing a Square subclass'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square is a subclass'''
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        '''Overriding the square class'''
        return f"[Square] ({self.id})\
 {self.x}/{self.y} - {self.size}"
