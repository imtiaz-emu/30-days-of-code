'''
Problem Statement: https://www.hackerrank.com/challenges/30-binary-search-trees/problem
Author: Imtiaz Emu
Language: Python 3
'''


class Node:
  def __init__(self, data):
    self.right = self.left = None
    self.data = data


class Solution:
  def insert(self, root, data):
    if root == None:
      return Node(data)
    else:
      if data <= root.data:
        cur = self.insert(root.left, data)
        root.left = cur
      else:
        cur = self.insert(root.right, data)
        root.right = cur
    return root


def getHeight(self, root):
  if(root == None):
    return 0
  else:
    lHeight = self.getHeight(root.left)
    rHeight = self.getHeight(root.right)

    if(lHeight > rHeight):
      return lHeight + 1
    else:
      return rHeight + 1


T = int(input())
myTree = Solution()
root = None
for i in range(T):
  data = int(input())
  root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
