import cv2
import numpy as np
import csv

# Load and process image
image = cv2.imread("plat+gem.png", cv2.IMREAD_UNCHANGED)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

height, width = binary.shape
path_points = []

# Find start point (leftmost black pixel)
start_found = False
for x in range(width):
    for y in range(height):
        if binary[y, x] == 255:
            path_points.append((x, height - y))  # Flip Y coordinate for Illustrator
            start_found = True
            break
    if start_found:
        break

# Follow path using 8-direction connectivity
directions = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
x, y = path_points[0]
y = height - y  # Convert back to image coordinates for processing

while True:
    found_next = False
    binary[y, x] = 0  # Mark as visited
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height and binary[ny, nx] == 255:
            path_points.append((nx, height - ny))  # Store in Illustrator coordinates
            x, y = nx, ny
            found_next = True
            break

    if not found_next:
        break

# Save as CSV
with open("curve_path2.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["X", "Y"])
    writer.writerows(path_points)

print(f"Extracted {len(path_points)} curve points. Saved to curve_path.csv.")