#movement

import cv2
import numpy as np

image = np.zeros((500, 700, 3), dtype="uint8")

x = 250
y = 250
s = 30

bx = 200
by = 250
radius = 20

while True:

    image[:] = 0

    cv2.rectangle(image, (x - s, y - s), (x + s, y + s), (255, 0, 0), -1)
    cv2.circle(image, (bx, by), radius, (0, 255, 255), -1)

    cv2.imshow("Keyboard", image)
    key = cv2.waitKey(30) & 0xFF

    if key == ord("q"):
        break

    if key == ord("a"):
        x = x - 20
    if key == ord("w"):
        y = y - 20
    if key == ord("s"):
        y = y + 20
    if key == ord("d"):
        x = x + 20
    
    if key == ord('u'):
        by = by - 20
    if key == ord('j'):
        by = by + 20
    if key == ord("k"):
        bx = bx + 20
    if key == ord("h"):
        bx = bx - 20
    
    if x < s:           
        x = s           
    if x > 700 - s:     
        x = 700 - s    
    if y < s:           
        y = s           
    if y > 500 - s: 
        y = 500 - s     

    if bx < radius:
        bx = radius
    if bx > 700 - radius:
        bx = 700 - radius
    if by < radius:
        by = radius
    if by > 500 - radius:
        by = 500 - radius

cv2.destroyAllWindows()



