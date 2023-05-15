import cv2
import numpy as np

# Load the original image and the watermark image
original_image = cv2.imread("C:/Users/mohammed rafik m/OneDrive/Documents/computer vision/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg")
watermark_image = cv2.imread("C:/Users/mohammed rafik m/OneDrive/Documents/computer vision/watermark-styles.jpg", cv2.IMREAD_UNCHANGED)

# Resize the watermark image to an appropriate size
resized_watermark = cv2.resize(watermark_image, (100, 100))

# Choose the position to place the watermark on the original image
x_pos = original_image.shape[1] - resized_watermark.shape[1] - 10  # Adjust the position as desired
y_pos = original_image.shape[0] - resized_watermark.shape[0] - 10  # Adjust the position as desired

# Create a transparent overlay for the watermark
overlay = np.zeros_like(original_image)
overlay[y_pos:y_pos+resized_watermark.shape[0], x_pos:x_pos+resized_watermark.shape[1]] = resized_watermark

# Blend the watermark with the original image
alpha = 0.6  # Adjust the opacity as desired (0.0 - fully transparent, 1.0 - fully opaque)
watermarked_image = cv2.addWeighted(original_image, 1, overlay, alpha, 0)

# Display or save the watermarked image
cv2.imshow("Watermarked Image", watermarked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
