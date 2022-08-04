#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    if(n == 1 or n == 0):
        return 1
    count = 0
    binary = str(bin(n))
    for i in binary[2:]:
        if(i == "0"):
            count += 1
    return 2**(count)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()