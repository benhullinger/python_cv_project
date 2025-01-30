import cv2
import numpy as np
import csv
import sys
from pathlib import Path

def process_image(image_path):
    # Ensure file exists
    if not Path(image_path).exists():
        raise FileNotFoundError(f"Image file not found: {image_path}")

    # Load and process image
    image = cv2.imread(str(image_path), cv2.IMREAD_UNCHANGED)
    if image is None:
        raise ValueError("Failed to load image")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the image (binarize: black = 255, transparent/white = 0)
    _, binary = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY_INV)

    # Get image dimensions
    height, width = binary.shape

    # Store tick mark positions
    tick_positions = []

    # Scan vertical columns for tick marks
    for x in range(width):
        black_streak = 0
        for y in range(height):
            if binary[y, x] == 255:  # Check if pixel is black
                black_streak += 1
            else:
                if 6 <= black_streak <= 7:  # Found a tick!
                    tick_positions.append((x, y - black_streak // 2))  # Store center
                black_streak = 0

    # Flip Y coordinates for Illustrator
    tick_positions = [(x, height - y) for x, y in tick_positions]

    # Save positions to CSV
    output_file = Path(image_path).stem + "_ticks.csv"
    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["X", "Y"])
        writer.writerows(tick_positions)

    return len(tick_positions), output_file

if __name__ == "__main__":
    try:
        image_path = sys.argv[1] if len(sys.argv) > 1 else "charttestwhite2.png"
        count, output_file = process_image(image_path)
        print(f"✓ Found {count} tick marks")
        print(f"✓ Saved to {output_file}")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)