# Sales by match

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    
    # Counts how many values in the array are the same
    count = 0
    arr = set(ar) # Convert list `ar` into a set to get unique values
    for v in arr: # Loop through each unique value in `arr`
        count += ar.count(v)//2 # Count occurrences of `v` in `ar`, divide by 2 (integer division)
    return count 
        

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()