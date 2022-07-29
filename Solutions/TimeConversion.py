#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    time = s.split(":")
    notation = time[-1][-2:]
    if notation == "PM" and int(time[0])<12:
        time[0] = str(int(time[0])+12)
    if int(time[0])==12 and notation =="AM":
        time[0] = "00"

    output = ":".join(time)
    return output[:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
