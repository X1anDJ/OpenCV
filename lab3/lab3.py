import cv2

img = cv2.imread('flower.png')

# Resize the image
resized_img = cv2.resize(img, (300, 300))

# Crop the image
cropped_img = img[100:300, 100:300]

# Rotate the image
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Label the image
labeled_img = cv2.putText(img, 'flower', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

# Display the images
cv2.imshow('resized', resized_img)
cv2.imshow('cropped', cropped_img)
cv2.imshow('rotated', rotated_img)
cv2.imshow('labeled', labeled_img)

cv2.waitKey(0)



cv2.destroyAllWindows()