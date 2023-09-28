# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 13:33:38 2023

@author: Jinjia
"""

"""
Write a mode() function that has a numbers parameter. This function 
returns the mode, or most frequently appearing number, of the list
of integer and floating-point numbers passed to the function.

Prerequisite concepts: for loops, augmented assignment operators,
indexes, not in operator
"""

def mode(numbers):
    # return the mode of the list of numbers
    if len(numbers) == 0:
        return None
    
    numberCount = {}
    
    mostFreqNum = None
    mostFreqNumCount = 0
    
    for number in numbers:
        if number not in numberCount:
            numberCount[number] = 0
        numberCount[number] += 1
        
        if numberCount[number] > mostFreqNumCount:
            mostFreqNum = number
            mostFreqNumCount = numberCount[number]
    return mostFreqNum


assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1
import random
random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    assert mode(testData) == 4
            
    