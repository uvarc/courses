# Introduction to the Command Line Interface (CLI)

Requirements:

* MacOS / Linux users: Terminal
* Windows: PuTTY [[Download](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)]

Connect:

    ssh labuser@shell.uvasomrc.io

Contents:

* [Navigating the File System](#navigating-the-file-system)
* [Changing the File System](#changing-the-file-system)
* [Redirecting Input/Output](#redirecting-inputoutput)
* [Archive/Unarchive Things](#archiveunarchive-things)
* [Finding Things](#finding-things)
* [Managing Your Session](#managing-your-session)
* [Configuring Your Environment](#configuring-your-environment)
* [Interacting with Other Systems](#interacting-with-other-systems)
* [Basic Shell Scripting](#basic-shell-scripting)

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

### View Things

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
    touch "my file with spaces.txt" ( <-- bad form )

Use a simple text editor `nano`

    nano myfile.txt

Make a directory (folder):

    mkdir foldername
    mkdir "here is a folder with spaces" ( <-- bad form )

Change into that directory:

    cd foldername

POSIX ownership bits:

    -rw-r--r-- 1 root root    60 Sep  1 16:24 data.tsv
    -rw-r--r-- 1 root root 11251 Sep  1 16:23 longfile
    drwxr-xr-x 2 root root  4096 Sep  1 16:24 myfolder
    drwxr-xr-x 2 root root  4096 Sep  5 19:54 scripts
    -rw-r--r-- 1 root root    22 Sep  1 16:23 shortfile

Three levels of control:

* Owner - `rwx` (Read / Write / Execute)
* Group - `rwx`
* Other - `rwx`

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

## Finding Things

Find where a program is. Where is `bash`?

    whereis bash
    which bash

Find a word somewhere in a stack of files

    grep "dog" ./*

Find a word somewhere in a stack of text files

    grep "dog" /home/myaccount/*.txt

Find a word somewhere in a stack of files, possibly within deeper folders (recursively)

    grep -r "dog" ./*

Find something by name

    find ./ -name "1.txt"

    Parameters: (./) this directory; (-name) look for this name in files and dirs

Find a FILE by name (this looks for files with a name)

    find ./ -type f -name "1.txt"

Find a DIRECTORY by name (recursive by default)

    find ./ -type d -name "foo"


## Managing your session

Clear the screen. Get rid of the chaos!:

    clear

Look at all your previous commands with `history`:

    history

Note the line numbers. You can reuse a line by prepending a `!` to it:

    !13  # Executes the same command as line 13 in your history


## Configuring your environment

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

## Understanding your environment

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


## Interacting with Other Systems

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
