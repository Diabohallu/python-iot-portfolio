import cv2  
from pyfirmata2 import Arduino   
import time  
import mediapipe as mp  

board = Arduino('COM3')

led_pin = 2
board.digital[led_pin].mode = 1  

mp_hands = mp.solutions.hands 
hands = mp_hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0) 

while True:
    ret, frame = cap.read()  
    if not ret:
        break  

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  
    result = hands.process(rgb) 

    if result.multi_hand_landmarks: 
        board.digital[led_pin].write(1)  
    else:
        board.digital[led_pin].write(0)  

    cv2.imshow('Frame', frame) 
    
    if cv2.waitKey(1) & 0xFF == 27:  
        break

cap.release()  
cv2.destroyAllWindows()  
board.exit()
