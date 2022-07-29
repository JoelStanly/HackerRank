#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i==0:
            zero+=1
        else:
            if i>0:
                positive+=1
            else:
                negative+=1
    n = len(arr)
    zero/=n
    positive/=n
    negative/=n
    print("%.6f"%positive)
    print("%.6f"%negative)
    print("%.6f"%zero)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
