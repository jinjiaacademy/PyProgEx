# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 23:02:28 2023

@author: Jinjia
"""

"""
Write a drawBorder() function with parameters width and height.
The function draws the border of a rectangle with the given integer sizes.

Prerequisite concepts: Boolean operators, strings, string concatenation,
string replication, for loops, range()
"""

def drawBorder(width, height):
    print("+" + "-" * (width-2) + "+")
    for i in range(height - 2):
        print("|" + (width-2) * " " + "|")
    print("+" + "-" * (width-2) + "+")
    
drawBorder(32, 10)