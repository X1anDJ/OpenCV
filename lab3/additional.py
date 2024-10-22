import cv2

# Load the image
img = cv2.imread('flower.png')

# Flip the image horizontally
flipped_horizontally = cv2.flip(img, 1)  

# Flip the image vertically
flipped_vertically = cv2.flip(img, 0)  

# Flip the image both horizontally and vertically
flipped_both = cv2.flip(img, -1)  

# Display the results
cv2.imshow('Flipped Horizontally', flipped_horizontally)
cv2.imshow('Flipped Vertically', flipped_vertically)
cv2.imshow('Flipped Both', flipped_both)

cv2.waitKey(0)
cv2.destroyAllWindows()
