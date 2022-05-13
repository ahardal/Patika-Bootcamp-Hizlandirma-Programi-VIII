# 30 Days of Code Day 2: Operators
# https://www.hackerrank.com/domains/tutorials/30-days-of-code

# Task
#  Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
#  and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.
#  Round the result to the nearest integer.
# Example:
# If the meal price is $100, the tip percentage is 20, and the tax percentage is 8, 
# then the total cost of the meal is $123.

####| Sample Input
#-1-| 12.00
#-2-| 20
#-3-| 8

####| Sample Output
#-1-| 15


import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip = meal_cost * tip_percent / 100 # Calculate the tip
    tax = meal_cost * tax_percent / 100 # Calculate the tax
    print(round(meal_cost + tip + tax)) # Print the total cost of the meal

if __name__ == '__main__':
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    solve(meal_cost, tip_percent, tax_percent)
