import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/mohammed rafik m/OneDrive/Documents/computer vision/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg", cv2.IMREAD_GRAYSCALE)

# Define the kernel for dilation
kernel_size = (3, 3)  # Adjust the kernel size as desired
kernel = np.ones(kernel_size, dtype=np.uint8)

# Perform dilation
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Display the original and dilated images
cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
