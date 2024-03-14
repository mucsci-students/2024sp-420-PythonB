@echo off
setlocal

if not defined VIRTUAL_ENV (
   set /p venv_name=venv name (will be created if it isn't in pwd):
   set "venv_path=%CD%\%venv_name%"
   dir "%venv_path%" > nul 2>&1
   if not %errorlevel% equ 0 (
        py -m venv "%venv_name%"
   )
)

source "$PWD/$env_name/bin/activate"
pip install "$PWD"
clear
python3 uml.py
clear
