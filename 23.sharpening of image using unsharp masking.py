import cv2
import numpy as np

# Load the image
img = cv2.imread('C:/Users/mohammed rafik m/OneDrive/Documents/computer vision/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the image
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Calculate the unsharp mask
unsharp_mask = cv2.addWeighted(gray, 1.5, blur, -0.5, 0)

# Display the original and sharpened images
cv2.imshow('Original Image', gray)
cv2.imshow('Sharpened Image', unsharp_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
