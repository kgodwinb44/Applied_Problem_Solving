# Hash Function 1

import math
import os
import random
import re
import sys

#
# Complete the 'HashFunction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING S as parameter.
#
        

def HashFunction(S):
    A = 48271
    M = 2147483647
    n = 256  # Number of bins
    hash_value = 0

    for char in S:
        hash_value = (hash_value + ord(char)) * A % M  

    return hash_value % n  
