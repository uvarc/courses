#!/usr/bin/env python

# import modules
import argparse

# accept command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input wide-format file", required=True)
parser.add_argument("-o", "--output", help="Output long-format file", required=True)
args = parser.parse_args()

# open file handles
ifh = open(args.input, 'r')
ofh = open(args.output, 'w')

# read input file
inheader = ifh.readline()
inhead_arr = inheader.split('\t')

# initialize dictionary
myDict = dict()

for line in ifh:
	line = line.strip()
	arr = line.split("\t")

	myDict.setdefault(arr[0],{})
	myDict.setdefault(arr[0],{}).setdefault('lastName', arr[1])
	myDict.setdefault(arr[0],{}).setdefault('firstName', arr[2])
	myDict.setdefault(arr[0],{}).setdefault('bonus', arr[3])

# output file 
outheader = ["ID", "Field", "Value"]
print("\t".join(outheader), file = ofh)

for k,v in sorted(myDict.items()):
	outstr1 = [k, "LastName", v['lastName']]
	print("\t".join(outstr1), file=ofh)
	outstr2 = [k, "FirstName", v['firstName']]
	print("\t".join(outstr2), file=ofh)
	outstr3 = [k, "Bonus", v['bonus']]
	print("\t".join(outstr3), file=ofh)

# close file handles
ifh.close()
ofh.close()
