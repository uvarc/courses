# Introduction to the Command Line Interface (CLI)

Requirements:

* MacOS / Linux users: Terminal
* Windows: PuTTY [[Download](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)]

Connect:

    ssh user@host

## Navigating the file system

Learn your way around without feeling stuck. These commands help you change directories and view their contents.

List files/folders in a directory:

    ls

List all files (even hidden) in a directory, with detailed info:

    ls -al

List all files sorted by most recent edits:

    ls -alt

Return the present working directory (where I am now):

    pwd

Change directories:

    cd <dir>

More versions of changing directories:

    cd ..
    cd ../../
    cd ../dir

Change to my home directory:

    cd ~

Change to the base directory:

    cd /

Switch back to the directory I was in before this one:

    cd -


## Changing the file system

Create a file without any contents:

    touch myfile.txt

Show the contents of a file (concatenate):

    cat myfile.txt

Show only the first 20 lines or so of a file:

    head myfile.txt

Show only the last few lines of a file:

    tail myfile.txt

Page through a longer file:

    cat myfile.txt | more

Make a directory (folder):

    mkdir foldername

Change into that directory:

    cd foldername

POSIX ownership bits:

    -rwxr-xr-x   5 user  staff     1701 Feb  3  2017 codefile.txt
    drwxr-xr-x  12 user  staff      408 Jun  8 09:41 miniconda2
    drwxr-xr-x   5 user  staff      170 Jun  8 09:36 sandbox
    drwxrwxrwx   4 user  staff      136 Apr 28 09:40 scripts

Copy command:

    cp myfile.txt newfile.txt

Copy something in a folder to another folder:

    cp folder/item.txt folder2/

Copy everything in this directory to a folder:

    cp * folder/

Copy just .txt files into a folder:

    cp *.txt folder/

Move (rename) a file:

    mv firstfile.txt secondfile.txt

Move all .txt files into a folder:

    mv *.txt folder/

Move all .txt files that start with the letter "M" into a folder:

    mv m*.txt folder/
    mv M*.txt folder/

## Redirecting Input/Output

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


## Managing your session

Clear the screen. Get rid of the chaos!:

    clear

Look at all your previous commands with `history`:

    history

Note the line numbers. You can reuse a line by prepending a `!` to it:

    !13  # Executes the same command as line 13 in your history


## Configuring your environment

### Environment Variables

    echo $HOSTNAME
    echo $PATH
    echo $HOME
    echo $SHELL
    echo $HISTSIZE

### Shell Variables

Set your own:

    FNAME=your-first-name
    export FNAME
    echo $FNAME

Now incorporate variables into other commands:

    echo "Hello there $FNAME, how are you today?"

Or make that look prettier:

    echo -e "\n\n Hello there $FNAME, how are you doing today?\n\n"


### Package Managers

    apt install xxxxx
    pip install xxxxx

## Understanding your environment

Processes running:

    top
    htop

Current date-time:

    date

Uptime (how long in days/hours/minutes)

    uptime

