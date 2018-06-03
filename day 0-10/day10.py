'''
Problem Statement: https://www.hackerrank.com/challenges/30-binary-numbers/problem
Author: Imtiaz Emu
Language: Python 3
'''


from itertools import groupby

def get_binary(number):
  result = ""
  while (number > 0):
    result += str(number%2)
    number //= 2
  
  return result[::-1]

def get_consecutive_1s(base2):
  groups = groupby(base2)
  
  result = 0
  for label, group in groups:
    if label == '1':
      tupleOf1 = (label, sum(1 for _ in group))
      result = max(tupleOf1[1], result)

  print(result)


base10 = int(input())

get_consecutive_1s(get_binary(base10))
