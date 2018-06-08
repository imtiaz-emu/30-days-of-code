'''
Problem Statement: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem
Author: Imtiaz Emu
Language: Python 3
'''


import sys


S = input().strip()
try:
    integer = int(S)
    print(integer)
except:
    print("Bad String")