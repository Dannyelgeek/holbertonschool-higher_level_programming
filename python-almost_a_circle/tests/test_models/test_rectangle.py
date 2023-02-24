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
            Rectangle("string")
            Rectangle("3", 6)
            Rectangle(3, "6")
            Rectangle(3, 6, "9")
            Rectangle(3, 6, 9, "12") 
            Rectangle(None)
            Rectangle(float("inf"))
            Rectangle(3.6, 9.1)
            raise TypeError()
        
        with self.assertRaises(ValueError):
            Rectangle(-8, 9)
            Rectangle(6, -9)
            Rectangle(0, 3)
            Rectangle(3, 0)
            Rectangle(3, 6, -9)
            Rectangle(3, 6, 9, -12)
            raise ValueError()

        self.assertEqual(t1.id, 21)
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
        t6 = Rectangle(3, 2)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            t6.display()
            self.assertEqual(fakeOutput.getvalue(), '###\n###\n')

        t7 = Rectangle(4, 5, 0, 1, 12)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            t7.display()
            self.assertEqual(fakeOutput.getvalue(),
                             '\n####\n####\n####\n####\n####\n')
        
    def test_str(self):
        '''Testing ___str___ method'''
        t8 = Rectangle(3, 2)
        t9 = Rectangle(8, 7, 0, 0, 12)
        t10 = Rectangle(3, 2, 1)
        t11 = Rectangle(3, 2, id="holberton")

        self.assertEqual(t8.__str__(), '[Rectangle] (22) 0/0 - 3/2')
        self.assertEqual(t9.__str__(), '[Rectangle] (12) 0/0 - 8/7')
        self.assertEqual(t10.__str__(), '[Rectangle] (23) 1/0 - 3/2')
        self.assertEqual(t11.__str__(), '[Rectangle] (holberton) 0/0 - 3/2')

        

if __name__ == "__main__":
    unittest.main()