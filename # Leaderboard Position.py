import math
import os
import random
import re
import sys

#
# Complete the 'LeaderboardPosition' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER nLines
#  2. STRING_ARRAY scoreData
#  3. STRING name
#

def LeaderboardPosition(nLines, scoreData, name):
    #List for player_name, score
    scores = []
    
    for data in scoreData:
        player_name, player_score = data.split()
        scores.append((player_name, int(player_score)))
    
    # Sort the score by ascending order in scores list
    sorted_scores = sorted(scores, key=lambda x: x[1])
    
    # Initialize the rank and previous score
    rank = 1
    current_rank = 1
    previous_score = sorted_scores[0][1]
   
    # Iterate through the scores
    for i in range(len(sorted_scores)):
        player_name, player_score = sorted_scores[i]
        
        # If the score is not the same as previous score
        if player_score != previous_score:
            # Update rank
            rank = current_rank  
        
        # Check if the current player's name matches the target name
        if player_name == name:
            return rank
        
        # Move to the next player
        current_rank += 1
        previous_score = player_score



        

nLines = 5
scoredata = ['Ardath 1', 'Kerstin 1', 'Tomasine 4', 'Cordula 4', 'Valene 1']
name = 'Tomasine'
LeaderboardPosition(nLines, scoredata, name)
    
    

        