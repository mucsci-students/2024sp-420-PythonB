import os
import platform

def main():
    '''Performs three things:
        1) sets up a venv in the current directory if one doesn't exist
        2) enters the venv in the current directory if it is not active
        3) builds the project inside the current directory in the venv
    '''
    #the alias to python is os dependent
    alias = get_prefix()

    if not os.getenv("VIRTUAL_ENV"):
        setup_venv(alias)

    if os.getenv("VIRTUAL_ENV"):
        os.system("pip install .")


def setup_venv(alias:str):
    '''Sets up and enters a virtual environment in the current directory'''

    hasVenv = input("You are not in a venv; [c]reate or activate one now: ").strip().lower()
    name = input("Enter the name of the virtual environment: ").strip()    

    if hasVenv[0:] == 'c':
        os.system(alias + " -m venv " + name)

    if alias == "py":
        os.system("powershell.exe Set-ExecutionPolicy Bypass -Scope Process")
        os.system("powershell.exe source " + name + "\\Scripts\\Activate.ps1")
    else:
        os.system("source " + name + "/bin/activate")



def get_prefix() -> str:
    '''chooses the alias to python based on the operating system.
        NOTE: Assumes all os's that don't self-identify as Windows or Linux are Mac
    '''
    os = platform.system()

    if os == "Windows":
        prefix = "py"
    elif os == "Linux":
        prefix = "python"
    else:
        prefix = "python3"

    return prefix

main()