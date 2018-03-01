# Introduction to the Command Line Interface (CLI)

## Requirements:

* MacOS / Linux users: Terminal
* Windows: PuTTY [[Download](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)]

## Connect:

### MacOS / Linux users

    ssh mst3k@rivanna.hpc.virginia.edu

### Windows users, in the "Host name" field of PuTTY, enter

    mst3k@rivanna.hpc.virginia.edu


## Contents:

* [Navigate the File System](#navigate-the-file-system)
* [Change the File System](#change-the-file-system)
* [Redirect Input/Output](#redirect-inputoutput)
* [Archive/Unarchive Things](#archiveunarchive-things)
* [Find Things](#find-things)
* [Manage Your Session](#manage-your-session)
* [Configure Your Environment](#configure-your-environment)
* [Interact with Other Systems](#interact-with-other-systems)
* [Basic Shell Scripting](#basic-shell-scripting)


## Change the file system

### Viewing Things

Show the contents of a file (concatenate):

    cat myfile.txt

Show only the first 20 lines or so of a file:

    head myfile.txt

Show only the last few lines of a file:

    tail myfile.txt

Page through a longer file:

    cat myfile.txt | more

Create a file without any contents:

    touch myfile.txt

Use a simple text editor `nano`

    nano myfile.txt

Make a directory (folder):

    mkdir foldername
    mkdir "here is a folder with spaces" ( <-- bad form )

Change into that directory:

    cd foldername


### Copy Things

Copy command:

    cp myfile.txt newfile.txt

Copy something in a folder to another folder:

    cp folder/item.txt folder2/

Copy everything in this directory to a folder:

    cp * folder/

Copy just .txt files into a folder:

    cp *.txt folder/

Copy a folder:

    cp -R folder1 folder2


### Move Things

Move (rename) a file:

    mv firstfile.txt secondfile.txt

Move all .txt files into a folder:

    mv *.txt folder/

Move all .txt files that start with the letter "M" into a folder:

    mv m*.txt folder1/
    mv M*.txt folder2/

Move a folder:

    mv folder1 folder2

### Delete Things

Remove a file

    rm myfile.txt

Remove a file in a directory

    rm directory_name/myfile.txt

Remove all files in a directory

    rm directory_name/*

Remove a directory and everything in it

    rm -R directory_name

Some systems will then ask you to verify, by file, that you want to delete it. If you'd like to skip that, force it with the `f` flag

    rm -Rf directory_name

### Symbolic Links

Create a symbolic link. What is a symbolic link? It's a virtual path to another file or directory in your system.

    ln -s realfile.txt symbolic-file.txt
    ln -s directory_one/ sybmolic_directory/


## Redirect Input/Output

Echo command writes arguments to output (the screen):

    echo "I am learning the command line"

You can also echo statements into files:

    echo "Here is some content for my file" > fileA

Note the single > which overwrites all previous contents of that file.

To simply ADD more contents to an existing file, use >>

    echo "Here is even more content for my file" >> fileB

Similarly, you can cat out the contents of files into other files to overwrite them:

    cat myfile.txt > fileC

Or you can append a file to another file:

    cat myfile.txt >> fileD

Overwrite NULL (empty) to an existing file:

    cat /dev/null > fileB

Find a word in a file

    cat myfile.txt | grep "dog"

You can also redirect backwards, feeding a file (for example) into a command:

    mysql db_name < sql_script.sql

## Archive/Unarchive Things

Zip:

    zip new_archive.zip folder_to_zip/
    zip new_archive.zip file1.txt file2.txt file3.txt ...

Unzip:

    unzip some_archive.zip

Tar Compress (with Gzip)

    tar -czf new_archive.tar.gz folder_to_tar/

    Flags: (c) compress; (z) use gzip; (f) write to file

Tar Decompress:

    tar -xzf another_archive.tar.gz

    Flags: (x) expand; (z) use gzip; (f) read from file

## Find Things

Find a program. Where is `bash`?

    whereis bash
    which bash

Find a word somewhere in a stack of files (any type of file)

    grep "dog" ./*

Find a word somewhere in a stack of text files

    grep "dog" /home/myaccount/*.txt

Find a word somewhere in a stack of files, possibly within deeper folders (recursively)

    grep -r "dog" ./*

Find something by name. This looks for files and directories with a specific name

    find ./ -name "1.txt"

    Parameters: (./) this directory; (-name) look for this name in files and dirs

Find a FILE by name (this looks for files with a name)

    find ./ -type f -name "1.txt"

Find a DIRECTORY by name (recursive by default)

    find ./ -type d -name "foo"


## Manage your session

Clear the screen. Get rid of the chaos!:

    clear

Look at all your previous commands with `history`:

    history

Note the line numbers. You can reuse a line by prepending a `!` to it:

    !13  # Executes the same command as line 13 in your history


## Configure your environment

### Shell Variables

Set your own variable:

* SET it with a name and value
* Use no spaces between characters
* Declare a variable without the `$` sign
* Then EXPORT it to make it available to other commands
* Retrieve it by using the `$` reference

Here is an example:

    FNAME=your-first-name
    export FNAME
    echo $FNAME

Or you can capture a phrase by wrapping it with `''` single quotes:

    FULLNAME='My Full Name'
    export FULLNAME
    echo $FULLNAME

Now incorporate variables into other commands:

    echo "Hello there $FNAME, how are you today?"

Or make that look prettier:

    echo -e "\n\n Hello there $FNAME, how are you doing today?\n\n"


### Environment Variables

Your login session also comes with several "environment" variables. Here are a few:

    echo $HOSTNAME
    echo $PATH
    echo $HOME
    echo $SHELL
    echo $HISTSIZE

These are created by the system. But you can also set your own by editing your `~/.bashrc` file.

    export FLAVOR='vanilla'

Then, to make use of this variable you could log out and back in again, or run this command:

    source ~/.bashrc

Now see if the variable is set

    echo $FLAVOR    


### Package Managers

    apt install <software-name>
    apt update
    apt upgrade

    pip install <package-name>
    pip install <package-name> --upgrade

Install a game

    apt install bastet            (Tetris)
    apt install pacman4console    (Pacman)

Play a game

    /usr/games/bastet
    /usr/games/pacman4console


## Understand your environment

Processes running

    top
    htop
    ps -al

Current date/time

    date

Uptime (how long in days/hours/minutes)

    uptime

Find other users on the system

    w

See when the last users logged in (interactive users)

    last -i


## Interact with Other Systems

You can retrieve web pages, files, data, other remote content using either `curl` or `wget`

    apt install curl wget

    curl 'https://api.github.com/repos/stedolan/jq/commits?per_page=5'
    wget 'https://api.github.com/repos/stedolan/jq/commits?per_page=5'

Note that `curl` lets you view the contents, and `wget` retrieves it as a file.

You can pipe commands together with other tools, so that you can view and filter them (eliminate clutter)

    apt install jq

    curl 'https://api.github.com/repos/stedolan/jq/commits?per_page=5' | jq '.[0]'    


Using `jq` limited to the first [0] record. Now limit to the first record, but only two fields

    curl 'https://api.github.com/repos/stedolan/jq/commits?per_page=5' \
        | jq '.[0] | {message: .commit.message, name: .commit.committer.name}'


The output is now something like this

    {
      "message": "Merge pull request #162 from stedolan. Closes #161",
      "name": "Stephen Dolan"
    }

Or try it again with all records

    curl 'https://api.github.com/repos/stedolan/jq/commits?per_page=5' \
        | jq '.[] | {message: .commit.message, name: .commit.committer.name}'


Or grab a different field from the records

    curl 'https://api.github.com/repos/stedolan/jq/commits?per_page=5' | jq -r .[].sha


    7b81a836c31500e685d043729259affa8b670a87
    c538237f4e4c381d35f1c15497c95f659fd55850
    4a6241be0697bbe4ef420c43689c34af59e50330
    1900c7bcac76777782505c89a032c18a65fcc487
    578d536233b62884764b3c5c6cd42077958d6a49


[Read more](https://discuss.rc.virginia.edu/t/jq-a-simple-json-parser/91) about basic usage of `jq`.


## Basic Shell Scripting

Scripts are simple ways of bundling up a series of commands to run in order. You can run your script manually, or scheduled to run automatically.

The basics of a shell script:

1. Create a text file with the path to `bash` in the first line, with a shebang `#!` prepended.
2. Add shell commands below that, in the order you need and expect them to run.
3. Assume the script is running from its current location, so directory paths need to be explicit.

A simple example:

    #!/bin/bash

    clear
    echo "Let me print something out for you, $FNAME"

    sleep 3

    clear

    echo -e "Here is a quote of the day:\n\n"
    qod=`curl -s http://quotes.rest/qod.json | jq -r .contents.quotes[0].quote`
    echo "  " $qod
    echo ""

## More Information

* SOM Research Computing - https://somrc.virginia.edu/
* UVA Research Computing FAQ/Knowledgebase - https://discuss.rc.virginia.edu/
* [Slide Deck](https://docs.google.com/presentation/d/1U89TFIxGQli8xOH82bZbVX8R89nzY1kYiAQmXlc3LTc/edit?usp=sharing)
# Additional Unix Commands

Before we begin the next session, lets download example data  

	wget "https://s3.amazonaws.com/somrc-workshop-data/data.tar.gz"

Use `tar` to decompress the downloaded gzipped tarball:

	tar [options ???] data_archive.tar.gz

Look at its contents -

	ls data

Notice there are some compressed files. Lets uncompress them all at once using wildcards -

	command ???




## grep 

**G**lobally search for **r**egular **e**xpression and **p**rint.

The `grep` utility searches any given input files, selecting lines that match one or more patterns.

**Syntax**:

	grep [option(s)] [pattern] [filename]

Lets look at some options on an example file in the ./data directory: `grepExampleFile.txt`

	$ cat ./data/grepExampleFile.txt
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

Search for pattern:

	grep [pattern] filename

Case-insentive search:

	grep -i

Word search: 

	grep -w 

Print additional lines (num) after pattern match:

	grep -A<num>

Print additional lines (num) before pattern match:

	grep -B<num>

Inverse search:

	grep -v 

Print the line number of match(es):

	grep -n

Print the number(/count) of lines that match the pattern:

	grep -c 

Search all lines of `file1` in `file2`:

	grep -f file1.txt file2.txt

Refer `man` page for more ... 
	
	man grep

**The real power: `grep` supports regular expressions, a step beyond wildcards!**

Create patterns using - 

Expressions:

	.		A single character
	[abc]	Range (any one of these characters)
	[0-9]	Range (any one of these numbers)
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

	cut [option(s)] filename

Field separator (default delimiter \t):

	cut -d 

Cut on characters:

	cut -c 


## sort

The `sort` utility sorts the lines of a text file and prints to standard output.

Syntax:

	sort [option(s)] filename

Field separator (default whitespace): 

	sort -t 

Select column (`key` for sorting):

	sort -k 

Numeric sort:

	sort -n

Reverse order:

	sort -r

Combine options to perform meaningful sorting! 



## uniq 

Unique - Filters out repeated lines in file

Syntax:

	uniq [option(s)] filename

Count the number of occurences: 

	uniq -c 

Be careful: `uniq` expects duplicate lines to be adjecent. 
`uniq` is almost always used in combination with `sort`



## Exercise 

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
 
10. Typical NGS experimental design involves multiplexing of numerous samples to increase throughput. To achieve this, a unique barcode (short nucleotide sequence)is attached to the end of DNA fragments and everything is sequenced in a massively parallel way. The first step of data analysis is to separate reads into sample-specific files. The file `./data/miseq_raw.fasta` has data from a multiplexed sequencing experiment, with a 12bp barcode attached at the beginning of each read. Find how many reads are sequenced for each sample. 


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

We have a custom database of known microbial 16S rRNA gene sequences and a query set of 10 unknown sequences. Lets find out what those sequences are using BLAST alignment  

### Installing BLAST

1. Download BLAST+ from the FTP Server:

	wget "ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.7.1+-x64-linux.tar.gz"

2. Decompress the tarball

3. Check out the binaries 

4. Change your $PATH environment

	export PATH="$PATH:/PATH-TO-BIN-FOLDER/"

This tells the system where to find BLAST+ executables


### Step 1: Format reference database
To perform sequence alignment locally on a custom database, we need to first format the database. 

	makeblastdb -help

	makeblastdb -dbtype nucl -in ./data/16SMicrobial.fasta

Mandatory!!!

### Step 2: Perform the alignment
Lets perform a nucleotide-nucleotide BLAST

	blastn -db ./data/16SMicrobial.fasta -query ./data/query.fasta -outfmt 6 -out ./data/blastn_output.txt

## Bash Script

Lets write a simple bash script to perform both steps:

Create an empty script file:

	touch myBlastScript.sh

Add the following lines to the file using your favorite text editor:

		
	#!/bin/bash

	# Step1 
	makeblastdb -dbtype nucl -in ./data/16SMicrobial.fasta

	# Step2
	blastn -db ./data/16SMicrobial.fasta -query ./data/query.fasta -outfmt 6 -out ./data/blastn_output.txt
	


Make the script executable

	chmod 755 myBlastScript.sh

Execute the script

	./myBlastScript.sh


Let's make the script more flexible. 
Accept the reference, query and output files from command line

	
	#!/bin/bash
	
	REF=$1
	QUERY=$2
	OUT=$3
	
	# Step1 
	makeblastdb -dbtype nucl -in ${REF}
	
	# Step2
	blastn -db ${REF} -query ${QUERY} -outfmt 6 -out ${OUT}
	
	echo "Done!"
	

To execute the above script:

	./myBlastScript.sh <REF> <QUERY> <OUT>

**Yay! You are now ready to search "any" query sequence(s) against "any" custom reference database!!!**
