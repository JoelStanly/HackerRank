#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    size = len(arr)
    left = [0 for i in range(size)]
    right = [0 for i in range(size)]
    for i in range(size):
        j = size-i-1
        if(i == 0):
            left[i] = 0
            leftValue = arr[i]
            right[j] = 0
            rightValue = arr[j]
        else:
            left[i] = left[i-1]+leftValue
            leftValue = arr[i]
            right[j] = right[j+1]+rightValue
            rightValue = arr[j]
    for i in range(size):
        if(left[i] == right[i]):
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
