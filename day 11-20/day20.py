'''
Problem Statement: https://www.hackerrank.com/challenges/30-sorting/problem
Author: Imtiaz Emu
Language: Python 3
'''

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# Write Your Code Here
numSwaps = 0
for i in range(n):
  for j in range(n-1-i):
    if(a[j] > a[j+1]):
      temp = a[j]
      a[j] = a[j+1]
      a[j+1] = temp
      numSwaps += 1

print('Array is sorted in {0} swaps.'.format(numSwaps))
print('First Element: {0}'.format(a[0]))
print('Last Element: {0}'.format(a[-1]))
