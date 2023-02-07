#!/usr/bin/python3
"""
created on Tue Feb 07 17:43:34 2023
@author: Alfred Ternor
"""
import json


def load_from_json_file(filename):
    """creates an object from a json file.
        Args:
            filename: the file to read json from
    """
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
