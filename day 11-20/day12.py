'''
Problem Statement: https://www.hackerrank.com/challenges/30-inheritance/problem
Author: Imtiaz Emu
Language: Python 3
'''


class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


class Student(Person):

  def __init__(self, firstName, lastName, idNumber, scores):
    Person.__init__(self, firstName, lastName, idNumber)
    self.scores = scores

  def grade(self, mark):
    if(mark < 40):
      return 'T'
    elif(mark >= 40 and mark < 55):
      return 'D'
    elif (mark >= 55 and mark < 70):
      return 'P'
    elif (mark >= 70 and mark < 80):
      return 'A'
    elif (mark >= 80 and mark < 90):
      return 'E'
    else: return 'O'

  def calculate(self):
    avg = sum(self.scores) / len(self.scores)
    return self.grade(avg)


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())