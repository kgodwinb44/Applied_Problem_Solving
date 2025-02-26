# Count the unique pairs

import math
import os
import random
import re
import sys

#
# Complete the 'UniquePairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY values
#   

def unique_pairs(n, values):
    
    pairs = []
    
    # Iterate through the list to generate pairs
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            print(i,j)
            # Only consider pairs with different elements
            if values[i] != values[j]:
                # Create a pair, sorted to avoid (a, b) and (b, a) being counted separately
                pair = sorted([values[i], values[j]])
                if pair not in pairs:
                    pairs.append(pair)
    #return len(pairs)

    
        

# Test example
values = 4,5,7,5,5      
result = unique_pairs(5,values)
print(result)