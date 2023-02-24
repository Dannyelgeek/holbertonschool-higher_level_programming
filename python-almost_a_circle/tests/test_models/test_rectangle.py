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

    def test_update(self):
        '''Testing update method'''
        t12 = Rectangle(3, 2)
        t13 = Rectangle(8, 7, 0, 0, 12)
        t14 = Rectangle(3, 2, 1)
        t15 = Rectangle(3, 2, id="holberton")
        t16 = Rectangle(3, 2, id="holberton")

        t12.update(5, 7)
        self.assertEqual(t12.__str__(), '[Rectangle] (26) 0/0 - 7/2')
        with self.assertRaises(ValueError):
            t13.update(**{'id': 1337, 'x': -1})
            t14.update("stringid", None, None)
        t15.update(None)
        self.assertEqual(t15.__str__(), '[Rectangle] (None) 0/0 - 3/2')
        t16.update(-5)
        self.assertEqual(t16.__str__(), '[Rectangle] (-5) 0/0 - 3/2')

    def test_to_dictionary(self):
        '''Testing to_dictionary method'''
        t17 = Rectangle(3, 2)
        t18 = Rectangle(8, 7, 0, 0, 12)
        t19 = Rectangle(3, 2, 1)
        t20 = Rectangle(3, 2, id="holberton")

        r17 = {'id': 24, 'width': 3, 'height': 2, 'x': 0, 'y': 0}
        r18 = {'id': 12, 'width': 8, 'height': 7, 'x': 0, 'y': 0}
        r19 = {'id': 25, 'width': 3, 'height': 2, 'x': 1, 'y': 0}
        r20 = {'id': 'holberton', 'width': 3, 'height': 2, 'x': 0, 'y': 0}

        self.assertDictEqual(t17.to_dictionary(), r17)
        self.assertDictEqual(t18.to_dictionary(), r18)
        self.assertDictEqual(t19.to_dictionary(), r19)
        self.assertDictEqual(t20.to_dictionary(), r20)


if __name__ == "__main__":
    unittest.main()