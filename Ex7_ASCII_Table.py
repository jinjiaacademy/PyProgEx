# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 13:36:33 2023

@author: Jinjia
"""

"""
Write a printASCIITalbe() function that displays the ASCII number
and its corresponding text character, from 32 to 126.

Prerequisite concepts: for loops, range() with two arguments, chr()
"""

def printASCIITalbe():
    # print the ASCII number and its corresponding text character
    for num in range(32, 127):
        print(num, chr(num))


printASCIITalbe()