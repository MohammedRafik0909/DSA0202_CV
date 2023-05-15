import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/mohammed rafik m/OneDrive/Documents/computer vision/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg", cv2.IMREAD_GRAYSCALE)

# Apply the Sobel operator
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Compute the magnitude of the gradient
gradient_magnitude = np.sqrt(np.square(sobel_x) + np.square(sobel_y))

# Threshold the gradient magnitude to obtain the boundary
threshold = 50  # Adjust the threshold as desired
boundary = np.uint8(gradient_magnitude > threshold) * 255

# Display the boundary image
cv2.imshow("Boundary Image", boundary)
cv2.waitKey(0)
cv2.destroyAllWindows()
