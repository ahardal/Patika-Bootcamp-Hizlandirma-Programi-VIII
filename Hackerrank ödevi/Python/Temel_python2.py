
# https://www.hackerrank.com/challenges/py-collections-namedtuple



# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

# Read total number of students
n = int(input())

# Read column names and create namedtuple 
students = namedtuple('Student',input())
data = []
for _ in range(n):
  id,mark,cls,name = input().split() # Read values 
  data.append(students(id,mark,cls,name)) # 
  
total = 0
for i in range(len(data)):
  total = total + int(data[i].MARKS)

print(total / len(data))