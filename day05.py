'''
Problem Statement: https://www.hackerrank.com/challenges/30-loops/problem
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
    for i in range(1, 11):
        print("{0} x {1} = {2}".format(n, i, n*i))
