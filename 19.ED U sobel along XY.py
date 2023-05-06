import cv2
import numpy as np

# Load the image
img = cv2.imread('C:/Users/mohammed rafik m/OneDrive/Documents/computer vision/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg', 0)

# Apply Sobel filter along the X-axis
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Apply Sobel filter along the Y-axis
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Compute the gradient magnitude
gradmag = np.sqrt(sobelx**2 + sobely**2)

# Display the results
cv2.imshow('Original Image', img)
cv2.imshow('Sobel Edge Detection (XY-axis)', gradmag)
cv2.waitKey(0)
cv2.destroyAllWindows()
