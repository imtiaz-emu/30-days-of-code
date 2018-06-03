'''
Problem Statement: https://www.hackerrank.com/challenges/30-conditional-statements/problem
Author: Imtiaz Emu
Language: Python 3
'''


import math
import os
import random
import re
import sys


def weirdNotWeird(num):
   if(num % 2 == 1):
    print('Weird')
   else:
    if(num > 20):
        print('Not Weird')
    elif (num >= 6 and num <= 20):
        print('Weird')
    elif (num >= 2 and num <= 5):
        print('Not Weird')

if __name__ == '__main__':
    N = int(input())
    weirdNotWeird(N)
