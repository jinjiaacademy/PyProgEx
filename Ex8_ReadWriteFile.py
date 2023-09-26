# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 13:44:25 2023

@author: Jinjia
"""

"""
You will write three functions for this exercise.
First, write a writeToFile() function with two parameters for 
the filename of the file and the text to write into the file.
Second, write an appendToFile() function, which is identical to 
writeToFile() except that the file opens in append mode instead
of write mode.
Finally, write a readFromFile() function with one parameter for 
the filename to open. This function returns the full text contents
of the file as a string.

Prerequisite concepts: text file reading and writing.
"""


def writeToFile(filename, text):
    # write text to the file
    with open(filename, "w") as f:
        f.write(text)

    
def appendToFile(filename, text):
    # append the text to the file
    with open(filename, "a") as f:
        f.write(text)


def readFromFile(filename):
    # read from file
    with open(filename) as f:
        return f.read()
        
        
writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'