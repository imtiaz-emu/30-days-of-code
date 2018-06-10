'''
Problem Statement: https://www.hackerrank.com/challenges/30-queues-stacks/problem
Author: Imtiaz Emu
Language: Python 3
'''

import sys

from collections import deque


class Solution:

  stack = []
  dque = deque([])

  def pushCharacter(self, i):
    self.stack.append(i)

  def enqueueCharacter(self, i):
    self.dque.append(i)

  def popCharacter(self):
    return self.stack.pop()

  def dequeueCharacter(self):
    return self.dque.popleft()


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
  obj.pushCharacter(s[i])
  obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
  if obj.popCharacter() != obj.dequeueCharacter():
    isPalindrome = False
    break
# finally print whether string s is palindrome or not.
if isPalindrome:
  print("The word, " + s + ", is a palindrome.")
else:
  print("The word, " + s + ", is not a palindrome.")