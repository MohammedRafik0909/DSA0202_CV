import cv2

# Load the image
image = cv2.imread('C:/Users/mohammed rafik m/OneDrive/Documents/computer vision/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg')

# Display the image
cv2.imshow('Image', image)

# Wait for key press
cv2.waitKey(0)

# Close the image window
cv2.destroyAllWindows()

# Select the region of interest (ROI) using mouse events
roi = cv2.selectROI(image)

# Extract the object from the image using the ROI
object = image[int(roi[1]):int(roi[1] + roi[3]), int(roi[0]):int(roi[0] + roi[2])]

# Display the extracted object
cv2.imshow('Object', object)
cv2.waitKey(0)
cv2.destroyAllWindows()
