@echo off
setlocal

:: Set the current directory
set "Current=%~dp0"

:: Activate the virtual environment
call "%Current%.venv\Scripts\activate.bat"

:: Start your Eel application without displaying a console window
start "" "%Current%.venv\Scripts\python.exe" "%Current%app.py"





