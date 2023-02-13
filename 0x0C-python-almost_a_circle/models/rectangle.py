#!/usr/bin/python3
"""
created on Sun Feb 12 17:43:34 2023
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
        elif value <= 0:
            raise ValueError("width must be > 0")
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
        elif value <= 0:
            raise ValueError("height must be > 0")
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

    def area(self):
        """Calculates the area of the Rectangle

        Returns:
            The Rectangle area
        """
        return (self.width * self.height)

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v


    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """"Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return f"[Rectangle] ({self.id} {self.x}/{self.y} - {self.width}/{self.height}"