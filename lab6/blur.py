import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('mountain1.png')

# Apply averaging box filter
blurred_avg = cv2.blur(img, (5, 5))

# Apply Gaussian filter with a small kernel
blurred_gaussian = cv2.GaussianBlur(img, (5, 5), 0)


# _______________Additional example_______________

# Apply Gaussian filter with a larger kernel
blurred_gaussian_large = cv2.GaussianBlur(img, (15, 15), 0)

# Apply median filter
blurred_med = cv2.medianBlur(img, 5)

# Apply bilateral filter
blurred_bi = cv2.bilateralFilter(img, 9, 50, 25)

# Display the images
plt.figure(figsize=(10, 8))

plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(cv2.cvtColor(blurred_avg, cv2.COLOR_BGR2RGB))
plt.title('Averaging Filter')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(cv2.cvtColor(blurred_gaussian, cv2.COLOR_BGR2RGB))
plt.title('Gaussian Filter (5x5)')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(cv2.cvtColor(blurred_gaussian_large, cv2.COLOR_BGR2RGB))
plt.title('Gaussian Filter (15x15)')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(cv2.cvtColor(blurred_med, cv2.COLOR_BGR2RGB))
plt.title('Median Filter')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(cv2.cvtColor(blurred_bi, cv2.COLOR_BGR2RGB))
plt.title('Bilateral Filter')
plt.axis('off')

plt.tight_layout()
plt.show()

cv2.waitKey(0)
