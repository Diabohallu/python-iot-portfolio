
import cv2
import numpy as np

image = np.zeros((500, 500, 3), dtype = "uint8")
def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x,y), 40, (0, 0, 255), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(image, (x-40, y-20), (x+40, y+20), (0, 255, 0), -1)
cv2.namedWindow("Canvas")
cv2.setMouseCallback("Canvas", mouse_click)

while True:
    cv2.imshow("Canvas", image)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
