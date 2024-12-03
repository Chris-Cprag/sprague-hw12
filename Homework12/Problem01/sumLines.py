"""
This program reads a text file and computes the sum, the number of integers, and
the average of the set of numbers
Example Innvocation:
"""
import sys

numbers = []
numbers2 = []
#Opens the File
f = open(sys.argv[1])
flines = f.readlines()
linecount = len(flines)
#Splits by Lines and Places into List
for i in flines:
  numbers.append(i.split())
#Makes List of Arrays into a Single List
for i in numbers:
  for n in i:
    numbers2.append(n)

#Basic Calculations
length = len(numbers2)
sums = 0
for n in numbers2:
  sums = sums + int(n)

print("Sum: ",sums)
print("Number of Integers: ",length)
print("Average: ",float(sums)/float(length))
