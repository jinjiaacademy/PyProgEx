# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:34:06 2023

@author: Jinjia
"""

"""
Write a fizzBuzz() function with a single integer parameter
named upTo. For the numbers 1 up to and including upTo, the function
prints one of four things:
    Prints 'FizzBuzz' if the number is divisible by 3 and 5
    Prints 'Fizz' if the number is only divisible by 3
    Prints 'Buzz' if the number is only divisible by 5
    Prints the number if the number is neither divisible by 3 nor 5
Print them without newlines.

Prerequisite concepts: modulo operator, end keyword argument for 
print(), for loops, range() with two arguments.
"""


def fizzBuzz(upTo):
    for number in range(1, upTo+1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(number, end=" ")


number = int(input("Enter the up-to number you want to show FizzBuzz: "))
fizzBuzz(number)
