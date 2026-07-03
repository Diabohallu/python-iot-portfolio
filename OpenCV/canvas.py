import cv2
import numpy as np

image = np.ones((600, 600, 3), dtype="uint8") * 255

drawing = False  
color = (0, 0, 0)  
thickness = 3


def draw_with_mouse(event, x, y, flags, param):
    global drawing
    if event == cv2.EVENT_LBUTTONDOWN:  
        drawing = True 
        cv2.circle(image, (x, y), thickness, color, -1)  
    elif event == cv2.EVENT_MOUSEMOVE and drawing: 
        cv2.circle(image, (x, y), thickness, color, -1)  
    elif event == cv2.EVENT_LBUTTONUP:  
        drawing = False

cv2.namedWindow("Drawing")
cv2.setMouseCallback("Drawing", draw_with_mouse)

while True:
    cv2.imshow("Drawing", image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'): 
        image[:] = 255  
    elif key == ord('q'):  
        break

cv2.destroyAllWindows()