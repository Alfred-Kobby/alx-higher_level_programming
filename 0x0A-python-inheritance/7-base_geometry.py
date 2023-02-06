#!/usr/bin/python3
"""
Created on Mon Feb 06 16:21:54 2023
@author: Alfred Ternor
"""


class BaseGeometry:
    """Represent base geometry."""
    def area(self):
        """Calculates the area of the base geometry

        Returns:
            The area of the square
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
