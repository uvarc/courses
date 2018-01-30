# Additional Unix Commands

Before we begin the next session, lets download example data  
Use `tar` to decompress the downloaded gzipped tarball:
```
wget ""
tar [options ???] data_archive.tar.gz
```

Lets look at its contents:
```
$ ls data
```


## grep 

**G**lobally search for **r**egular **e**xpression and **p**rint.

The `grep` utility searches any given input files, selecting lines that match one or more patterns.

**Syntax**:
```
grep [option(s)] [pattern] [filename]
```

Lets look at some options on an example file in the ./data directory: `exampleFile_grep.txt`

```
$ cat ./data/exampleFile_grep.txt
Lets have fun with grep!
THIS LINE IS WRITTEN IN UPPER CASE.
this line is written in lower case.
This Line Is Written In Title Case.
The quick brown fox jumps over the lazy dog!
May the force be with you! 
Alvin, Simon and Theodore.
123 456 789
This line also contains numbers: 434 924 0311
Line10: This is the last line of the file.
```

Search for pattern:
```
grep [pattern] filename
```

Case-insentive search:
```
grep -i
```

Word search: 
```
grep -w 
```

Print additional lines (<num>) after pattern match:
```
grep -A<num>
```

Print additional lines (<num>) before pattern match:
```
grep -B<num>
```

Inverse search:
```
grep -v 
```

Print the line number of match(es):
```
grep -n
```

Print the number (count) of lines that match the pattern:
```
grep -c 
```

Search all lines of `file1` in `file2`:
```
grep -f file1.txt file2.txt
```

Refer `man` page for more ... 
```
man grep
```

**The real power: `grep` supports regular expressions, a step beyond wildcards!**

Create patterns using - 

Expressions:

	.		A single character
	[abc] / [0-9]	Range (any one of these characters)
	\		Backslash, escape char
	|		The logical "or" operator
	
Anchors:

	^		Beginning of line
	$		End of line
	\<		Beginning of word
	\>		End of word
	\b		Beginning/End of word

RE Multipliers:

	?	Preceeding item is optional
	*	Preceeding item matched zero or more times
	+	Preceeding item matched one or more times
	{n}	Preceeding item _n_ times
	{n,m}	Preceeding item matched between _n_ and _m_ times 

This is not a comprehensive list. Wealth of information on Google! Spend some time understanding how to represent a pattern using regular expression. Practice! Practice! Practice!



## cut

The `cut` utility cuts portions of file (used for selecting columns)

**Syntax**:
```
cut [option(s)] filename
```

Field separator (default delimiter \t):
```
cut -d 
```

Cut on characters:
```
cut -c 
```


## sort

The `sort` utility sorts the lines of a text file and prints to standard output.

Syntax:
```
sort [option(s)] filename
```

Field separator (default whitespace): 
```
sort -t 
```

Select column (`key` for sorting):
```
sort -k 
```

Numeric sort:
```
sort -n
```

Reverse order:
```
sort -r
```

Combine options to perform meaningful sorting! 



## uniq 

Unique - Filters out repeated lines in file

Syntax:
```
uniq [option(s)] filename
```

Count the number of occurences: 
```
uniq -c 
```

Be careful: `uniq` expects duplicate lines to be adjecent. 
`uniq` is almost always used in combination with `sort`



## Exercises: 

1. Count the number of lines of file `./data/sample_transcripts.gtf`

2. Print lines 2501 to 2750 of file `./data/sample_transcripts.gtf`

3. Count number of transcripts with read_support of "yes" in file `./data/sample_transcripts.gtf`  

4. Print gene_id and FPKM value of top10 genes with highest FPKM values in file `./data/sample_genes.fpkm_tracking`

5. Print total number of species represented in `./data/16SMicrobial.fasta` 

**Your turn:**

6. Count the number of reads mapped to transcripts on every chromosome in file `./data/sample_transcripts.gtf`

7. Calculate a histogram of various Lactobacilli species in the 16S microbial database in file `./data/16SMicrobial.fasta`. Print top 5 species.

8. Identify reference sequences belonging to Streptococcus, Staphylococcus, and Lactobacillus genera in the 16S microbial database `./data/16SMicrobial.fasta` Save the sequences in a new file `16SMicrobial.subset.fasta`

9. Print email address of Instructors teaching workshops that are part of _Bioinformatics on HPC_ track. The workshop details are in `./data/somrc_spring2018_workshops.txt` while the contact information of instructors is in `./data/somrc_instructors.txt`
 
10. Typical NGS experimental design will include multiplexing of numerous samples to increase throughput. This step involves attaching a unique barcode (short nucleotide sequence) to the end of DNA fragments and sequencing everything in a massively parallel way. The first step of data analysis is to separate reads into sample-specific files. The file `./data/miseq_raw.fasta` has data from a multiplexed sequencing experiment, with a 8bp barcode attached at the beginning of each read. Find how many reads are sequenced for each sample. 


## Command-Line BLAST 

BLAST (Basic Local Alignment Search Tool) finds regions of similarity between biological sequences, nucleotide and/or proteins. It helps to infer functional and evolutionary relationships between genes and proteins of interest. [Learn more](https://blast.ncbi.nlm.nih.gov/Blast.cgi)

Web BLAST exists! So why learn how to use it on the command line?
* not rely on NCBI servers
* don't have to wait for search to finish and download the results
* query on custom databases of interest
* use multi-threading to speed the alignments
* use BLAST as a part of larger analysis pipeline
* the list goes on ... and on ... and on ...  

What are my command line options? 
1. Write a code that uses BLAST APIs to submit a batch of sequences to be processed at NCBI or cloud service provider(s) and fetch the results, or
2. Download the software, along with reference databases and run it locally

We will do the latter! 

**Problem:**

We have a custom database of known microbial 16S rRNA gene sequences, and a query set of 10 unknown sequences. Lets find out what those sequences are using BLAST alignment  


### Installing BLAST

1. Download BLAST+ from the FTP Server:
```
wget "ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.7.1+-x64-linux.tar.gz"
```

2. Decompress the tarball

3. Check out the binaries 

4. Change your $PATH environment
```
export PATH="$PATH:/PATH-TO-BIN-FOLDER/"
```
This tells the system where to find BLAST+ executables


### Step 1: Format reference database
To perform sequence alignment locally on a custom database, we need to first format the database. 
```
makeblastdb -help

makeblastdb -dbtype nucl -in ./data/16SMicrobial.fasta
```
Mandatory!!!

### Step 2: Perform the alignment
Lets perform a nucleotide-nucleotide BLAST
```
blastn -db ./data/16SMicrobial.fasta -query ./data/query.fasta -outfmt 6 -out ./data/blastn_output.txt
```

## Bash Script

Lets write a simple bash script to perform both steps:

Create an empty script file:
```
touch myBlastScript.sh
```

Add the following lines to the file using your favorite text editor:
```
#!/bin/bash

# Step1 
makeblastdb -dbtype nucl -in ./data/16SMicrobial.fasta

# Step2
blastn -db ./data/16SMicrobial.fasta -query ./data/query.fasta -outfmt 6 -out ./data/blastn_output.txt
```

Make the script executable
```
chmod 755 myBlastScript.sh
``` 

Execute the script
```
./myBlastScript.sh
```

Let's make the script more flexible. 
Accept the reference, query and output files from command line

```
#!/bin/bash

REF=$1
QUERY=$2
OUT=$3

# Step1 
makeblastdb -dbtype nucl -in ${REF}

# Step2
blastn -db ${REF} -query ${QUERY} -outfmt 6 -out ${OUT}

echo "Done!"
```

To execute the above script:
```
./myBlastScript.sh <REF> <QUERY> <OUT>
```

