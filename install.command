#!/bin/bash
cd "$(dirname "$0")"

echo "🔍 Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python not found. Please install Python 3 first:"
    echo "1. Visit https://www.python.org/downloads/"
    echo "2. Download and install Python 3"
    echo "3. Run this script again"
    read -n 1 -s -r -p "Press any key to exit"
    exit 1
fi

echo "📦 Installing dependencies..."
python3 -m pip install -r requirements.txt

echo "✅ Installation complete!"
echo "You can now use the vectorization tools."
read -n 1 -s -r -p "Press any key to exit"
