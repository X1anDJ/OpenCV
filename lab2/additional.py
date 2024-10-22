import cv2

# Load the original image
image = cv2.imread('flower.png')

# Convert to HSV color space
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Convert to LAB color space
image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Display the original and converted images
cv2.imshow('Original Image', image)
cv2.imshow('HSV Image', image_hsv)
cv2.imshow('LAB Image', image_lab)

# Save the converted images
cv2.imwrite('flower_hsv.png', image_hsv)
cv2.imwrite('flower_lab.png', image_lab)

# Wait for a key press to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
