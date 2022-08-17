#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    size = len(s)
    if(size%2 != 0):
        return -1
    substring1 = list(s[:size//2])
    substring2 = list(s[size//2:])
    c1 = Counter(substring1)
    c2 = Counter(substring2)
    diff = c1 - c2
    result = len(list(diff.elements()))
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
