#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    counter = 0
    while(n>=2):
        lowerPower = 2**(n.bit_length()-1)
        if(lowerPower == n):
            n //= 2
            counter += 1
        else:
            n -= lowerPower
            counter += 1
    if(counter%2 != 0):
        return "Louise"
    else:
        return "Richard"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
