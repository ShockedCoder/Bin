#!/bin/python


# This was a task in my "coding" class

from math import factorial as f
size = 25
numlist = []

for i in range(size):

    for a in range(i+1):
        numlist.append(str(f(i)//(f(a)*f(i-a))))

    print(numlist)
    numlist = []