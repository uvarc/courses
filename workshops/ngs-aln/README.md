# Next generation Sequence Alignment

The goal of this hands-on workshop is to perform a simple NGS data alignment against a long reference genome, using the computational resources of [Rivanna](https://arcs.virginia.edu/rivanna), UVA's high-performance computing system. We will use popular short-read aligners like BWA/Bowtie2, followed by further manipulation of SAM/BAM file formats.  
 
**Note:** Do not use the same command options for you project data. The parameters used in the workshop are for demonstration purpose only, to familiarize yourself with different tools, its syntax and to understand the outputs. 

## Pre-requisites
- Familiarity with Unix command line
- Familiarity with terminal-based text editor
- Familiarity with Rivanna
- Basic understanding of NGS sequencing data 


## Tools
- [BWA](http://bio-bwa.sourceforge.net/)
- [Bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/index.shtml)
- [SAMtools](http://samtools.sourceforge.net/)
- [picard](https://broadinstitute.github.io/picard/)
- [bcftools](https://samtools.github.io/bcftools/bcftools.html)
- [IGV](http://software.broadinstitute.org/software/igv/)


## Rivanna allocations

For today's workshop, we will use the `somrc-hpc-workshop` allocation to run our jobs on Rivanna.  
**Note:** You will be removed from this _mygroup_ at the end of today's session.


## Copy the data

We will work with a random subset of reads from the whole genome sequencing data of _NA12878_, a participant of the 1000 Genomes Project. We will align the reads to _hg19_ build of human genome. 

Copy the data to your `scratch` directory - 

	cp /scratch/hp7d/ngs-aln.tar.gz /scratch/<mst3k>/

Decompress the tarball, and unzip the files within - 

	cd /scratch/<mst3k>/
	tar -xzvf ngs-aln.tar.gz
	gunzip ngs-aln/reference/hg19.fa.gz
	gunzip ngs-aln/sample/*.gz 

**Note:** At the end of today's session, you will not have access to files stored in `/scratch/hp7d/`.  
To download the human genome [click here](http://hgdownload.cse.ucsc.edu/downloads.html).  
To download sequence data from 1000 Genomes Project [click here](http://www.internationalgenome.org/data).


## Alignment

We will perform sequence alignment using popular aligners like BWA-MEM and Bowtie2.  
BWA and Bowtie2 use the Burrows-Wheeler Transform algorithm to index the reference genome. This allows for rapid identification of potential origin of your query sequence within the large genome, with a relatively small memory footprint. I strongly encourage you to read the publication/manual pages for algorithm details.  
 
Alignemnt is a two-step process: 
- indexing the genome (only perform once)
- aligning sample reads
 
We will go over the command to execute both the steps on Rivanna, under different scenarios. 


### Case 1
**_You want to align reads to a reference genome interactively on one of Rivanna's compute node_**

We will use *_BWA MEM_* for this section!

You should **NOT** do your computational processing on the head node.  

In many cases, especially when you are testing/developing your analysis pipelines, you may want to perfrom the task interactively on a compute node. This can be achieved by using the `ijob` command and requesting appropriate resources.  


#### Start an interactive session, prepare environment - 
	
	ijob -A somrc-hpc-workshop -p standard -c 20 --mem=20gb

Load the bwa module - 

	module load bwa

Check all available _bwa_ commands - 

	bwa <ENTER>

In order to check different options for each command - 

	bwa index <ENTER>

_(Optional)_ Export a work-dir variable, so that you dont have to type full file paths 

	export WORKDIR="/scratch/<mst3k>/ngs-aln/"

#### Create the index
**DO NOT EXECUTE THIS!** 

Indexing needs to be done only once for a particular _version_ of a genome. Indexing full human genome takes ~1hr. This has already been done, using the below command - 

	bwa index /PATH/TO/hg19.fa

This will create new files with extentions - `.amb`, `.ann`, `.bwt`, `.pac`, `.sa` in the same location as reference fasta file. These files constitute the index. You will never directly reference these files. _BWA_ will know how to find them based on the basename.  

The index files are located at `/scratch/hp7d/ngs-aln/hg19_bwaIndex/`.


#### Align Reads

Next, we will align the sample data to the reference genome, indexed in the previous step.

First, make a directory to save the output 

	mkdir /scratch/<mst3k>ngs-aln/bwaOut
	cd /scratch/<mst3k>ngs-aln/bwaOut
	
Align the reads 

	bwa mem -M -t 20 /scratch/hp7d/ngs-aln/hg19_bwaIndex/hg19.fa /scratch/<mst3k>/sample/NA12878_R1.subset.fastq /scratch/<mst3k>/sample/NA12878_R2.subset.fastq > /scratch/<mst3k>/bwaOut/NA12878_subset.bwa.sam

This command aligns the forward (R1) and reverse (R2) reads to the indexed hg19 reference genome using _20_ threads and writes the output to `NA12878_subset.bwa.sam` SAM file.  
This step will take ~5 mins.

#### Relinquish allocations  

	exit


### Case 2
**_You want to submit the alignment job using a SLURM submission script_**

We will use *_Bowtie2_* for this section. 

Create a bowtie2 output directory and `cd` to it - 

	mkdir /scratch/<mst3k>/ngs-aln/bwtOut
	cd /scratch/<mst3k>/ngs-aln/bwtOut

Next, create an empty _SLURM_ sbatch submission script - 

	touch bowtie2-aln.slurm.sh

Open the file in your favorite terminal-based text editor and paste the contents from `bowtie2-aln.slurm.sh` script on [parikhhi:GithubGist](https://gist.github.com/parikhhi/42a4e114502e557557cfe727f1266ad1#file-bowtie2-aln-slurm-sh) page.

**Modify its contents!!!**

Bowtie2 index files for hg19 - `/scratch/hp7d/ngs-aln/hg19_bwtIndex/hg19.fa`

Submit the job - 

	sbatch bowtie2-aln.slurm.sh

Monitor the progress of your job -  

	jobq 

	OR

	squeue -u <mst3k>


[Learn More](https://arcs.virginia.edu/slurm) about SLRUM batch submission.


### Case 3
**_You want to run the alignment command for multiple samples, simultaneously_**

In case you would like to submit a large number of jobs through one request, the recommended method is to use the `sbatch array` job submission.  

We will walk through the steps to set up an array job, to process 10 alignment jobs simultaneously.

**Set up** 

Create 10 copies of sample reads
	
	cd /scratch/<mst3k>/ngs-aln/sample

	for i in {1..10}; do head -10000 NA12878_R1.subset.fastq > sample${i}_R1.fastq; done
	for i in {1..10}; do head -10000 NA12878_R2.subset.fastq > sample${i}_R2.fastq; done

Create a working directory 

	mkdir /scratch/<mst3k>/ngs-aln/bwtOut-array
	cd /scratch/<mst3k>/ngs-aln/bwtOut-array

**Create `seedfile.txt`**  

Create the `seedfile.txt`, a text file with one-command-per-line.  
This can be created in your favorite scripting language, or manually (if you have the patience!). We will write a simple bash script to do this - 

	% cat create_seedfile.sh

	#!/bin/bash
	for r1file in /scratch/<mst3k>/ngs-aln/sample/*_R1*fastq; do
		r2file=${r1file/R1/R2}
		sname=`echo $r1file | cut -d "/" -f 6 | cut -d "_" -f 1`
		echo -e "bowtie2 -x /scratch/<mst3k>/ngs-aln/hg19_bwtIndex/hg19.fa -1 ${r1file} -2 ${r2file} -p 20 -S /scratch/<mst3k>/ngs-aln/bwtOut-array/${sname}.bowtie2.sam"
	done

Open your favorite text editor and paste the above script in a file named `create_seedfile.sh`.  

Now execute the script and write the contents to the seedfile - 

	sh create_seedfile.sh > seedfile.txt


**SLURM array submission script**
 
Finally, we will write the slurm submission script - 

	touch bowtie2-aln.slurm-array.sh

Open the file in your favorite terminal-based text editor and paste the contents from `bowtie2-aln.slurm-array.sh` script on [parikhhi:GithubGist](https://gist.github.com/parikhhi/42a4e114502e557557cfe727f1266ad1#file-bowtie2-aln-slurm-array-sh) page.

**Modify its contents!!!**

To submit the job 

	sbatch bowtie2-aln.slurm-array.sh seedfile.txt


Monitor the progress of yours job -  

	jobq 

	OR

	squeue -u <mst3k>


[Learn More](https://arcs.virginia.edu/slurm) about SLRUM array jobs.


## Sequence Alignment/Map Format (SAM)

**[SAM Format](https://samtools.github.io/hts-specs/SAMv1.pdf)**

Lets explore the outputs from alignmnet step - 

	cd /scratch/<mst3k>/ngs-aln/bwtOut/

	less -S NA12878_subset.bowtie2.sam

**[SAMTools](https://github.com/samtools/samtools)**  
SAM Tools provide various utilities for manipulating alignments in the SAM format, including sorting, merging, indexing and generating alignments in a per-position format.

Start an interactive session on Rivanna's compute node - 

	ijob -A somrc-hpc-workshop -p standard -c 1 --mem=10gb

Load samtools module - 

	module load samtools

Check out various samtools commands and options for them - 

	samtools <ENTER>
	samtools view <ENTER>
	samtools index <ENTER>

**Convert SAM to BAM**

	samtools view -hSb NA12878_subset.bowtie2.sam > NA12878_subset.bowtie2.bam
	OR
	samtools view -hSbo NA12878_subset.bowtie2.bam NA12878_subset.bowtie2.sam 

**Sort BAM file on coordinates**

	samtools sort -o NA12878_subset.bowtie2.sorted.bam NA12878_subset.bowtie2.bam

**Index BAM**

	samtools index NA12878_subset.bowtie2.sorted.bam


**Picard**  
The above 3 steps can also be performed using [Picard]()

	module load picard

	java -jar $EBROOTPICARD/picard.jar SortSam I=NA12878_subset.bowtie2.sam O=NA12878_subset.bowtie2.sorted-pct.bam SORT_ORDER=coordinate CREATE_INDEX=true


**Filter BAM**  

By region of interest - 

	samtools view -h NA12878_subset.bowtie2.sorted.bam chr20 | less -S

	samtools view -h NA12878_subset.bowtie2.sorted.bam chr20:100000-500000 | less -S

	samtools view -h NA12878_subset.bowtie2.sorted.bam chr20:100000-500000 chr5:10000-15000 | less -S 


By alignment flag - 

	# filter forward reads that mapped as proper pairs
	samtools view -hf 67 NA12878_subset.bowtie2.sorted.bam | less -S 

	# filter reverse reads that mapped as proper pairs
	samtools view -hf 131 NA12878_subset.bowtie2.sorted.bam | less -S 

	# filter all unmapped reads
	samtools view -hf 4 NA12878_subset.bowtie2.sorted.bam | less -S

	# reverse the selection 
	samtools view -hF 4 NA12878_subset.bowtie2.sorted.bam | less -S

[Explain SAM Flags](https://broadinstitute.github.io/picard/explain-flags.html)


**Flagstat**  

	samtools flagstat NA12878_subset.bowtie2.sorted.bam



**BAM to FASTQ**

	samtools view -bhf 3 NA12878_subset.bowtie2.sorted.bam chr5 > NA12878_subset.bowtie2.sorted.flag3-chr5.bam
	samtools index NA12878_subset.bowtie2.sorted.flag3-chr5.bam
	samtools fastq -1 NA12878_subset.bowtie2.sorted.flag3-chr5.R1.fastq -2 NA12878_subset.bowtie2.sorted.flag3-chr5.R2.fastq NA12878_subset.bowtie2.sorted.flag3-chr5.bam


## Visualize BAM files 

We will use [IGV](https://software.broadinstitute.org/software/igv/home) to visualize our alignment results. Download from [here](https://software.broadinstitute.org/software/igv/download).  
Copy the bam file (and the index) to your local computer. On your laptop - 

	scp <mst3k>@rivanna.hpc.virginia.edu:/scratch/<mst3k>/ngs-aln/bwtOut/NA12878_subset.bowtie2.sorted.bam ./
	scp <mst3k>@rivanna.hpc.virginia.edu:/scratch/<mst3k>/ngs-aln/bwtOut/NA12878_subset.bowtie2.sorted.bam.bai ./

Lets explore!!!


## Call Variants 

We will now find locations where the reads are different from the genome, using the Bayesian variant caller - `samtools mpileup`, in conjunction with `bcftools`.  
Note: `samtools` collects summary information in the input BAMs, computes the likelihood of data given each possible genotype and stores the likelihoods in the BCF format. It does not call variants! `bcftools` takes that information and does the actual calling. 
	
	module load bcftools

	samtools mpileup -ut DP -d 8000 -f ../reference/hg19.fa NA12878_subset.bowtie2.sorted.bam > NA12878_subset.bowtie2.sorted.mpileup.bcf

	bcftools call -cv NA12878_subset.bowtie2.sorted.mpileup.bcf > NA12878_subset.bowtie2.sorted.mpileup.raw.vcf

	vcfutils.pl varFilter NA12878_subset.bowtie2.sorted.mpileup.raw.vcf > NA12878_subset.bowtie2.sorted.mpileup.flt.vcf

	
**[VCF Specifications](https://samtools.github.io/hts-specs/VCFv4.2.pdf)**  

**Visualize VCF**  
We can visualize the VCF file in IGV as well. 

