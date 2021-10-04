#!/usr/bin/python3

""" module for shapes """


class Rectangle:

    """ class for rectangle """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initiation of object """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ return area """
        return self.__height * self.width

    def perimeter(self):
        """ return perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            hashes = '#' * self.__width
            return '\n'.join(hashes for h in range(self.__height))

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
