#!/usr/bin/env python

# import modules
import random
from statistics import *

# create a random list of 100 integers between 0 - 1000 
myList = random.sample(range(0, 1000), 100)

# calculate the mean
m = mean(myList)

# print the mean
print("Mean of the random list: %f" % m)
