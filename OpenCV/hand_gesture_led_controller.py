#hand gesture led controller

import cv2
import mediapipe as mp
import time
from pyfirmata2 import Arduino, util  

board = Arduino('COM3')  

led_pins = [3, 4, 5, 6, 7]

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands
tipIds = [4, 8, 12, 16, 20]

video = cv2.VideoCapture(0)
time.sleep(2)

with mp_hand.Hands(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as hands:

    while True:
        ret, image = video.read()
        if not ret:
            continue

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_rgb.flags.writeable = False

        results = hands.process(image_rgb)

        image_rgb.flags.writeable = True
        image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

        lmList = []

        if results.multi_hand_landmarks:
            handLms = results.multi_hand_landmarks[0] 

            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy]) 

            mp_draw.draw_landmarks(
                image, handLms, mp_hand.HAND_CONNECTIONS)

        fingers = []

        if len(lmList) != 0:

            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

        total = fingers.count(1)

        for i, pin in enumerate(led_pins):
            if i < total:
                board.digital[pin].write(1)
            else:
                board.digital[pin].write(0)

        cv2.rectangle(image, (20, 300), (260, 440), (0, 255, 0), cv2.FILLED)
        cv2.putText(image, str(total), (45, 375),
                    cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)
        cv2.putText(image, "LED", (120, 375),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)

        cv2.imshow("Frame", image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video.release()   
cv2.destroyAllWindows()
board.exit()




