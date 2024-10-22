# Lab 3

This project demonstrates various image transformations using OpenCV, including resizing, cropping, rotating, labeling, and flipping.

## Environment
Use your OpenCV virtual environment.

## Explanation and Observation

### 1. Resizing
- **Function:** `cv2.resize(img, (300, 300))`
- **Explanation:** Changes the size of the image to the specified dimensions.
- **Observation:** Useful for standardizing image sizes for processing

### 2. Cropping
- **Function:** `img[100:300, 100:300]`
- **Explanation:** Extracts a region of interest (ROI) from the original image.
- **Observation:** Crop a region

### 3. Rotating
- **Function:** `cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)`
- **Explanation:** Rotates the image 90 degrees clockwise.
- **Observation:** It rotates!

### 4. Labeling
- **Function:** `cv2.putText(img, 'flower', (50, 50), ...)`
- **Explanation:** Adds text to the image.
- **Observation:** Useful for annotations or labeling objects.

### 5. Extra Example: Image Flipping
- **Function:** `cv2.flip(img, axis)`
  - **`1`**: Horizontal flip.
  - **`0`**: Vertical flip.
  - **`-1`**: Flip both horizontally and vertically.
- **Explanation:** Flips the image along the specified axis for data augmentation or symmetry adjustments.
- **Observation:** Flipping is quick and useful for generating new data from existing images.

## Conclusion
These transformations help in various tasks like data preparation, annotation, and alignment. The **extra example with image flipping** is my additional example
