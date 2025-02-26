# Multimodal

import math
import os
import random
import re
import sys

#
# Complete the 'Mode' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY values
#


def Mode(n, values):

 counts = {}
 result = []
 occurance = 0

 for i in values:
       counts[i] = counts.get(i, 0) + 1
       if counts[i] > occurance:
           occurance = counts[i]

 for key, value in counts.items():
       if value == occurance:
           result.append(key)
  
 if len(result) == 1:
        return result[0]
 else:
        return -1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    values = []

    for _ in range(n):
        values_item = int(input().strip())
        values.append(values_item)

    mode = Mode(n, values)

    fptr.write(str(mode) + '\n')

    fptr.close()