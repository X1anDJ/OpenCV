import cv2
#read image
image = cv2.imread('flower.png')
image_gray = cv2.imread('flower.png', cv2.IMREAD_GRAYSCALE)
#show image
cv2.imshow('flower', image)
#show grayscale image
cv2.imshow('flower_gray', image_gray)


#wait for any keys to close windows
cv2.imwrite('flower_gray.png', image_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()