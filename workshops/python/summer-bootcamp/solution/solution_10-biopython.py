#!/usr/bin/env python

import argparse
from Bio import SeqIO
from Bio.Seq import Seq

# accept command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nuc', help="Input Nucleotide FASTA", required=True)
parser.add_argument('-p', '--prot', help="Output Protein FASTA", required=True)
args = parser.parse_args()

# use biopython Seq class to translate 
protRecList = []	# create empty list
for rec in SeqIO.parse(args.nuc,"fasta"):
	prot_rec = rec.translate(to_stop=True)	# translate the seq, stop at STOP codon
	prot_rec.id = rec.id	# assign the prot seq identifier
	protRecList.append(prot_rec)	# append to the list

# write the translated sequences
SeqIO.write(protRecList, args.prot, "fasta")	# write all protein records to output file in FASTA format
