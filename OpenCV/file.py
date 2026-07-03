import cv2
import mediapipe as mp
from pyfirmata2 import Arduino
import time
from collections import deque
import numpy as np

# Arduino setup
board = Arduino('COM3')
time.sleep(2)
led_pin = 2
board.digital[led_pin].mode = 1

# Mediapipe setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)

SMOOTH_FRAMES = 2
landmark_history = deque(maxlen=SMOOTH_FRAMES)

cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            board.digital[led_pin].write(1)

            for hand_landmarks in result.multi_hand_landmarks:
                current = [(lm.x, lm.y, lm.z) for lm in hand_landmarks.landmark]
                landmark_history.append(current)

                # Only smooth if we have enough frames
                if len(landmark_history) == SMOOTH_FRAMES:
                    weights = np.array([0.2, 0.8])
                    smoothed = np.average(landmark_history, axis=0, weights=weights)
                else:
                    smoothed = np.array(current)

                h, w, _ = frame.shape
                for connection in mp_hands.HAND_CONNECTIONS:
                    start_idx, end_idx = connection
                    x1, y1 = int(smoothed[start_idx][0] * w), int(smoothed[start_idx][1] * h)
                    x2, y2 = int(smoothed[end_idx][0] * w), int(smoothed[end_idx][1] * h)
                    cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                for x, y, z in smoothed:
                    cx, cy = int(x * w), int(y * h)
                    cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
        else:
            board.digital[led_pin].write(0)

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
    board.digital[led_pin].write(0)
    board.exit()