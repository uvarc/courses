## Esxercises

The afternoon lab component is intended to give you a chance to explore and use the tools discussed in the morning lecture. These exercises introduce new concepts as well, and in doing so point towards various tools and documentation. Feel free to spend as much or as little time with each prompt.

---

### Learn Git Branching

Git branching is an important and sometimes difficult concept to learn. A group of developers have created a very helpful tool for exploring how branches behave.

Go through the **Learn Git Branching** exercises:

<https://learngitbranching.js.org/>

Alternatively, visit the sandbox to interactively make commits, create branches, merge branches, etc.:

<https://learngitbranching.js.org/?NODEMO>

---

### Good Commit Messages

Every `git commit` requires an accompanying message. At minimum this should be a single "subject line" briefly describing the changes made. However, the commit message can include a "body" with more thorough and descriptive notes about how / why the edits were implemented. These comments are particularly useful for a future **maintainer** or **contributor** ... and that person might be you! So you can do yourself a huge favor by creating good commit messages. 

Take some time to read a blog post by developer Chris Beams titled "How to Write a Git Commit Message":

<https://chris.beams.io/posts/git-commit/>

Try making a new commit locally to your `quality/` repository. Use a commit message with a body.

---

### Syncing a Fork

When you fork a repository, you bring along all of the files, commits and associated version control information ... *starting from the point in time when it was forked*.

As you continue to work on your fork, the *upstream* repository (from which you originally forked) may or may not be static. The owner or other contributors might modify the contents, creating commits that depart from the tree structure that you are tracking.

To keep up with these changes you must **sync** the fork:

<https://help.github.com/articles/syncing-a-fork/>

Use the documentation above to sync your fork of the `foods/` repository with the upstream:

<https://github.com/uvasomrc/foods>

---

### Create a conflict

The basic unit of Git is the repository. However, GitHub slightly extends to this concept in its *Gist* service, which essentially allows users to upload snippets of code without having to track an entire repository.

For this exercise, you'll be working from code hosted in a GitHub Gist:

<https://gist.github.com/JonathanMH/397fc427842614dd4803>

Start by cloning the Gist:

<https://help.github.com/articles/forking-and-cloning-gists/>

`create_conflict.sh` is a shell script that demonstrates what happens when there is a conflict in git commits. Try running it on your computer ... and if you're not sure how to do that, Google it!

**Make sure you are running this script relative to a directory location (folder) that you are comfortable making a new folder called `git-repo/` ... feel free to delete this folder after the exercise.**

---

### GitHub Pages

In addition to hosting free public repositories, GitHub also provides a service to host *static* websites called GitHub Pages:

https://pages.github.com/

Follow the 5 steps on the GitHub Pages website to get started.

If you would like a more advanced example, try forking the following repo:

<https://github.com/onlywei/explain-git-with-d3>

Forking remotely copies an **upstream** repository from one account to another. Because it is operating on the repository level, the fork inherits all commits *and* branches. In this case the `explain-git-with-d3` repo includes branch named `gh-pages`. As a service, GitHub.com will host anything that is stored in a `gh-pages` branch. To access the hosted version of the contents, you can go to `https://{USERNAME}.github.io/{REPOSITORYNAME}`
