#!/usr/bin/python3
# test_base.py
# Alfred Ternor
"""Defines unittests for rectangle.py.

"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.r = Rectangle(2,3,4,5)


    def test_width_getter(self):
        self.assertEqual(2,self.r.width)




if __name__ == '__main__':
    unittest.main()