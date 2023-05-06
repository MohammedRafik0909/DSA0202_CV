import cv2
img = cv2.imread("C:/Users/mohammed rafik m/OneDrive/Pictures\Saved Pictures/WhatsApp Image 2022-03-18 at 6.54.12 AM.jpeg")
x, y = 100, 100
dx, dy = 50, 50
def move_image():
    global x, y, dx, dy
    x += dx
    y += dy
    if x < 0 or x > img.shape[1] or y < 0 or y > img.shape[0]:
        dx = -dx
        dy = -dy
def draw_image():
    global x, y
    cv2.imshow("Moving Image", img)
    cv2.moveWindow("Moving Image", x, y)
draw_image()
while True:
    move_image()
    draw_image()
    key = cv2.waitKey(50)
    if key != -1:
        break
cv2.destroyAllWindows()
