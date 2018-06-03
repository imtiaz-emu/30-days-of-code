'''
Problem Statement: https://www.hackerrank.com/challenges/30-data-types/problem
Author: Imtiaz Emu
Language: Python 3
'''

i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
second_integer = int(input())
second_double = float(input())
second_string = input()
# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.
print(i + second_integer)
# Print the sum of the double variables on a new line.
print("%.1f" % (d + second_double))
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + second_string)