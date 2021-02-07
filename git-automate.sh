#!/bin/zsh

function create() {
  # navigate to python file that creates git repo
  cd path/to/github-automation
  # open python file and input project name as argument
  python create.py $1
  }