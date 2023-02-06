#!/usr/bin/python3
"""
Created on Mon Feb 06 16:21:54 2023
@author: Alfred Ternor
"""


class MyList(list):
    """Represent a List."""
    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
