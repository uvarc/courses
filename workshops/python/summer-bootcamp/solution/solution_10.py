#!/usr/bin/env python

import argparse

# accept command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-m', '--map', help="AminoAcid to Codon mapping", required=True)
parser.add_argument('-n', '--nuc', help="Input Nucleotide FASTA", required=True)
parser.add_argument('-p', '--prot', help="Output Protein FASTA", required=True)
args = parser.parse_args()

# open file handles
mfh = open(args.map, 'r')
ifh = open(args.nuc, 'r')
ofh = open(args.prot, 'w')

# read mapping file, store data in dict
mfh.readline()	# read the header line, ignore it
codonDict = dict()	# initialize empty dictionary
for line in mfh:
	line = line.strip()	# strip whitespace
	arr = line.split("\t")	# split line into list using tab
	aa = arr[1]	# save SLC to aa
	codons = arr[2].split(",")	# split the codons into list using ,
	for codon in codons:
		codonDict.setdefault(codon, aa)	# populate dictionary 


# user-defined function to convert nucl to prot
def nuc2prot(seq):
	prot_seq = ""
	# loop through the seq in increments of 3 bases
	for i in range(0,len(seq)-2,3):	
		seqCodon = seq[i:i+3]
		# if you encounter stop codon, stop translating
		if seqCodon in ["TAA", "TAG", "TGA"]:
			break
		else:
			prot_seq += codonDict[seqCodon]
	# return the protein sequence to the caller	
	return prot_seq


# read the input fasta file and write output
for line in ifh:
	line = line.strip()	# strip whitespace

	# capture sequence identifier
	if line.startswith(">"):
		print(line, file=ofh)
		continue
	# translate nucleotide sequence
	else:
		prot_seq = nuc2prot(line)
		print(prot_seq, file=ofh)

# close file handles
mfh.close()
ifh.close()
ofh.close()
