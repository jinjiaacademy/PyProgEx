# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:58:19 2023

@author: Jinjia
"""


"""
In English, ordinal numerals have suffixes such as the 'th' in '30th'
or 'nd' in '2nd'. Write an ordinalSuffix() function with an integer
parameter named number and returns a string of the number with its
ordinal suffix. 

Prerequisite concepts: strings, in operator, slices, string concatenation
"""


def ordinalSuffix(number):
    # Return the number's ordinal suffix
    numStr = str(number)
    
    if numStr[-2:] in ["11", "12", "13"]:
        return numStr+"th"
    if numStr[-1] == "1":
        return numStr+"st"
    if numStr[-1] == "2":
        return numStr+"nd"
    if numStr[-1] == "3":
        return numStr+"rd"
    return numStr+"th"
        
        
assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'
