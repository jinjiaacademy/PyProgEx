# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:47:30 2023

@author: Jinjia
"""

"""
Write an average() function that has a numbers parameter. This function
returns the statistical average of the list of integer and floating-point
numbers passed to the function. 
Passing an empty list to average() should cause it to return None

Prerequisite concepts: len(), for loops, augmented assignment operators
"""


def average(numbers):
    # return the average of list of numbers, if numbers list is empty
    # returns None
    if len(numbers) == 0:
        return None
    
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
assert average([12, 20, 37]) == 23
assert average([0, 0, 0, 0, 0]) == 0
import random
random.seed(42)
testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
for i in range(1000):
    random.shuffle(testData)
    assert average(testData) == 2