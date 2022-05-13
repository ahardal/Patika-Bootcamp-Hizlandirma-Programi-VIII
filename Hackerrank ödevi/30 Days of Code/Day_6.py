## 30 Days of Code Day 6: Let's Review
# https://www.hackerrank.com/domains/tutorials/30-days-of-code

# Sample Input
# 2
# Hacker
# Rank

# Sample Output
# Hce akr
# Rn ak

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
data = []
for i in range(N):
  data.append(input())
  
for word in  data:
    odd = []; even = [] # create empty lists
    for index,letter in enumerate(word): # loop through each letter in the word
        if index % 2 == 0: # append even and odd letters to their respective lists
            even.append(letter)
        else:
            odd.append(letter) 
    print(f'{"".join(even)} {"".join(odd)}') # print the even and odd letters