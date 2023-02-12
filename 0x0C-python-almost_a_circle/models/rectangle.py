#!/usr/bin/python3
"""
created on Mon Jan 30 17:43:34 2023
@author: Alfred Ternor
"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle using Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): x coordinate
            y (int): y coordinate
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

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
    

    @property
    def x(self):
        """Call the function to checking property

        Returns:
            The x of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """check errors and setter for x attribute

        Args:
            value: Value to checking errors

        Raises:
            TypeError: Exception if x is not an integer
            ValueError: Exception if x is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Call the function to checking property

        Returns:
            The y of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """check errors and setter for y attribute

        Args:
            value: Value to checking errors

        Raises:
            TypeError: Exception if y is not an integer
            ValueError: Exception if y is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
