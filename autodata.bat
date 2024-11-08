@echo off
:: Store the current directory
set "CURRENT_DIR=%CD%"


:: Store the project path
set "PROJECT_DIR=C:\DATA_GETER"


:: Change directory to the project folder
cd /d "%PROJECT_DIR%"
if errorlevel 1 (
    echo Failed to change directory to %PROJECT_DIR%
    pause
    exit /b 1
)

:: Check if the first argument is "hear"
if "%~1"=="here" (
    :: Run the Python script with CURRENT_DIR as an argument
    python main.py "%CURRENT_DIR%"
)
:: Return to the original directory
cd /d "%CURRENT_DIR%"
