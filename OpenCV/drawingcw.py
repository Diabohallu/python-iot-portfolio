
import cv2
import numpy as np

red_screen = np.zeros((150, 300, 3), dtype = "uint8")
red_screen[:] = (0, 0, 255)

green_screen = np.zeros((150, 300, 3), dtype = "uint8")
green_screen[:] = (0, 255, 0)

image = np.zeros((500, 700, 3), dtype = "uint8")
cv2.circle(image, (130, 230), 100, (255, 0, 0), -1)
cv2.circle(image, (350, 230), 100, (0, 255, 0), -1)
cv2.circle(image, (570, 230), 100, (0, 0, 255), -1)

traffic = np.zeros((600, 350, 3), dtype = "uint8")
cv2.circle(traffic, (170, 100), 80, (0, 0, 255), -1)
cv2.circle(traffic, (170, 300), 80, (0, 255, 255), -1)
cv2.circle(traffic, (170, 500), 80, (0, 255, 0), -1)

flag = np.zeros((550, 700, 3), dtype = "uint8")
cv2.rectangle(flag, (50, 50), (650, 200), (10, 150, 255), -1)
cv2.rectangle(flag, (50, 200), (650, 350), (255, 255, 255), -1)
cv2.rectangle(flag, (50, 350), (650, 500), (0, 255, 0), -1)
cv2.circle(flag, (355, 275), 75, (255, 0, 0), 2)
cv2.line(flag, (355, 350), (355, 200), (255, 0, 0), 2)
cv2.line(flag, (280, 275), (430, 275), (255, 0, 0), 2)
cv2.line(flag, (300, 325), (410, 225), (255, 0, 0), 2)
cv2.line(flag, (300, 225), (410, 325), (255, 0, 0), 2)

name = np.zeros((200, 400, 3), dtype = "uint8")
cv2.putText(name, "Obaidullah Bin Ahmed", (20, 110), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)

cv2.imshow("Red Screen", red_screen)
cv2.imshow("Green Screen", green_screen)
cv2.imshow("Circles", image)
cv2.imshow("Traffic Lights", traffic)
cv2.imshow("Indian Flag", flag)
cv2.imshow("My Name", name)
cv2.waitKey(0)
cv2.destroyAllWindows()
