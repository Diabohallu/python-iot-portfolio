#ball

import cv2
import numpy as np

image = np.zeros((500, 700, 3), dtype="uint8")
b_ball = np.zeros((500, 700, 3), dtype="uint8")
s_ball = np.zeros((500, 700, 3), dtype="uint8")

x = 50
d = 50  
c = 1
color = (0, 0, 255)
g_radius= 20
s_radius = 100

while True:
  
    image[:] = 0
    b_ball[:] = 0
    s_ball[:] = 0
    
    cv2.circle(image, (x, 250), 50, color, -1)
    c = c+ 1

    if c == 1: 
        color = (0, 0, 255)     
    elif c == 2: 
        color = (0, 255, 0)     
    elif c == 3: 
        color = (255, 0, 0)      
    elif c == 4: 
        color = (0, 255, 255)   
    elif c == 5: 
        color = (255, 255, 0)  
    elif c == 6:
        coloe = (255, 0, 255)
        c = 0

    cv2.circle(b_ball, (x, 250), g_radius, (0, 255, 0), -1)
    g_radius = g_radius + 10
    
    cv2.circle(s_ball, (x, 250), s_radius, (255, 255, 0), -1)
    s_radius = s_radius - 10

    if s_radius < 5:
        s_radius = 5

    x = x + d

    if x >= 650 or x <= 50:
        d *= -1  
        g_radius = 20
        s_radius = 100
        
    cv2.imshow("Bonus 1: Rainbow Ball", image)
    cv2.imshow("Bonus 2: Bigger Ball", b_ball)
    cv2.imshow("Bonus 3: Shrinking Ball", s_ball)
    
    key = cv2.waitKey(100) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
