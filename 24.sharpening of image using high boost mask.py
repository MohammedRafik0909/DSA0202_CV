import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/mohammed rafik m/OneDrive/Documents/computer vision/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define the high-boost kernel
kernel = np.array([[-1,-1,-1],
                   [-1, 9,-1],
                   [-1,-1,-1]])

# Apply the high-boost kernel to the grayscale image
sharpened = cv2.filter2D(gray, -1, kernel)

# Display the original and sharpened images
cv2.imshow("Original", img)
cv2.imshow("Sharpened", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
