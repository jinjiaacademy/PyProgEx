# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 11:54:31 2023

@author: Jinjia
"""

"""
Write two functions named calculateSum() and calculateProduct().
They both have a parameter named numbers, which will be a list of
integer or floating-point values.
calculateSum() function adds these numbers and returns the sum while
the calculateProduct() function multiplies these numbers and returns
the product.
If the list passed to calculateSum() is empty, the function returns 0, 
and if the list passed to calculateProduct() is empty, the function
returns 1.

Prerequisite concept: lists, indexes, for loops, augmented assignment
operator
"""


def calculateSum(numbers):
    # return the sum of list of numbers   
    total = 0
    for num in numbers:
        total += num
    return total


def calculateProduct(numbers):
    # return the product of list of numbers
    product = 1
    for num in numbers:
        product *= num
    return product


assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840