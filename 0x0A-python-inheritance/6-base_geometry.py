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
