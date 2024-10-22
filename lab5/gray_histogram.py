import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('mountain1.png', 0)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

#plot histogram
plt.plot(hist)
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()

#wait for any keys to close windows
cv2.waitKey(0)
cv2.destroyAllWindows()