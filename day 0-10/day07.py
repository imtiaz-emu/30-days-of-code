'''
Problem Statement: https://www.hackerrank.com/challenges/30-arrays/problem
Author: Imtiaz Emu
Language: Python 3
'''


import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(*(arr[::-1]))
