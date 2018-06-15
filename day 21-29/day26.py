'''
Problem Statement: https://www.hackerrank.com/challenges/30-nested-logic/problem
Author: Imtiaz Emu
Language: Python 3
'''

da, ma, ya = map(int, input().strip().split())
de, me, ye = map(int, input().strip().split())

if (ya > ye):
  print(10000)
elif (ya < ye):
  print(0)
else:
  if (ma > me):
    print(500 * (ma - me))
  elif (me > ma):
    print(0)
  else:
    if (da > de):
      print(15 * (da - de))
    else:
      print(0)
