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
        with self.assertRaises(TypeError):
            t3 = Rectangle("string")
            t4 = Rectangle(None)
            t5 = Rectangle(float("inf"))
            t6 = Rectangle(3.6, 9.1)
            t7 = Rectangle(-8, 9)
            t8 = Rectangle()

        self.assertEqual(t1.id, 18)
        self.assertEqual(t2.id, 12)

if __name__ == "__main__":
    unittest.main()