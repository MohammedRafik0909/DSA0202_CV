import cv2

img = cv2.imread("C:/Users/mohammed rafik m/OneDrive/Pictures\Saved Pictures/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg")
height, width = img.shape[:2]

scale_factor = 1.5
bigger_img = cv2.resize(img, (int(width * scale_factor), int(height * scale_factor)))

scale_factor = 0.5
smaller_img = cv2.resize(img, (int(width * scale_factor), int(height * scale_factor)))

cv2.imshow("Original Image", img)
cv2.imshow("Bigger Image", bigger_img)
cv2.imshow("Smaller Image", smaller_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
