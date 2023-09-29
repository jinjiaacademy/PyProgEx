# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 13:01:42 2023

@author: Jinjia
"""

"""
Write an isValidDate() function with parameters year, month, and day.
The function should return True if the integers provided for these parameters
represent a valid date. Otherwise the function returns False. 

Prerequisite concepts: import statements, Boolean operators, chaining operators,
elif statements
"""

from Ex20_LeapYear import isLeapYear


def isValidDate(year, month, day):
    # If month is outside the bounds of 1 to 12, return False:
    if not (1 <= month <= 12):
        return False
    # After this point, you can assume the month is valid.

    # If the year is a leap year and the date is Feb 29th, it is valid:
    if isLeapYear(year) and month == 2 and day == 29:
        return True
    # After this point, you can assume the year is not a leap year.

    # Check for invalid dates in 31-day months:
    if month in (1, 3, 5, 7, 8, 10, 12) and not (1 <= day <= 31):
        return False
    # Check for invalid dates in 30-day months:
    elif month in (4, 6, 9, 11) and not (1 <= day <= 30):
        return False
    # Check for invalid dates in February:
    elif month == 2 and not (1 <= day <= 28):
        return False

    # Date passes all checks and is valid, so return True:
    return True

                
assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False
import datetime
d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
    assert isValidDate(d.year, d.month, d.day) == True
    d += oneDay