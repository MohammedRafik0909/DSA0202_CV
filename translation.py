import cv2
import numpy as np

image = cv2.imread('C:/Users/mohammed rafik m/OneDrive/Pictures\Saved Pictures/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg')
height, width = image.shape[:2]

quarter_height, quarter_width = height / 4, width / 4

T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])
img_translation = cv2.warpAffine(image, T, (width, height))

cv2.imshow("Originalimage", image)
cv2.imshow('Translation', img_translation)
cv2.waitKey()

cv2.destroyAllWindows()

