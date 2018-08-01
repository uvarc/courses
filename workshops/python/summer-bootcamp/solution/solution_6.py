#!/usr/bin/env python

# import modules
import argparse

# accept command line argument
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input sequence FASTA file", required=True)
parser.add_argument("-o", "--output", help="Output statistics file", required=True)
args = parser.parse_args()

# GC content function
def gc_content(seq):
	g = seq.count("G")
	c = seq.count("C")
	gc = ((g + c) / float(len(seq))) * 100.0
	return "%.2f" % gc

# open file handles
ifh = open(args.input, 'r')
ofh = open(args.output, 'w')

# print output header
header = ["Sequence", "Length", "Acount", "GC"]
print("\t".join(header), file=ofh)

# read the input file 
for line in ifh:
	line = line.strip()

	# capture seqID
	if line.startswith(">"):
		seqid = line[1:]
		continue

	else:
		seq = line
	
		# calculate stats
		seq_len = len(seq)
		seq_Acount = seq.count("A")
		gc = gc_content(seq)				
		
		# print output
		outArr = [seqid, seq_len, seq_Acount, gc]
		outArr = [str(x) for x in outArr]
		print("\t".join(outArr), file=ofh)
	
# close file handles, exit gracefully
ifh.close()
ofh.close()
print("Done!")
