# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 10:45:43 2023

@author: Jinjia
"""

"""
Write two functions, isOdd() and isEven(), with a single parameter
named number. 
The isOdd() function returns True if number is odd and False is number is even. 
The isEven() function returns the True if number is even and False if number is odd.
Both functions return False for numbers with fractional parts. 
Zero is considered an even number.

Prerequisite concepts: modulo operator
"""

def isOdd(number):
    # Return True if number is odd and False if number is even
    return number % 2 == 1


def isEven(number):
    # Return True if number is even and False if number is odd
    return number % 2 == 0


assert isOdd(42) == False
assert isOdd(9999) == True
assert isOdd(-10) == False
assert isOdd(-11) == True
assert isOdd(3.1415) == False
assert isEven(42) == True
assert isEven(9999) == False
assert isEven(-10) == True
assert isEven(-11) == False
assert isEven(3.1415) == False