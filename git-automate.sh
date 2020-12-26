#!/bin/zsh

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