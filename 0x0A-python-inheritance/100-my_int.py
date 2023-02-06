#!/usr/bin/python3
"""
Created on Mon Feb 06 16:21:54 2023
@author: Alfred Ternor
"""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
