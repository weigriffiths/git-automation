#!/bin/zsh

# test
# function print_my_input() {
#   echo 'Your input: ' $1
# }

# ECHO COMMANDS
# Remember to make shell script executable by running: chmod 755 {filename of .sh}
# Place "source ~/{filepath}/{name.sh}" in .bash_profile to execute globally

# CHECKLIST
# Create function that runs python program
# Ensure python program is executable 
# Variables in env

function create() {
  # navigate to python file that creates git repo
  cd Documents/Wei/dev/automation/github-automation
  # open python file and input project name as argument
  python create.py $1
  }