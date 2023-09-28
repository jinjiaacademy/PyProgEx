# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:21:19 2023

@author: Jinjia
"""

"""
Write a rollDice() function with a numberOfDice parameter that
represents the number of six-sided dice. The function returns the 
sum of all of the dice rolls.
For this exercise you must import Python's random module to call
its random.randint() function for this exercise.

Prerequistite concepts: import statements, random module, randint(),
for loops, range(), augmented assignment operator
"""


import random


def rollDice(numberOfDice):
    # return the sum of all of the dice rolls.
    total = 0
    
    for i in range(numberOfDice):
        total += random.randint(1, 6)
    
    return total


assert rollDice(0) == 0
assert rollDice(1000) != rollDice(1000)
for i in range(1000):
    assert 1 <= rollDice(1) <= 6
    assert 2 <= rollDice(2) <= 12
    assert 3 <= rollDice(3) <= 18
    assert 100 <= rollDice(100) <= 600