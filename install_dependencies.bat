@echo off

rem Check if requirements.txt file exists
if not exist requirements.txt (
    echo Error: requirements.txt file not found.
    exit /b 1
)

rem Check for the command
if "%1" == "install" (
    rem Install dependencies from requirements.txt
    pip install -r requirements.txt

    rem Check if installation was successful
    if %errorlevel% equ 0 (
        echo Dependencies installed successfully.
    ) else (
        echo Error: Failed to install dependencies.
        exit /b 1
    )
) else if "%1" == "start" (
    rem Add your command to start your app here
    echo Starting your app...
    rem Example: python your_app_script.py
    python GUI_main.py
) else (
    echo Error: Unknown command. Use "install" or "start".
    exit /b 1
)