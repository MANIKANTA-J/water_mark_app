@echo off
REM Build Script for Python Watermark App (Windows)

REM Clean previous build/dist folders if they exist
IF EXIST dist (
    rmdir /s /q dist
)
IF EXIST build (
    rmdir /s /q build
)

REM Check for Python
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is not installed. Please install Python 3.6 or newer.
    exit /b 1
)

REM Check for PyInstaller
pip show pyinstaller >nul 2>&1
IF ERRORLEVEL 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
)

REM Build executable for GUI app
echo Building standalone executable...
pyinstaller --onefile --windowed run_gui.py --name WatermarkApp

echo Build complete. Executable is in the "dist" folder.