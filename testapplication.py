# Create the StartApp.bat file (Windows launcher)
startapp_bat_content = '''@echo off
title PDF Tools Suite - Professional Edition
color 0A
echo.
echo ================================================
echo          PDF Tools Suite - Starting...
echo ================================================
echo.

REM Check if Python is installed
echo [INFO] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Python not found!
    echo.
    echo Please install Python 3.7+ from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

REM Display Python version
for /f "tokens=*" %%i in ('python --version') do echo [INFO] Found %%i

REM Check if main application exists
if not exist "PDFToolsApp.py" (
    echo.
    echo [ERROR] PDFToolsApp.py not found!
    echo Please make sure all application files are in the same directory.
    echo.
    pause
    exit /b 1
)

REM Check if dependencies are installed
echo [INFO] Checking dependencies...
python -c "import pypdf, reportlab, PIL" >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [INFO] Installing required dependencies...
    echo This may take a few moments...
    echo.
    pip install pypdf>=3.0.0 reportlab>=4.0.0 Pillow>=10.0.0
    
    REM Check if installation was successful
    python -c "import pypdf, reportlab, PIL" >nul 2>&1
    if %errorlevel% neq 0 (
        echo.
        echo [ERROR] Failed to install dependencies!
        echo Please try manually: pip install pypdf reportlab pillow
        echo.
        pause
        exit /b 1
    )
    echo [SUCCESS] Dependencies installed successfully!
)

echo [INFO] All dependencies are ready!
echo.
echo ================================================
echo           Starting PDF Tools Suite...
echo ================================================
echo.

REM Start the application
python PDFToolsApp.py

REM Check exit code
if %errorlevel% neq 0 (
    echo.
    echo ================================================
    echo [ERROR] Application encountered an error.
    echo ================================================
    echo.
    echo Troubleshooting tips:
    echo 1. Make sure all files are in the same directory
    echo 2. Check if Python tkinter is available
    echo 3. Try running: python -c "import tkinter"
    echo 4. See InstallationGuide.md for detailed help
    echo.
    pause
) else (
    echo.
    echo [SUCCESS] PDF Tools Suite closed normally.
)

REM Optional: Keep window open for debugging
REM pause
'''

with open('StartApp.bat', 'w') as f:
    f.write(startapp_bat_content)

print("✅ Created StartApp.bat (Windows launcher)")
print(f"   Size: {len(startapp_bat_content)} characters")