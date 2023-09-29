# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 09:09:17 2023

@author: Jinjia
"""

"""
Write a drawBox() function with a size parameter. The size parameter contains
an integer for the width, length, and height of the box. The horizontal lines
are drawn with - dash characters, the vertical lines with | pipe characters, 
and the diagonal lines with / forward slash characters. The corners of the
box are drawn with + plus signs.

Prerequisite concepts: strings, string concatenation, string replication,
for loops, range()
"""


def drawBox(size):
    # Special case: Draw nothing if size is less than 1:
    if size < 1:
        return

    # Draw back line on top surface:
    print(' ' * (size + 1) + '+' + '-' * (size * 2) + '+')

    # Draw top surface:
    for i in range(size):
        print(' ' * (size - i) + '/' + ' ' * (size * 2) + '/' + ' ' * i + '|')

    # Draw top line on top surface:
    print('+' + '-' * (size * 2) + '+' + ' ' * size + '+')

    # Draw front surface:
    for i in range(size - 1, -1, -1):
        print('|' + ' ' * (size * 2) + '|' + ' ' * i + '/')

    # Draw bottom lie on front surface:
    print('+' + '-' * (size * 2) + '+')

# In a loop, call drawBox() with arguments 1 to 5:
for i in range(1, 6):
    drawBox(i)