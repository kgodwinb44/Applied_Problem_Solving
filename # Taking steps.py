import math
import os
import random
import re
import sys

#
# Complete the 'TakeSteps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER nArray
#  2. INTEGER nSteps
#  3. STRING_ARRAY grid
#

def TakeSteps(nArray, nSteps, grid):
    # Write your code here
    
    x, y = 0, 0
    i = 0
    
    while i < nSteps:
        move = grid[y][x]
        
        if move == '>':
            x += 1
        elif move == '<':
            x -= 1
        elif move == '^':
            y -= 1
        elif move == 'v':
            y += 1
        i += 1
    return nArray * y + x

nArray = 128
nSteps = 10
grid = [
    '^v^v^v<>^v<<<v<>^v<<<v<<<v<<^<v<<<v<^v^v^>^v^>^v^<v<<<<>^v^v^v<v',
    '^>^>^v^v<>>v^v^v<>>v^>>v^>>>>^>v>^>>^>^>^v<>^v<>>^>v>>^v<>^>^v^v',
    '^>^>^v^v<>>v^v^v<>>v^>>v^>>>>^>v>^>>^>^>^v<>^v<>>^>v>>^v<>^>^v^v'
    ]
TakeSteps(nArray,nSteps,grid)