# Patika Temel Python Dictionary Hackerrank Challange
# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem


# Solution
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

d = defaultdict(list)

# Read length of group a and group b 
n, m = input().split()

# Read Group A values
for _ in range(int(n)):
  d['group_a'].append(input()) 
  
# Read Group B values
for _ in range(int(m)):
  d['group_b'].append(input())
  
for letter_2 in d['group_b']:
    if not letter_2 in d['group_a']: # if the word is not in group a print -1
                print("-1")
    else:
        for index,letter_1 in enumerate (d['group_a']): # if the word is in group a print the index
            if letter_2 == letter_1:
                print(index+1,end=' ')
        print('')