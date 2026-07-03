#Virtual button

import cv2
import mediapipe as mp
from pyfirmata2 import Arduino
import time

board = Arduino('COM3') 
led_pins = [8, 9, 10]     

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

cap = cv2.VideoCapture(0)

INDEX_FINGER_TIP = 8

buttons = [
    {"label": "Switch 1", "x": 50, "y": 50, "w": 150, "h": 60, "state": False, "last_toggle": 0},
    {"label": "Switch 2", "x": 50, "y": 130, "w": 150, "h": 60, "state": False, "last_toggle": 0},
    {"label": "Switch 3", "x": 50, "y": 210, "w": 150, "h": 60, "state": False, "last_toggle": 0},
]

TOUCH_DELAY = 0.5 

def draw_button(frame, button):
    color = (0, 255, 0) if button["state"] else (0, 0, 255)
    cv2.rectangle(frame, (button["x"], button["y"]), (button["x"] + button["w"], button["y"] + button["h"]), color, -1)
    cv2.rectangle(frame, (button["x"], button["y"]), (button["x"] + button["w"], button["y"] + button["h"]), (255, 255, 255), 2)
    cv2.putText(frame, button["label"], (button["x"] + 10, button["y"] + button["h"] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    finger_x, finger_y = None, None

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            h, w, _ = frame.shape
            index_tip = hand_landmarks.landmark[INDEX_FINGER_TIP]
            finger_x, finger_y = int(index_tip.x * w), int(index_tip.y * h)

    if finger_x is not None and finger_y is not None:
        for button in buttons:

            if button["x"] <= finger_x <= button["x"] + button["w"] and button["y"] <= finger_y <= button["y"] + button["h"]:
                if time.time() - button["last_toggle"] > TOUCH_DELAY:
                    button["state"] = not button["state"]
                    button["last_toggle"] = time.time()

    for i, button in enumerate(buttons):
        board.digital[led_pins[i]].write(1 if button["state"] else 0)

    for button in buttons:
        draw_button(frame, button)

    if finger_x is not None and finger_y is not None:
        cv2.circle(frame, (finger_x, finger_y), 10, (255, 255, 0), -1)

    cv2.imshow("Touch Virtual Switches", frame)
    key = cv2.waitKey(30) & 0xFF
    if key == ord('q'):
        break
       

cap.release()
cv2.destroyAllWindows()
board.exit()