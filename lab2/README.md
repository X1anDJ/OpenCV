# Lab 2

This project shows reading images in color and grayscale, displaying, and saving  using OpenCV, with additional colorspace example

## Environment
Use your OpenCV virtual environment.

## Explanation and Observation

### 1. Reading and Displaying Images
- **Function:** `cv2.imread('flower.png')`
- **Explanation:** Reads the image in color and grayscale.
- **Observation:** Displayed in grayscale.

### 2. Saving Grayscale Image
- **Function:** `cv2.imwrite('flower_gray.png', image_gray)`
- **Explanation:** Saves the grayscale version of the image.
- **Observation:** It's saved.

### 3. Extra Example: Color Space Conversion
- **Function:** 
  - `cv2.cvtColor(image, cv2.COLOR_BGR2HSV)` for HSV conversion.
  - `cv2.cvtColor(image, cv2.COLOR_BGR2LAB)` for LAB conversion.
- **Explanation:** Converts the image into HSV and LAB color spaces, used for color filtering and correction.
- **Observation:** It's good for processing

## Conclusion
This lab covers basic operations like reading, displaying, and saving images, along with an **extra example on color space conversion**. It's important for future image processing.
