'''
Problem Statement: https://www.hackerrank.com/challenges/30-binary-trees/problem
Author: Imtiaz Emu
Language: Python 3
'''

import sys


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
  
  def levelOrder(self, root):
    # Write your code here
    nodes = []
    queue = [root] if root else []
    while queue:
      currentNode = queue.pop()
      nodes.append(str(currentNode.data))
      
      if currentNode.left:
        queue.insert(0, currentNode.left)
      if currentNode.right:
        queue.insert(0, currentNode.right)
    print(' '.join(nodes))


T = int(input())
myTree = Solution()
root = None
for i in range(T):
  data = int(input())
  root = myTree.insert(root, data)
myTree.levelOrder(root)
