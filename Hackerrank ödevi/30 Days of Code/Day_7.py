## 30 Days of Code Day 7: Arrays
# https://www.hackerrank.com/domains/tutorials/30-days-of-code

# Example:
# A = [1, 2, 3, 4]
#Print 4 3 2 1. Each integer is separated by one space.

# Sample Input
# 4
# 1 4 3 2

# Sample Output
# 2 3 4 1

#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))


print(" ".join(map(str,arr[::-1])))

# Without map type error occurs,
# TypeError: sequence item 0: expected str instance, int found
# https://stackoverflow.com/a/34477119