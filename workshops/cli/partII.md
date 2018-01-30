# Additional Unix Commands

Before we begin the next session, please [download]() the data archive.  
Use `tar` to decompress the downloaded gzipped tarball:
```
$ tar [options ???] data_archive.tar.gz
```

Lets look at its contents:
```
$ ls data_archive

drwxrwx---  2 <user>  staff    68B Jan 29 12:43 scripts		# directory containing scripts
drwxrwx---  2 <user>  staff    68B Jan 29 13:09 tools		# directory containing software
drwxrwx---  5 <user>  staff   170B Jan 29 17:34 data		# direcotry with data files

```


## grep 

**G**lobally search for **r**egular **e**xpression and **p**rint.

The `grep` utility searches any given input files, selecting lines that match one or more patterns.

**Syntax**:
```
grep [option(s)] [pattern] [filename]
```

Lets look at some options on an example file in the ./data_archive/data directory: `exampleFile_grep.txt`

```
$ cat ./data_archive/data/exampleFile_grep.txt
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

1. Print lines 2501 to 2750. File: `./data_archive/data/sample_transcripts.gtf`
```
>! head -2750 ./data_archive/data/sample_transcripts.gtf | tail -250
```

2. Count number of transcripts with read_support of "yes". File: `./data_archive/data/sample_transcripts.gtf`  
```
grep "transcript" ./data_archive/data/sample_transcript.gtf | grep "yes" | wc -l
```

3. Print gene_id and FPKM value of top10 genes with highest FPKM values. File: `./data_archive/data/sample_genes.fpkm_tracking`
```
sort -nrk 11 ./data_archive/data/sample_gene.fpkm_tracking | head | cut -f 4,11
```

4. Count the number of sequences in ./data_archive/data/16SMicrobial.fasta
```
grep ">" ./data_archive/data/16SMicrobial.fasta | wc -l
grep -c ">" ./data_archive/data/16SMicrobial.fasta
```

5. Print total number of species represented in ./data_archive/data/16SMicrobial.fasta 
```
grep ">" ./data_archive/data/16SMicrobial.fasta | cut -d "|" -f 2,3 | sort | uniq | wc -l
```

**Your turn:**

6. Print a unique list of reference sequences belonging to Streptococcus, Staphylococcus, and Lactobacillus genera in the 16S microbial database. File: `./data_archive/data/16SMicrobial.fasta`

7. Calculate a histogram of various Lactobacilli species in the 16S microbial database. Print the top10 rows. File: `./data_archive/data/16SMicrobial.fasta`

8. Print the top 5 chromosomes with most transcripts mapped. File: `./data_archive/data/sample_transcripts.gtf`



