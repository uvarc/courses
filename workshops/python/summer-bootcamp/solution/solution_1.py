#!/usr/bin/env python

a=[1,2,3] 
b = a[:]
c = a
b[0] = 5
c[0] = 10

# print values of a and b
print("List a: ", a)
print("List b: ", b)
print("List c: ", c)
