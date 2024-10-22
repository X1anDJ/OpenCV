import cv2
import numpy as np
import matplotlib.pyplot as plt

#load image
img = cv2.imread('mountain1.png')
colors = ('b', 'g', 'r')

# loop through each channel
for i, col in enumerate(colors):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color = col)
    
plt.title('Color Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()

#wait for any keys to close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
