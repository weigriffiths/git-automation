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
  source .env
  cd NEW_DIR
  
  }



# ORIGINAL SHELL COMMANDS
# prompt user input
  # while true; do
  #   read -p "Project will be created in [$DEFAULT_PATH] ? (Y/N)  " ANSWER
  #   case "$ANSWER" in
  #       [Yy]*) 
  #         PATH="$DEFAULT_PATH/$1"
  #         break;;
  #       [Nn]*) 
  #         read -p "Enter location of parent directory: " DIR
  #         PATH="$DIR/$1"
  #         break;;
  #       *) echo "Please answer yes or no.";;
  #   esac
  # done

  # # check if path is correct if not default
  # if [ ! -z "$PATH" ] 
  # then 
  # echo "Saving to default path."
  # PATH="$DEFAULT_PATH/$1"
  # fi

  
  # echo "$PATH"

  # Git commands
  # git init
  # git remote add origin git@github.com:$USERNAME/$1.git
  # touch README.md
  # git add .
  # git commit -m "Initial commit"
  # git push -u origin master
  # code .