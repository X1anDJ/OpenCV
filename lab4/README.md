# Lab 4

This project shows different methods for feature detection and matching, including SIFT, Harris Corner Detection, and ORB.

## Environment
Use your OpenCV virtual environment.

## Explanation and Observation

### 1. SIFT Feature Detection and FLANN Matching
- **Function:** Uses `cv2.SIFT_create()` to detect and compute keypoints and descriptors.
- **Explanation:** Matches features between two images using FLANN-based matcher and a ratio test to filter good matches.
- **Observation:** SIFT detects distinctive features but can be slow on large images.

### 2. Harris Corner Detection
- **Function:** Uses `cv2.cornerHarris()` to detect corners.
- **Explanation:** Identifies corners by dilating the response and marking them in red.
- **Observation:** Good at finding corners but may struggle with curved shapes.

### 3. Extra Example: ORB Feature Detection and FLANN Matching
- **Function:** Uses `cv2.ORB_create()` to detect and compute features, and matches them with a FLANN-based matcher.
- **Explanation:** ORB offers a faster alternative to SIFT with good performance for real-time applications.
- **Observation:** ORB is faster but may not be as accurate as SIFT.

## Additional Example:
- **ORB Feature Matching:** Demonstrates how ORB can replace SIFT for lightweight, real-time applications with acceptable accuracy.

## Conclusion
Feature detection and matching help identify similarities between images. SIFT provides detailed matching but can be slow, Harris is best for detecting strong corners, and ORB offers a fast alternative with reasonable accuracy. The **extra example with ORB** highlights the trade-off between speed and precision.
