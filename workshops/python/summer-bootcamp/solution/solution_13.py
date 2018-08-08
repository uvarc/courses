#!/usr/bin/env python

# import modules
import argparse
import statistics as stats

# accept command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input gene fpkm file", type=str, required=True)
parser.add_argument("-c", "--chr", help="Chromosome", type=str, required=True)
parser.add_argument("-s", "--start", help="Start location", type=int, required=True)
parser.add_argument("-e", "--end", help="End location", type=int, required=True)
args = parser.parse_args()

# open file handle
ifh = open(args.input, 'r')

# read input file
inheader = ifh.readline()

# initialize variables to capture
gene_cnt = 0
fpkm_list = []

for line in ifh:
	line = line.strip()
	arr = line.split("\t")

	# parse location
	chrom = arr[6].split(":")[0]
	start = int(arr[6].split(":")[1].split("-")[0])
	end = int(arr[6].split(":")[1].split("-")[1])
	
	if chrom == args.chr and start >= args.start and end <= args.end:
		gene_cnt += 1
		fpkm = float(arr[10])
		fpkm_list += [fpkm]


# calculate output stats

print("FPKM stats for genes on chromosome %s between %d and %d: " % (args.chr, args.start, args.end))

if len(fpkm_list) > 0:
	print("Number of genes: %d" % len(fpkm_list))
	print("Minimum FPKM value: %f" % min(fpkm_list))
	print("Maximum FPKM value: %f" % max(fpkm_list))
	print("Average FPKM value: %f" % stats.mean(fpkm_list))
else:
	print("No genes in specified location!")


# close file handle
ifh.close()
