#!/usr/bin/env python

# import modules
import random

# create the 2 lists
list1 = random.sample(range(0,10), 7)
list2 = random.sample(range(0,10), 5)

# user-defined merge function
def mergeLists(list1, list2):
	mergedList = []
	for x in list1:
		if x in list2:
			mergedList += [x]
	return mergedList

# call the function
list3 = mergeLists(list1, list2)

# print the output
print("List1: ", list1)
print("List2: ", list2)
print("Merged List: ", list3)

