# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 22:57:59 2023

@author: Jinjia
"""

"""
Write a drawRectangle() function with two integer parameters: width and 
height. The function doesn't return any values but rather prints a rectangle
with the given number of hashtags in the horizontal and vertical directions.

Prerequisite concepts: for loops, range(), print(), end keyword argument for 
print()
"""

def drawRectangle(width, height):
    for i in range(height):
        print("#" * width)
        
drawRectangle(0, 0)