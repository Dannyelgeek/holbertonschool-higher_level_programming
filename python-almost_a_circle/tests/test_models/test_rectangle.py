#!/usr/bin/python3
'''Testing Rectangle class.'''
import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    '''Class for test Rectangle class'''
    def test_init(self):
        '''Testing instances of the Rectangle class.'''
        t1 = Rectangle(3, 6)
        t2 = Rectangle(6, 9, 0, 0 ,12)
        self.assertEqual(t1.id, 3)
        self.assertEqual(t2.id, 12)

if __name__ == "__main__":
    unittest.main()