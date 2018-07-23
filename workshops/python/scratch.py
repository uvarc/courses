#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 10:30:00 2018

@author: cag3fr
"""

# This is a comment.

"""
This is a block of comments.

"""

# %%
print(Hello World!)

# %%

print("Hello World!")

print("Thank you!")

# %%

1+1
2+3

# %%

print(1+2.3)
print(4-5)
print(67*7.8)
print(9.0/1.2)
print(3**4)
print(12%7)
print(12//7)

print(1-(2*4)/2)


print(0.5*50+7)

# %%

x = 1
print(x)
x = x + 1
print(x)

# %%

y = 5

myVar = x + y

print(myVar)

# %%

googol = 1.0e100
print(googol)
print(type(googol))

googol_int = 10**100
print(googol_int)
print(type(googol_int))

print(googol_int - googol)

print(googol == googol_int)

# %%

firstName = "Bilbo"
lastName = "Baggins"

myName = firstName + " " + lastName

print(myName)

print("chocolate" > "broccoli")

# %%

python_is_fun = True
python_is_boring = False

print(python_is_fun + python_is_boring)

print(python_is_fun + 3) 

# %%

my_list =  [1, 1, 2, 3, 5, 8]

print(my_list[0])

print(my_list[5])
print(my_list[-1])

# %%

my_list.append(my_list[-2] + my_list[-1])
print(my_list)

# %%

my_tuple = (1, 1, 2, 3, 5, 8)

my_tuple.append(my_tuple[-2] + my_tuple[-1])

# %%

my_slice = my_list[0:3]

print(my_slice)

# %%

my_set = {1, 2, 3, 4}
print(my_set)

my_set = {1, 1, 2, 2}
print(my_set)

# %%

dna_basepairs = {"A": "T", "C": "G"}

print(dna_basepairs["A"])

print(dna_basepairs["T"])

# %%

dna_basepairs = {"A": "T", "C": "G", "G": "C", "T": "A"}

print(dna_basepairs["A"])
print(dna_basepairs["C"])
print(dna_basepairs["G"])
print(dna_basepairs["T"])

# %%

dna_basepairs = {"A": "T", "C": "G", "G": "C", "T": "A"}

myDNA = "ATGGTGAGCAAG"
comp_seq = ""

for base in myDNA:
    comp_seq = comp_seq + dna_basepairs[base]

print(comp_seq)

# %%

counter = 0

while counter < 10:
    counter =  counter + 1
    print("counter = " + str(counter))
    
# %%
    
x = 25
print("original x = " + str(x))

if x%2 == 1:
    x = x + 1

print("new x = " +  str(x))

# %%

x = 13.5

if x%2 == 1:
    x = x + 1
elif x%2 == 0:
    x = x/2
else:
    x = round(x)
    
print(x)

# %%

dna_basepairs = {"A": "T", "C": "G", "G": "C", "T": "A"}

myDNA = "ATGGTGAGCAAG"
comp_seq = ""

for base in myDNA:
    if base == "A":
        comp_seq = comp_seq + "U"
    else:
        comp_seq = comp_seq + dna_basepairs[base]

print(comp_seq)    
    
# %%

def my_func(DNA_seq):
    
    dna_basepairs = {"A": "T", "C": "G", "G": "C", "T": "A"}
    comp_seq = ""
    
    for base in myDNA:
        if base == "A":
            comp_seq = comp_seq + "U"
        else:
            comp_seq = comp_seq + dna_basepairs[base]
        
    return comp_seq

print(my_func(myDNA))

# %%

import numpy
print(numpy.sqrt(4))

import numpy as np
print(numpy.sqrt(9))

from numpy import sqrt
print(sqrt(16))

# %%

f1 = open("my_sequences.txt","r")   # opening the file for reading ("r")
for row in f1:
    print(row)
f1.close()                     # closing the file, necessary if you open using the equal sign

# Method 2
with open("my_sequences.txt","r") as f2:  # using "with", the close function is not necessary
    for row in f2:
        print(row)
        
# %%
        
with open("my_sequences.txt","r") as fi:    # my_sequences.txt is opened for reading
    with open("my_complements.txt", "a") as fo:  # a new file my_complements.txt is opened for writing with appending
        for row in fi:                      # for each row in my_sequences.txt...:
            my_seq = row.upper().rstrip()   # upper capitalizes the dna sequence, rstrip removes the line ending code
            comp_seq = my_func(my_seq)      # runs our RNA transcription function
            fo.write(comp_seq+"\n")         # writes comp_seq and newline code to my_complements.txt
            
# %%

help(print)

print?