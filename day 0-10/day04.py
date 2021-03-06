'''
Problem Statement: https://www.hackerrank.com/challenges/30-class-vs-instance/problem
Author: Imtiaz Emu
Language: Python 3
'''


class Person:
  def __init__(self, initialAge):
    # Add some more code to run some checks on initialAge
    self.age = 0 if initialAge < 0 else initialAge
    if (self.age == 0):
      print("Age is not valid, setting age to 0.")

  def amIOld(self):
    # Do some computations in here and print out the correct statement to the console
    if (self.age >= 18):
      print("You are old.")
    elif (self.age >= 13 and self.age < 18):
      print("You are a teenager.")
    elif (self.age < 13):
      print("You are young.")

  def yearPasses(self):
    # Increment the age of the person in here
    self.age = self.age + 1