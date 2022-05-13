# 30 Days of Code Day 3: Intro to Conditional Statements
# https://www.hackerrank.com/domains/tutorials/30-days-of-code


#!/bin/python3
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input().strip())

# Check if value is odd
is_odd = N % 2 == 1

# If N is odd print Weird
if is_odd:
  print('Weird')
else:
  if (N > 1 and N < 6):
    print('Not Weird')
  elif (N > 5 and N < 21):
    print('Weird')
  elif (N > 20):
    if is_odd:
      print('Weird')
    else:
      print('Not Weird')
      
