import cv2
import numpy as np

#1. Garden
garden = np.zeros((600, 800, 3), dtype="uint8")
garden[:] = (200, 50, 0)
cv2.rectangle(garden, (0, 450), (800, 600), (34, 139, 34), -1)

cv2.circle(garden, (680, 80), 60, (0, 220, 255), -1)
cv2.rectangle(garden, (130, 300), (170, 450), (19, 69, 139), -1)

cv2.circle(garden, (150, 230), 90, (0, 140, 0), -1)

cv2.circle(garden, (318, 370), 16, (147, 20, 255), -1)  
cv2.circle(garden, (382, 370), 16, (147, 20, 255), -1)  
cv2.circle(garden, (350, 338), 16, (147, 20, 255), -1)   
cv2.circle(garden, (350, 370), 20, (255, 255, 255), -1)  
cv2.line(garden,   (350, 390), (350, 450), (0, 180, 0), 3)  
cv2.circle(garden, (350, 402), 16, (147, 20, 255), -1)
cv2.circle(garden, (350, 370), 20, (255, 255, 255), -1) 

cv2.circle(garden, (468, 380), 16, (255, 105, 180), -1)  
cv2.circle(garden, (532, 380), 16, (255, 105, 180), -1)  
cv2.circle(garden, (500, 348), 16, (255, 105, 180), -1)  
cv2.circle(garden, (500, 380), 20, (0, 220, 255), -1)    
cv2.line(garden,   (500, 400), (500, 450), (0, 180, 0), 3) 
cv2.circle(garden, (500, 412), 16, (255, 105, 180), -1)
cv2.circle(garden, (500, 380), 20, (0, 220, 255), -1) 

#2. Robot
robot = np.zeros((600, 500, 3), dtype="uint8")
robot[:] = (30, 30, 30)
 
cv2.rectangle(robot, (150, 60), (350, 200), (180, 180, 0), -1)
 
cv2.circle(robot, (205, 120), 25, (0, 0, 255), -1)
cv2.circle(robot, (295, 120), 25, (0, 0, 255), -1)   
cv2.circle(robot, (205, 120), 10, (255, 255, 255), -1)
cv2.circle(robot, (295, 120), 10, (255, 255, 255), -1)
 
cv2.rectangle(robot, (185, 165), (315, 185), (0, 200, 255), -1)
 
cv2.line(robot, (250, 60), (250, 20), (200, 200, 200), 4)
cv2.circle(robot, (250, 15), 10, (0, 0, 255), -1)
 
cv2.rectangle(robot, (215, 200), (285, 210), (150, 150, 0), -1)
 
cv2.rectangle(robot, (120, 210), (380, 400), (0, 128, 255), -1)
 
cv2.rectangle(robot, (175, 240), (325, 370), (0, 60, 180), -1)
cv2.circle(robot, (210, 280), 20, (0, 255, 255), -1)
cv2.circle(robot, (290, 280), 20, (0, 255, 0), -1)
cv2.rectangle(robot, (195, 320), (305, 355), (255, 100, 0), -1)
 
cv2.rectangle(robot, (70, 210), (120, 370), (100, 200, 50), -1)
cv2.rectangle(robot, (380, 210), (432, 370), (100, 200, 50), -1)
 
cv2.circle(robot, (95, 385), 25, (50, 150, 50), -1)
cv2.circle(robot, (405, 385), 25, (50, 150, 50), -1)
 
cv2.rectangle(robot, (150, 400), (230, 530), (200, 80, 0), -1)
cv2.rectangle(robot, (270, 400), (350, 530), (200, 80, 0), -1)
 
cv2.rectangle(robot, (130, 525), (240, 560), (150, 60, 0), -1)  
cv2.rectangle(robot, (260, 525), (370, 560), (150, 60, 0), -1) 

#3. Text
text= np.zeros((200, 710, 3), dtype="uint8")

cv2.putText(text, "I", (1,  120), cv2.FONT_HERSHEY_DUPLEX, 2.5, (0, 255, 255), 2)
cv2.putText(text, "Love", (220,  120), cv2.FONT_HERSHEY_DUPLEX, 2.5, (147, 20, 255), 2)
cv2.putText(text, "OpenCV", (400, 120), cv2.FONT_HERSHEY_DUPLEX, 2.5, (0, 200, 100), 2)


cv2.imshow("Garden", garden)
cv2.imshow("Robot", robot)
cv2.imshow("Text", text)
cv2.waitKey(0)
cv2.destroyAllWindows()
