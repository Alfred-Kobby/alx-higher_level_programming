#!/usr/bin/python3
"""
created on Tue Feb 07 17:43:34 2023
@author: Alfred Ternor
"""
import json


def from_json_string(my_str):
    """Returns python object.
        Args:
            my_str : The string to convert.
    """
    return json.loads(my_str)
