#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    finalString = ""
    for character in s:
        if(character>='a' and character<='z'):
            characterValue = ord(character) - 96
            changedValue = (characterValue+k)%26
            if(changedValue == 0):
                changedValue = 26 
            finalString += chr(changedValue + 96)
        elif(character>='A' and character<='Z'):
            characterValue = ord(character) - 64
            changedValue = (characterValue+k)%26
            if(changedValue == 0):
                changedValue = 26 
            finalString += chr(changedValue + 64)
        else:
            finalString += character
    return finalString
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
