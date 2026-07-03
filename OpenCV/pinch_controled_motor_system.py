#Pinch Controlled Motor System

import cv2
import mediapipe as mp
import math
from pyfirmata2 import Arduino, util
import time

board = Arduino('COM3') 
greenLED = board.get_pin('d:3:o')
redLED = board.get_pin('d:4:o')
buzzer = board.get_pin('d:5:o')

motorIN1 = board.get_pin('d:6:o')  
motorIN2 = board.get_pin('d:7:o') 

it = util.Iterator(board)
it.start()
time.sleep(1)

def motor_on():
    motorIN1.write(1)
    motorIN2.write(0)
    greenLED.write(1)
    redLED.write(0)
    buzzer.write(0)

def motor_off():
    motorIN1.write(0)
    motorIN2.write(0)
    greenLED.write(0)
    redLED.write(1)
    buzzer.write(1)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)

DIST_THRESHOLD = 0.05  

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    motor_state = "UNKNOWN"

    if result.multi_hand_landmarks:
        handLms = result.multi_hand_landmarks[0]

        x1 = handLms.landmark[4].x
        y1 = handLms.landmark[4].y

        x2 = handLms.landmark[8].x
        y2 = handLms.landmark[8].y

        distance = math.hypot(x2 - x1, y2 - y1)

        p1 = (int(x1 * w), int(y1 * h))
        p2 = (int(x2 * w), int(y2 * h))

        cv2.circle(frame, p1, 10, (0, 255, 0), -1)
        cv2.circle(frame, p2, 10, (0, 255, 0), -1)
        cv2.line(frame, p1, p2, (255, 0, 0), 2)

        if distance > DIST_THRESHOLD:
            motor_on()
            motor_state = "MOTOR RUNNING"
            color = (0, 255, 0)
        else:
            motor_off()
            motor_state = "MOTOR OFF"
            color = (0, 0, 255)

        cv2.putText(frame, motor_state, (30, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

        mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

    else:

        motor_off()
        cv2.putText(frame, "NO HAND DETECTED", (30, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    cv2.imshow("Finger Distance Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

motor_off()
cap.release()
cv2.destroyAllWindows()