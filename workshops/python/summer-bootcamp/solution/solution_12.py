#!/usr/bin/env python

# import modules
import sys
import statistics as stats

# accept command-line arguments
# print usage
if len(sys.argv) < 2:
	print("USAGE: python %s <gradesFile>" % sys.argv[0])
	sys.exit()
# input file argumen1
inFile = sys.argv[1]

# Open file handle
fh = open(inFile, 'r')

# Print the output header
header = ["Student", "FinalScore", "FinalGrade"]
print("\t".join(header))

# iterate over the input file
fh.readline()	# read input header 
for line in fh:
	line = line.strip()	# strip white characters
	arr = line.split('\t')	# split the line into a list

	# calculate avg score
	scores = arr[1:]
	scores = [int(x) for x in scores]
	score = float(stats.mean(scores))
	
	# determine the grade
	grade = ""
	if score >= 90.0:
		grade = "A"
	elif score >= 80.0 and score < 90.0:
		grade = "B"
	elif score >= 70.0 and score < 80.0:
		grade = "C"
	elif score >= 60.0 and score < 70.0:
		grade = "D"
	else:
		grade = "F" 

	# write output
	score = "%.2f" % score
	outArr = [arr[0], score, grade]

	print("\t".join(outArr))


# Close file handle
fh.close()

sys.exit()
