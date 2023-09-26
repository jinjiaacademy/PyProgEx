# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 10:19:59 2023

@author: Jinjia
"""

"""
Write a convertToFahrenheit(degreesCelsius) function returns
the number of this temperature in degrees Fahrenheit.
Then write a function named convertToCelsius(degreesFahrenheit)
returns a number of this temperature in degrees Celsius.

Prerequisite concepts: math operators
"""

def convertToFahrenheit(degreesCelsius):
    # Calculate and return the degrees Fahrenheit
    return degreesCelsius * (9 / 5) + 32


def convertToCelsius(degreesFahrenheit):
    # Calculate and return the degrees Celsius
    return (degreesFahrenheit - 32) * (5 / 9)


assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15

assert convertToCelsius(convertToFahrenheit(42)) == 42