#!/bin/python3

import math
import os
import random
import re
import sys


# import string

# Complete the solve function below.
def solve(word):
    a = word.split(" ")
    b = [i.capitalize() for i in a]
    return " ".join(b)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
