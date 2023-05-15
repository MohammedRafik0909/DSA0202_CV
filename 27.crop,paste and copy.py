#Copying and pasting image inside another image 
import cv2
import numpy as np

img = cv2.imread('C:/Users/mohammed rafik m/OneDrive/Documents/computer vision/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg')
logo = cv2.imread('C:/Users/mohammed rafik m/OneDrive/Documents/computer vision/watermark-styles.jpg')
logo_h, logo_w = logo.shape[:2]
x_offset = 50
y_offset = 100
roi = img[y_offset:y_offset+logo_h, x_offset:x_offset+logo_w]
if roi.shape != logo.shape:
    logo = cv2.resize(logo, roi.shape[:2][::-1])
logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(logo_gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
logo_fg = cv2.bitwise_and(logo, logo, mask=mask)
dst = cv2.add(img_bg, logo_fg)
img[y_offset:y_offset+logo_h, x_offset:x_offset+logo_w] = dst
cv2.imwrite('result_image.jpg', img)
