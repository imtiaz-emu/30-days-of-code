'''
Problem Statement: https://www.hackerrank.com/challenges/30-scope/problem
Author: Imtiaz Emu
Language: Python 3
'''


class Difference:
  def __init__(self, a):
    self.__elements = a

    # Add your code here
    maximumDifference = 0

    def computeDifference(self):
      self.__elements.sort()
      arr = self.__elements
      self.maximumDifference = arr[len(arr) - 1] - arr[0]


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)