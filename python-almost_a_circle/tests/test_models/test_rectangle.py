#!/usr/bin/python3
'''Testing Rectangle class.'''
import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Class for test Rectangle class'''

    def test_init(self):
        '''Testing instances of the Rectangle class.'''
        t1 = Rectangle(1, 2)
        t2 = Rectangle(6, 9, 0, 0 ,12)
        
        def test_errors(self):
            with self.assertRaises(TypeError):
                rectangle = Rectangle("1", 2)
            with self.assertRaises(TypeError):
                rectangle = Rectangle(1, "2")
            with self.assertRaises(TypeError):
                rectangle = Rectangle(1, 2, 3, "4")
            with self.assertRaises(TypeError):
                rectangle = Rectangle(1, 2, "3", 4)

            with self.assertRaises(ValueError):
                rectangle = Rectangle(-1, 2)
            with self.assertRaises(ValueError):
                rectangle = Rectangle(1, -2)
            with self.assertRaises(ValueError):
                rectangle = Rectangle(0, 2)
            with self.assertRaises(ValueError):
                rectangle = Rectangle(1, 0)
            with self.assertRaises(ValueError):
                rectangle = Rectangle(1, 2, -3)
            with self.assertRaises(ValueError):
                rectangle = Rectangle(1, 2, 3, -4)

        self.assertEqual(t1.id, 20)
        self.assertEqual(t2.id, 12)

    def test_area(self):
        '''Testing area method'''
        t3 = Rectangle(3, 2)
        t4 = Rectangle(8, 7, 0, 0, 12)
        t5 = Rectangle(999, 999)

        self.assertEqual(t3.area(), 6)
        self.assertEqual(t4.area(), 56)
        self.assertEqual(t5.area(), 998001)

    def test_display(self):
        '''Testing test_display method'''

        

if __name__ == "__main__":
    unittest.main()