# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 13:58:57 2023

@author: Jinjia
"""

"""
Write a getChessSquareColor() function that has parameters column
and row. The function either returns 'black' or 'white' depending
on the color at the specified column and row.
Chess boards are 8X8 spaces in size, and the columns and rows in
this program begin at 0 and end at 7. If the arguments for column
or row are outside the 0 to 7 range, the function returns a blank
string.

Prerequisite concepts: Boolean operators, modulo operator
"""


def getChessSquareColor(column, row):
    # get the color of chess square based on column and row
    if (column < 0 or column > 7) or (row < 0 or row > 7):
        return ""
    else:
        if column % 2 == row % 2:
            return "white"
        else:
            return "black"


assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == ''
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''