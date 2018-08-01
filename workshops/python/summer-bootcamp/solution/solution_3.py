#!/usr/bin/env python

# create the string
myStr = "The quick brown fox jumped over the lazy dog."

# split it into a list
myArr = myStr.split(" ")

# print the list
print("Original list: ", myArr)
# print the list with the index
for i,x in enumerate(myArr):
	print("Index: %d, Value: %s" % (i,x))

# delete the word "brown" at index 2
del myArr[2]

# print the modified list
print("Modified list: ", myArr)
