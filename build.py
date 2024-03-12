import os, platform, venv, sys, subprocess
import platform
import venv
import sys
from pip._internal import main as pip_main

def main():
    '''Performs three things:
        1) sets up a venv in the current directory if one doesn't exist
        2) enters the venv in the current directory if it is not active
        3) builds the project inside the current directory in the venv
    '''
    if not os.getenv("VIRTUAL_ENV"):
        setup_venv()
    else:
        os.system("pip install .")
        

def setup_venv():
    '''Sets up and enters a virtual environment in the current directory'''
    hasVenv = input("You are not in a venv; [c]reate or activate one now: ").strip().lower()

    if hasVenv[0:] == 'c':
        name = input("Enter the name of the virtual environment: ").strip()    
        venv.create(name, with_pip=True)
    else:
        print("To activate a venv on UNIX, use 'source venv/bin/activate'")
        print("To activate a venv on Windows, use 'source venv/Scripts/Activate.ps1'")


if __name__ == '__main__':
    main()