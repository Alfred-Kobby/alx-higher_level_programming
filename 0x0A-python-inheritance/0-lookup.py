#!/usr/bin/python3
"""
Created on Mon Feb 06 16:21:54 2023
@author: Alfred Ternor
"""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
