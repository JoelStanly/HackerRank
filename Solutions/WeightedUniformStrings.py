#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    prev = 0
    array = []
    result = []
    for current in s:
        if(prev!=current):
            currentValue = ord(current)-96
            prev = current
            array.append(currentValue)
        else:
            array.append(currentValue+array[-1])
    array = set(array)
    for i in queries:
        if(i in array):
            result.append("Yes")
        else:
            result.append("No")
    return result

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
