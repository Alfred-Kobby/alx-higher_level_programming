#!/usr/bin/python3
"""
created on Mon Jan 30 17:43:34 2023
@author: Alfred Ternor
"""


class Rectangle:
    """Represent a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Call the function to checking property

        Returns:
            The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """check errors and setter for width attribute

        Args:
            value: Value to checking errors

        Raises:
            TypeError: Exception if width is not an integer
            ValueError: Exception if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Call the function to checking property

        Returns:
            The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """check errors and setter for height attribute

        Args:
            value: Value to checking errors

        Raises:
            TypeError: Exception if height is not an integer
            ValueError: Exception if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates the area of the Rectangle

        Returns:
            The Rectangle area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of the Rectangle

        Returns:
            The Rectangle perimeter
        """
        return ((2*self.__width) + (2*self.__height))
