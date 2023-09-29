# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 19:43:54 2023

@author: Jinjia
"""

"""
Write a program that displays the lyrics to '99 Bottles of Beer'.
Each stanza of the song goes like this:
    X bottles of beer on the wall,
    X bottles of beer,
    Take one down,
    Pass it around,
    X – 1 bottles of beer on the wall,
The X in the song starts at 99 and decreases by one for each stanza. When X is one (and X – 1 is
zero), the last line is ―No more bottles of beer on the wall!‖ After each stanza, display a blank line to
separate it from the next stanza.

Prerequisite concepts: for loops, range() with three arguments, print()
"""

for i in range(99, 1, -1):
    print(f"""
{i} bottles of beer on the wall,
{i} bottles of beer,
Take one down,
Pass it around,
{i-1} bottles of beer on the wall\n
        """)

print(
      """
1 bottles of beer on the wall,
1 bottles of beer,
Take one down,
Pass it around,
No more bottles of beer on the wall!
      """
      )