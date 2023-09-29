# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 20:15:19 2023

@author: Jinjia
"""

"""
Write a function named printHandshakes() with a list parameter named
people which will be a list of strings of people's names. The function
prints out 'X shakes hands with Y', where X and Y are every possible pair
of handshakes between the people in the list. No duplicates are permitted.
The printHandshakes() function must also return an integer of the number
of handshakes.

Prerequisite concepts: for loops, range() with two arguments, len(), 
augmented assignment operators
"""


def printHandshakes(people):
    
    handshakesCount = 0 
    
    for i in range(len(people)):
        for j in people[i+1:]:
            print(f"{people[i]} shakes hands with {j}")
            handshakesCount += 1
            
    return handshakesCount
        
        
assert printHandshakes(['Alice', 'Bob']) == 1
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6