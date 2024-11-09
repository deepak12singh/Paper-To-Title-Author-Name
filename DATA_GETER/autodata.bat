@echo off
:: Store the current directory
set "CURRENT_DIR=%CD%"

:: Set the project directory path
set "PROJECT_DIR=C:\DATA_GETER"

:: Change directory to the project folder
cd /d "%PROJECT_DIR%"
if errorlevel 1 (
    echo Failed to change directory to %PROJECT_DIR%
    pause
    exit /b 1
)

:: Activate the virtual environment
call .\.venv\Scripts\activate
if errorlevel 1 (
    echo Failed to activate the virtual environment.
    pause
    exit /b 1
)
::echo Virtual environment activated.

:: Verify python in virtual environment

if errorlevel 1 (
    echo Python is not found in the virtual environment.
    pause
    exit /b 1
)

:: Check if the first argument is "here"
if "%~1"=="here" (
    :: Run the Python script with CURRENT_DIR as an argument
    ::echo Running main.py with argument %CURRENT_DIR%
    python main.py "%CURRENT_DIR%"
    if errorlevel 1 (
        echo Failed to run main.py.
        pause
        exit /b 1
    )
) else (
    echo Argument not recognized. Please use "here" as the first argument to run the script.
    pause
    exit /b 1
)

call deactivate
:: Return to the original directory
cd /d "%CURRENT_DIR%"
echo Script completed successfully.
