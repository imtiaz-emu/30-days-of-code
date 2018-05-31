'''
Problem Statement: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
Author: Imtiaz Emu
Language: Python 3
'''

t = int(input())
phoneBook = {}
for i in range(0, t):
  entry = input().rstrip().split()
  phoneBook[entry[0]] = entry[1]

while True:
  name = input()
  if not name:  # Exit on empty string.
    break
  if name in phoneBook:
    print("{0}={1}".format(name, phoneBook[name]))
  else:
    print("Not found")
