#!/usr/bin/python3
import json
"""
created on Tue Feb 07 17:43:34 2023
@author: Alfred Ternor
"""

def to_json_string(my_obj):
    """Returns json representation of object.
        Args:
            my_obj : The object to convert.
    """
    return json.dumps(my_obj)
