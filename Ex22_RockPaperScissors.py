# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 19:28:21 2023

@author: Jinjia
"""

"""
Write a rpsWinner() function with parameters player1 and player2. These
parameters are passed one of the strings 'rock', 'paper', or 'scissors'
representing that player's move. If this results in player 1 winning, the
function returns 'player one'. If this results in player 2 winning, the
function returns 'player two'. Otherwise, the function returns 'tie'.

Prerequisite concepts: Boolean operators, elif statements
"""

def rpsWinner(player1, player2):
    # return the result of rock, paper, scissors game
    if player1 == 'rock':
        if player2 == 'rock':
            return 'tie'
        elif player2 == 'scissors':
            return 'player one'
        else:
            return 'player two'
    elif player1 == 'scissors':
        if player2 == 'rock':
            return 'player two'
        elif player2 == 'scissors':
            return 'tie'
        else:
            return 'player one'
    else:
        if player2 == 'rock':
            return 'player one'
        elif player2 == 'scissors':
            return 'player two'
        else:
            return 'tie'
        
        
assert rpsWinner('rock', 'paper') == 'player two'
assert rpsWinner('rock', 'scissors') == 'player one'
assert rpsWinner('paper', 'scissors') == 'player two'
assert rpsWinner('paper', 'rock') == 'player one'
assert rpsWinner('scissors', 'rock') == 'player two'
assert rpsWinner('scissors', 'paper') == 'player one'
assert rpsWinner('rock', 'rock') == 'tie'
assert rpsWinner('paper', 'paper') == 'tie'
assert rpsWinner('scissors', 'scissors') == 'tie'