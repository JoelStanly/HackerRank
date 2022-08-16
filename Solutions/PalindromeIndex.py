#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    
    reverseString = s[::-1]
    size = len(s)
    for i in range(size):
        if(i==0):
            if(s[i+1:] == reverseString[:size-1]):
                return 0
        elif(i==size-1):
            if(s[:size-1] == reverseString[size-i:]):
                return size-1
        else:
            string = s[:i]+s[i+1:]
            reverse = reverseString[:size-i-1]+reverseString[size-i:]
            if(string == reverse):
                return i
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
