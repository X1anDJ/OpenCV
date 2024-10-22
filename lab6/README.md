# Lab 6 

This project demonstrates four filters using OpenCV 

## Environment
Use your OpenCV virtual environment.

## Explanation and Observation

### 1. Averaging Box Filter
- **Function:** `cv2.blur(img, (5, 5))`
- **Explanation:** Averages the pixel values with kernel size for a smooth image.
- **Observation:** The image becomes blurry, and fine details are lost.

### 2. Gaussian Filter
- **Function:** `cv2.GaussianBlur(img, (5, 5), 0)`
- **Explanation:** Gives more weight to pixels near the center of the kernel, which helps retain edges better than the averaging filter.
- **Observation:** It reduces noise while preserving edges.

### 3. Median Filter
- **Function:** `cv2.medianBlur(img, 5)`
- **Explanation:** Replaces each pixel with the median value of the surrounding pixels, good at removing salt-and-pepper noise.
- **Observation:** Good for noise removal.

### 4. Bilateral Filter
- **Function:** `cv2.bilateralFilter(img, 9, 50, 25)`
- **Explanation:** Considers both spatial distance and pixel intensity, making it good for edge-preserving smoothing.
- **Observation:** Smoothens the image while keeping edges sharp.

## Additional example
- **Larger Gaussian Kernel (15x15)**: Smoother image but with more significant loss of detail.

## Conclusion
Each filter has its own purpose: averaging smooths the image uniformly, Gaussian reduces noise while preserving edges, median removes salt-and-pepper noise, and bilateral smooths while keeping edges sharp. The additional example with a larger Gaussian kernel (15x15) shows smoother image but more loss of detal.

