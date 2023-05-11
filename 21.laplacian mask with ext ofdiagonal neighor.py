import cv2
import numpy as np

# Read the input image
img = cv2.imread('C:/Users/mohammed rafik m/OneDrive/Documents/computer vision/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Laplacian filter with diagonal extension
kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
laplacian = cv2.filter2D(gray, -1, kernel)

# Add the Laplacian image to the original image to sharpen it
sharpened = cv2.add(gray, laplacian)

# Display the original and sharpened images
cv2.imshow('Original Image', gray)
cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
