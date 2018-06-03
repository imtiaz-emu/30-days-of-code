'''
Problem Statement: https://www.hackerrank.com/challenges/30-review-loop/problem
Author: Imtiaz Emu
Language: Python 3
'''


def string_manipulation(str):
    oddResult = ""
    evenResult = ""
    for i in range(len(str)):
        if i % 2 == 0:
            evenResult = evenResult + str[i]
        else:
            oddResult = oddResult + str[i]
    return (evenResult + " " + oddResult)


t = int(input())
for i in range(0, t):
    givenString = input()
    print(string_manipulation(givenString))

