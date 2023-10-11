@echo off
setlocal

set "Current=%~dp0"

:: Activate the virtual environment
call "%Current%.venv\Scripts\activate.bat"

:: Start your Eel application without displaying a console window
start %Current%.venv\Scripts\python.exe "%Current%app.py"

:: Deactivate the virtual environment
deactivate

pause



