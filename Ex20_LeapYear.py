# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 12:36:14 2023

@author: Jinjia
"""

"""
Write a isLeapYear() function with an integer year parameter. If year is a
leap year, the function returns True. Otherwise, the function returns False.

Prerequisite concepts: modulo operator, elif statements
"""

def isLeapYear(year):
    # return the year is a leap year or not
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
assert isLeapYear(1999) == False
assert isLeapYear(2000) == True
assert isLeapYear(2001) == False
assert isLeapYear(2004) == True
assert isLeapYear(2100) == False
assert isLeapYear(2400) == True