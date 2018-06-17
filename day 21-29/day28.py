'''
Problem Statement: https://www.hackerrank.com/challenges/30-regex-patterns/problem
Author: Imtiaz Emu
Language: Python 3
'''

import math
import os
import random
import re
import sys

if __name__ == '__main__':
  N = int(input())
  names = []
  for N_itr in range(N):
    firstName, emailID = input().split()
    
    if (emailID.split("@")[1] == 'gmail.com'):
      names.append(firstName)
  
  for name in sorted(names):
    print(name)
    
