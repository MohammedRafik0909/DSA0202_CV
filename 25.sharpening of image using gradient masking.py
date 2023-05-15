import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/mohammed rafik m/OneDrive/Documents/computer vision/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg")

# Define the kernels
kernel1 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
kernel2 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the convolution operation
gradient1 = cv2.filter2D(gray, -1, kernel1)
gradient2 = cv2.filter2D(gray, -1, kernel2)

# Combine the gradients to create the sharpened image
sharpened = cv2.addWeighted(gradient1, 1, gradient2, 1, 0)

# Display the original and sharpened images
cv2.imshow("Original Image", image)
cv2.imshow("Sharpened Image", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
