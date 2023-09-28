# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 00:00:41 2023

@author: Jinjia
"""

"""
Write a getSmallest() function that has a numbers parameter.
The numbers parameter will be a list of integer and floating-point
number values. The function returns the smallest value in the list.
If the list is empty, the function should return None.
When you are done with this exercise, write a getBiggest() function
which returns the biggest number instead of the smallest number.

Prerequisite concepts: len(), for loops, lists, None value
"""


def getSmallest(numbers):
    # return the smallest number in numbers list, return None
    # if the numbers list is empty
    if len(numbers) == 0:
        return None
    
    smallestNum = numbers[0]
    for number in numbers:
        if number < smallestNum:
            smallestNum = number
    return smallestNum

def getBiggest(numbers):
    # return the biggest number in numbers list, return None
    # if the numbers list is empty
    if len(numbers) == 0:
        return None
    
    biggestNum = numbers[0]
    for number in numbers:
        if number > biggestNum:
            biggestNum = number
    return biggestNum


assert getSmallest([1, 2, 3]) == 1
assert getSmallest([3, 2, 1]) == 1
assert getSmallest([28, 25, 42, 2, 28]) == 2
assert getSmallest([1]) == 1
assert getSmallest([]) == None