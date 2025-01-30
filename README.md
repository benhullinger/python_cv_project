# Chart Vectorization Tools

Tools for converting raster chart images to vector format in Adobe Illustrator.

## Easy Setup

1. Install Python 3 from [python.org](https://www.python.org/downloads/)
2. Double-click:
   - On Mac: `install.command`
   - On Windows: `install.bat`

## Manual Setup

If the installation script doesn't work:

1. Open Terminal (Mac) or Command Prompt (Windows)
2. Navigate to the project directory
3. Run:
```
python --version
```

4. If Python is not installed, install it using Homebrew (Mac):
```
brew install python
```

5. Install Python dependencies:
```
pip install opencv-python numpy
```

6. Place your chart images in the project directory.

## Usage

### Extract Tick Positions

1. Run the `tickpositions.py` script to extract tick positions from your chart image:
```
python tickpositions.py
```

2. Import the tick positions into Adobe Illustrator using the `import_ticks.jsx` script.

### Extract Curve Path

1. Run the `curvepath.py` script to extract the curve path from your chart image:
```
python curvepath.py
```

2. Import the curve path into Adobe Illustrator using the `import_curve.jsx` script.