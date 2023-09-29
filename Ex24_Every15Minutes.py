# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 19:54:30 2023

@author: Jinjia
"""

"""
Write a program that display the time for every 15 minutes interval from
12:00 am to 11:45 pm.

Prerequisite concepts: for loops, lists, nested loops, string concatenation
"""

amPm = ['am', 'pm']
hours = ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
minutes = ['00', '15', '30', '45']

lines = 0

for halve in amPm:
    for hour in hours:
        for minute in minutes:
            print(f"{hour}:{minute} {halve}")
            lines += 1

print(lines)