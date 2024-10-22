import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in both color and grayscale
img_color = cv2.imread('mountain1.png')
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# Create a figure to display both histograms side by side
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Color Histogram
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    histr = cv2.calcHist([img_color], [i], None, [256], [0, 256])
    axes[0].plot(histr, color=col)
    
axes[0].set_title('Color Histogram')
axes[0].set_xlabel('Pixel Intensity')
axes[0].set_ylabel('Frequency')

# Grayscale Histogram
hist_gray = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
axes[1].plot(hist_gray, color='black')

axes[1].set_title('Grayscale Histogram')
axes[1].set_xlabel('Pixel Intensity')
axes[1].set_ylabel('Frequency')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()

# Wait for key press to close any open windows
cv2.waitKey(0)
cv2.destroyAllWindows()
