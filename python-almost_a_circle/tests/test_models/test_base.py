#!/usr/bin/python3
'''Testing Base class.'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Class for test Base class'''
    def test_init(self):
        '''Testing instances of th Base class.'''
        t1 = Base()
        t2 = Base(6)
        self.assertEqual(t1.id, 1)
        self.assertEqual(t2.id, 6)

    def test_to_json_string(self):
        '''Testing to_json_string method'''
        t3 = Base(9)
        t4 = Base(1)
        t5 = Base() 
        self.assertEqual(t3.to_json_string(None), "[]")
        self.assertEqual(t4.to_json_string({"Name": "Daniel", "age": "29"}), '{"Name": "Daniel", "age": "29"}')
        self.assertEqual(t5.to_json_string([]), '[]')

if __name__ == "__main__":
    unittest.main()
