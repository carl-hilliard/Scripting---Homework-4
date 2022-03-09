"""
Carl Hilliard
Intro to Scripting
Assignment 4
"""


## Problem 2: The Number Analysis Program


## The getTotal function
numList = []
def total():
    total = 0
    for i in range(len(numList)):
        total = total + numList[i]
    return total

## the lowest function
def lowest():
    numList.sort()
    return numList[0]

## the highest function
numList.sort()
length = len(numList)
    return numList[length-1]

for i in range(20):
    x = (int(input("Enter an ingeter")))
    numList.append(x)

print(lowest)
print(highest)
print(total)
print("Average:", total/20)









## Problem 3

num = int(input("Enter a number"))
diction = dict()

for i in range(1, number +1):
    diction[i] = i*i
print(diction)





## Problem 4
import random
lst = []
for i in range(0,100):
    num = random.randint(0, 20)
    list.append(num)
print(lst)

## Make sure there are no repeating elements in the list
## use an if statement
final = []
for i in lst:
    if i not in lst:
        final.append(i)
print(final)




























































