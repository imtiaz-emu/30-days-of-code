'''
Problem Statement: https://www.hackerrank.com/challenges/30-interfaces/problem
Author: Imtiaz Emu
Language: Python 3
'''


class AdvancedArithmetic(object):
  def divisorSum(n):
    raise NotImplementedError


class Calculator(AdvancedArithmetic):
  def divisorSum(self, n):
    if (n == 1): return 1
    result = 1 + n
    i = 2
    while i <= n//2:
      if(n % i == 0):
        result += i
      i += 1
    return result


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)