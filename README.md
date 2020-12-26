# Git Automation Tool

## What is Git Automate?
Git automate is a convenient time-saving tool which automatically creates both a local repo on the client side and a remote repo on Github.

1. Navigates to folder with python script
2. Creates a folder with project name
3. Navigates into folder
4. git init
5. Goes to GitHub and creates a new repository (start private)
6. Copies the remote repo ssh
7. Adds a remote to the local folder
8. Creates a README file
9. Git add .
10. Git commit
11. Git push -u origin master
12. Code .
13. Add source function to .zshrc or .bash_profile

## Installation
<<<<<<< HEAD
You can either clone it via github or fork it.

## Usage
Program is executed using the command <code>create repo_name</code>

## Notes
Remember to make the shell script executable by running <code>chmod +x git-automate.sh</code>
In the .bash_profile or .zshrc file in root directory add the following line to the file:
<code>source ~/path/to/git-automate.sh</code>