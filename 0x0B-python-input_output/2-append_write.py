#!/usr/bin/python3
"""
created on Tue Feb 07 17:43:34 2023
@author: Alfred Ternor
"""


def append_write(filename="", text=""):
    """Write a file and prints number of characters.
        Args:
            filename : The file to read.
            text: the text to be written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
