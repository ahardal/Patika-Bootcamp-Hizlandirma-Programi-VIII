# 30 Days of Code Day 1: Data Types
# https://www.hackerrank.com/domains/tutorials/30-days-of-code

# Sample Input
#-1-| 12
#-2-| 4.0
#-3-| is the best place to learn and practice coding!

# Sample Output
#-1-| 16
#-2-| 8.0
#-3-| HackerRank is the best place to learn and practice coding!

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.

# Read and save an integer, double, and String to your variables.
var_1 = int(input())
var_2 = float(input())
var_3 = input()
# Print the sum of both integer variables on a new line.
print(i + int(var_1))

# Print the sum of the double variables on a new line.
print(d + var_2)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + var_3)