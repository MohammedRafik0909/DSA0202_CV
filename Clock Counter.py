import cv2
img = cv2.imread("C:/Users/mohammed rafik m/OneDrive/Pictures\Saved Pictures/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg")
height, width = img.shape[:2]

angle = 30
center = (width/2, height/2)
M = cv2.getRotationMatrix2D(center, angle, 1)
clockwise_img = cv2.warpAffine(img, M, (width, height))
M = cv2.getRotationMatrix2D(center, -angle, 1)
counter_clockwise_img = cv2.warpAffine(img, M, (width, height))
cv2.imshow("Original Image", img)
cv2.imshow("Clockwise Rotated Image", clockwise_img)
cv2.imshow("Counter-Clockwise Rotated Image", counter_clockwise_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
