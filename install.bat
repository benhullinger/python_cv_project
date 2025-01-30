@echo off
echo 🔍 Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3 first:
    echo 1. Visit https://www.python.org/downloads/
    echo 2. Download and install Python 3
    echo 3. Run this script again
    pause
    exit /b 1
)

echo 📦 Installing dependencies...
python -m pip install -r requirements.txt

echo ✅ Installation complete!
echo You can now use the vectorization tools.
pause
