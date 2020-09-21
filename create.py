# Automatically create folder in desired directory
# Login to Github using API and create Repo with same name
# Grab the git remote authentication code
# Create README.md file
# git init, git add ., git commit -m "initial commit", git push -u origin master

################################# NOTES ########################################
# sys.argv: captures arguments in list [create.py, ....] 

# print("Hello from python")

# Import Modules
import sys
import os
import requests
from dotenv import load_dotenv
# call load_dotenv function
load_dotenv()

# VARIABLES
api_url = "https://api.github.com"
github_url = "https://github.com"
username = os.getenv("USERNAME")
default_path = os.getenv("DEFAULT_PATH")
github_token = os.getenv("ACCESS_TOKEN")

# COLLECT PROJECT NAME FROM INPUT
project_name = str(sys.argv[1])
print(f'Creating new repo {project_name}')
# project_name = "test"

# Confirm if user wants to change directory

def confirm_dir():
    reply = str(input(f"Project will be created in [{default_path}] ? (y/n): ")).lower().strip()
    if reply[0] == 'y':
        file_path = default_path
        return file_path
    if reply[0] == 'n':
        file_path = str(input('Enter path of parent directory (/Documents/...): '))
        if not os.path.isdir(file_path):
            file_path = str(input('Invalid path, please re-enter directory (/Documents/...): '))
        else:
            return file_path
    else:
        print("Please answer y/n")
        return confirm_dir()

file_path = confirm_dir()

# CREATE REPO IN GITHUB 

def create_repo(name=project_name, private=True):
    if private:
        payload = f'{{"name": "{name}", "private": true}}'
    else:
        payload = f'{{"name": "{name}", "private": false}}'

    headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3+json"
    }

    post_url = api_url + "/user/repos"
    try:
        req = requests.post(post_url, data=payload, headers=headers)
        req.raise_for_status()
    except requests.exceptions.RequestException as err:
            raise SystemExit(err)

create_repo()

# GIT INIT

def init_git(path=file_path, repo_name=project_name):
    try:
        os.chdir(path)
        os.system("mkdir " + repo_name)
        os.chdir(f'{path}/{repo_name}')
        os.system("git init")
        os.system(f"git remote add origin {github_url}/{username}/{repo_name}.git")
        os.system("echo '# "+repo_name+"' >> README.md")
        os.system("git add . && git commit -m 'Initial commit' && git push -u origin master")
        os.system("code .")
    except FileExistsError as err:
        raise SystemExit(err)

init_git()

# if __name__ == "__main__":
#   git_create()
