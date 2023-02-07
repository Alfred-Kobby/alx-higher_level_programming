#!/usr/bin/python3
"""
created on Tue Feb 07 17:43:34 2023
@author: Alfred Ternor
"""


def class_to_json(obj):
    """Returns Json representation of a class object.
        Args:
            my_obj : The object to convert.
    """
    return obj.__dict__
