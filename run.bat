@echo off
setlocal

REM Set the title of the command prompt window
title File Handler

REM Set the name of the virtual environment directory
set VENV_DIR=venv_handler

REM Check if the virtual environment directory exists
if not exist "%VENV_DIR%" (
    REM Create the virtual environment
    echo Creating virtual environment...
    python -m venv %VENV_DIR%

    REM Activate the virtual environment
    echo Activating virtual environment...
    call "%VENV_DIR%\Scripts\activate"

    REM Install requirements
    echo Installing requirements...
    pip install -r requirements.txt
) else (
    REM Activate the virtual environment if it already exists
    echo Activating existing virtual environment...
    call "%VENV_DIR%\Scripts\activate"
)

REM Run the Streamlit app
echo Running Streamlit app...
streamlit run app.py

endlocal
