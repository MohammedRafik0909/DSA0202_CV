#image rotation for 270
import cv2


path = r"C:/Users/mohammed rafik m/OneDrive/Pictures\Saved Pictures/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg"


src = cv2.imread(path)


window_name = 'Image'


image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)


cv2.imshow(window_name, image)
cv2.waitKey(0)
