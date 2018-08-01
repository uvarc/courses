#!/usr/bin/env python

# import modules
import argparse

# accept command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help="Input FASTA", required=True)
parser.add_argument('-o', '--output', help="Output RC FASTA", required=True)
args = parser.parse_args()

# user-defined functions
# reverse complement function
# accepts seq as argument, returns the reverse complement sequence 
def rcFunc(seq):
	rcDict = {'A':'T', 'G':'C', 'C':'G', 'T':'A', 'N':'N'}
	rc_seq = ""
	for i in reversed(seq):
		rc_seq += rcDict[i]
	return rc_seq

# open file handles
ifh = open(args.input, 'r')
ofh = open(args.output, 'w')

# iterate over input sequences
for line in ifh:

	line = line.strip()		# strip whitespace

	# capture sequence identifier
	if line.startswith(">"):
		seqid = line + "_rc"
		print(seqid, file=ofh)
		continue
	# call the function for sequence line
	else:
		rc_seq = rcFunc(line)
		print(rc_seq, file=ofh)	

# close file handles, exit gracefully
ifh.close()
ofh.close()
