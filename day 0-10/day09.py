'''
Problem Statement: https://www.hackerrank.com/challenges/30-recursion/problem
Author: Imtiaz Emu
Language: Python 3
'''

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if(n <= 1):
        return 1;
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
