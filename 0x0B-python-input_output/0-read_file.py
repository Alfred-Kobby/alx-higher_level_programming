#!/usr/bin/python3
"""
created on Tue Feb 07 17:43:34 2023
@author: Alfred Ternor
"""


def read_file(filename=""):
    """Read a file and prints its content.
        Args:
            filename : The file to read.
        """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
