#!/usr/bin/python3
'''task 8 module'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Initializaion of the object'''
    super().integer_validator('width', width)
    super().integer_validator('height', height)
    self.__width = width
    self.__height = height
