#!/usr/bin/python3
"""
created on Sun Jan 29 17:43:34 2023
@author: Alfred Ternor
"""


def add_integer(a, b=98):
    """
    adds two integers
    Args:
        a (int): First integer to add
        b (int): Second integer to add
    Raises:
        TypeError: Exception if size is not an integer
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))