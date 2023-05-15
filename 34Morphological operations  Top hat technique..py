import cv2
import numpy as np

# Load the image
image = cv2.imread('C:/Users/mohammed rafik m/OneDrive/Documents/computer vision/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg', 0)  # Read the image as grayscale

# Create a kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Perform top hat operation
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

# Display the original and top hat images
cv2.imshow('Original', image)
cv2.imshow('Top Hat', tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()
