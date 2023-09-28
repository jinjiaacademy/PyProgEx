# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:30:54 2023

@author: Jinjia
"""

"""
Write a function named getCostOfCoffee() that has a parameters named
numberOfCoffees and pricePerCoffee. Given this information, the function
returns the total cost of the coffee order. The coffee shop has an offer 
where you get one free coffee for every eight coffees you buy.

Prerequisite concepts: while loops, augmented assignment operator
"""


def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    # calculate the cost of coffee based on buy 8 get 1 free
    
    timesOfSale = numberOfCoffees // 8
    
    if numberOfCoffees <= 8:
        return numberOfCoffees * pricePerCoffee
    else:
        return (numberOfCoffees - timesOfSale) * pricePerCoffee


assert getCostOfCoffee(7, 2.50) == 17.50
assert getCostOfCoffee(8, 2.50) == 20
assert getCostOfCoffee(9, 2.50) == 20
assert getCostOfCoffee(10, 2.50) == 22.50
for i in range(1, 4):
    assert getCostOfCoffee(0, i) == 0
    assert getCostOfCoffee(8, i) == 8 * i
    assert getCostOfCoffee(9, i) == 8 * i
    assert getCostOfCoffee(18, i) == 16 * i
    assert getCostOfCoffee(19, i) == 17 * i
    assert getCostOfCoffee(30, i) == 27 * i