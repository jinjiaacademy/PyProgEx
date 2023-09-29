# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 23:07:33 2023

@author: Jinjia
"""

"""
Write a drawPyramid() function with a height parameter. The top of the 
pyramid has one centered hashtag character, and the subsequent rows have 
two more hashtags thatn the previous row.

Prerequisite concepts: strings, string concatenation, string replication,
for loops, range()
"""

def drawPyramid(height):
    # draw a pyramid with hashtag #
    for i in range(height):
        print(" " * (height - i - 1) + "#" * (2 * i + 1))
        
drawPyramid(10)