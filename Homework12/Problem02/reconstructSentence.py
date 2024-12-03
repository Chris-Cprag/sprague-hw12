"""
This program takes in two text files and return an alternating combination of
the two. The reverse order of each sentence is combined together in an
alternating fasion.
Example Innvocation: python3 ./reconstructSentence.py input1.py input2.py
"""


import sys


#Read in the Files
f1 = open(sys.argv[1])
f2 = open(sys.argv[2])

flines1 = f1.readlines()
flines2 = f2.readlines()

text1 = []
temp = []
text2 = []

#Seperate all Words in File 1
for i in flines1:
 temp.append(i.split())
for n in temp:
  for i in n:
    text1.append(i)

#Seperate all Words in File 2
temp = []
for i in flines2:
  temp.append(i.split())
for n in temp:
  for i in n:
    text2.append(i)

#Combine them in a reverse order
size = len(text1)
size2 = len(text2)

if(size > size2):
  uses = size
  diff2 = size-size2
  diff1 = 0
else:
  uses = size2
  diff2 = 0
  diff1 = size1-size

final = ""

for n in range(uses):
  if(size-n > 0):
    final = final + " " + text1[size-n-1-diff1]
  if(size2-n > 0):
    final = final + " " + text2[size-n-1-diff2]

f3 = open("output.txt","w")
f3.write(final)
print(final)
