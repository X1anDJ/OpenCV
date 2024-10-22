# Lab 5

This project shows how to create color and grayscale histograms using OpenCV and Matplotlib.

## Environment
Use your OpenCV virtual environment.

## Explanation and Observation

### 1. Color Histogram
- **Function:** `cv2.calcHist([img], [i], None, [256], [0, 256])`
- **Explanation:** Creates a histogram for each color channel (Red, Green, Blue) to show pixel intensity.
- **Observation:** Reveals how colors are spread across the image.

### 2. Grayscale Histogram
- **Function:** `cv2.calcHist([img], [0], None, [256], [0, 256])`
- **Explanation:** Plots a histogram of pixel brightness for the whole image.
- **Observation:** Helps see the overall brightness and contrast.

### 3. Combined Color and Grayscale Histograms
- **Function:** Shows color and grayscale histograms side by side.
- **Explanation:** Compares the spread of colors with the overall intensity.
- **Observation:** Gives a full view of how colors and brightness work together in the image.

## Additional Example:
- **Combined Histogram Comparison:** Side-by-side display of color and grayscale histograms to show how colors and brightness relate.

## Conclusion
Histograms give useful info about the spread of colors and brightness. The **combined histogram example** helps see how the color channels and overall brightness shape the look of the image.
