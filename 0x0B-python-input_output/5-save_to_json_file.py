#!/usr/bin/python3
"""
created on Tue Feb 07 17:43:34 2023
@author: Alfred Ternor
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes object to a file in Json representation.
        Args:
            my_obj : The object to write.
            filename: the file to write to
    """
    with open(filename, "w", encoding="utf-8") as f:
        return(f.write(json.dumps(my_obj)))
