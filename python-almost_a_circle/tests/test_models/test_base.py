#!/usr/bin/python3
'''Testing Base class.'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Class for test Base class'''
    def test_init(self):
        '''Testing instances of th Base class.'''
        t1 = Base()
        self.assertEqual(t1.id, 1)

if __name__ == "__main__":
    unittest.main()
