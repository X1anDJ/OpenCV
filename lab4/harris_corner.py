import cv2
import numpy as np

#Part I: loading images

image = cv2.imread('flower.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Harris corner detection
gray = np.float32(gray)
harris_corners = cv2.cornerHarris(gray, 3, 3, 0.04)

# Dialate thedetected corners to enhance them
harris_corners = cv2.dilate(harris_corners, None) 

#Threshold for optimal value
image[harris_corners > 0.01 * harris_corners.max()] = [0, 0, 255]

# Display the image with the corners
cv2.imshow('Harris Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()