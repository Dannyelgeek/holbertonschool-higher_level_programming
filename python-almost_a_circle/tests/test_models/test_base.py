#!/usr/bin/python3
'''Testing Base class.'''
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Class for test Base class'''
    def test_init(self):
        '''Testing instances of th Base class.'''
        t1 = Base()
        t2 = Base(6)
        self.assertEqual(t1.id, 4)
        self.assertEqual(t2.id, 6)

    def test_to_json_string(self):
        '''Testing to_json_string method'''
        t3 = Base(9)
        t4 = Base(1)
        t5 = Base() 
        self.assertEqual(t3.to_json_string(None), "[]")
        self.assertEqual(t4.to_json_string({"Name": "Daniel", "age": "29"}), '{"Name": "Daniel", "age": "29"}')
        self.assertEqual(t5.to_json_string([]), '[]')

    def test_from_json_string(self):
        '''Testing from_json_string method'''
        t6 = [{"id": 3, "w": 6}]
        r6 = Base.to_json_string(t6)
        t7 = None
        r7 = Base.to_json_string(t7)
        t8 = "string"
        r8 = Base.to_json_string(t8)
        self.assertEqual(Base.from_json_string(r6), t6)
        self.assertEqual(Base.from_json_string(r7), [])
        self.assertEqual(Base.from_json_string(r8), t8)

    def test_create(self):
        '''Testing create method'''
        t9 = {"id": 1, "width": 1, "height": 2, "x": 2, "y": 2}
        r9 = Rectangle.create(**t9)
        self.assertEqual(r9.__str__(), "[Rectangle] (1) 2/2 - 1/2")

        t10 = {'id': 2, 'size': 3, 'x': 4, 'y': 5}
        r10 = Square.create(**t10)
        self.assertEqual(r10.__str__(), "[Square] (2) 4/5 - 3")

        t11 = {'id': 1, 'width': "string", 'height': 2, 'x': 2, 'y': 2}
        t12 = {'id': 2, 'size': "string", 'x': 4, 'y': 5}
        with self.assertRaises(TypeError):
            r11 = Rectangle.create(**t11)
            r12 = Square.create(**t12)

    def test_save_to_file(self):
        '''Testing save_to_file method'''
        t13_1 = Rectangle(3, 6, 9, 12)
        t13_2 = Rectangle(15, 18)
        t14_1 = Square(3, 6, 9)
        t14_2 = Square(12)
        r13 = Rectangle.save_to_file([t13_1, t13_2])
        r14 = Square.save_to_file([t14_1, t14_2])

        self.assertTrue(os.path.isfile("Rectangle.json"))
        self.assertTrue(os.path.isfile("Square.json"))

    def test_load_from_file(self):
        '''Testing load_from_file method'''
        t15_1 = Rectangle(3, 6, 9, 12)
        t15_2 = Rectangle(15, 18)
        t16_1 = Square(3, 6, 9)
        t16_2 = Square(12)

        r15 = Rectangle.save_to_file([t15_1, t15_2])
        r16 = Square.save_to_file([t16_1, t16_2])

        rec_list = Rectangle.load_from_file()
        sq_list = Square.load_from_file()

        self.assertIsInstance(rec_list[0], Rectangle)
        self.assertIsInstance(rec_list[1], Rectangle)
        self.assertIsInstance(sq_list[0], Square)
        self.assertIsInstance(sq_list[1], Square)

        self.assertEqual(rec_list[0].__str__(), "[Rectangle] (5) 9/12 - 3/6")
        self.assertEqual(rec_list[1].__str__(), "[Rectangle] (6) 0/0 - 15/18")
        self.assertEqual(sq_list[0].__str__(), "[Square] (7) 6/9 - 3")
        self.assertEqual(sq_list[1].__str__(), "[Square] (8) 0/0 - 12")

if __name__ == "__main__":
    unittest.main()
