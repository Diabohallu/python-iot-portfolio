
import cv2
import mediapipe as mp
import math
import pyfirmata2
import numpy as np

my_port = 'COM3' 

try:
    board = pyfirmata2.Arduino(my_port)
    iter8 = pyfirmata2.util.Iterator(board)
    iter8.start()
    pin9 = board.get_pin('d:9:s')   
    arduino_connected = True
    print("Arduino connected successfully.")
except Exception as e:
    print("Arduino not connected!", e)
    arduino_connected = False
    pin9 = None

def move_servo(angle):
    if not arduino_connected or pin9 is None:
        return  
    try:
        angle = max(0, min(180, angle))   
        pin9.write(angle)
    except Exception as e:
        print("Servo write error:", e)


def drawline(img, pt1, pt2, color, thickness=1, style='dotted', gap=20):
    try:
        dist = math.dist(pt1, pt2)          
    except:
        return  

    if dist < 1:
        return

    pts = []
    for i in np.arange(0, dist, gap):
        r = i / dist
        x = int(pt1[0] * (1 - r) + pt2[0] * r)
        y = int(pt1[1] * (1 - r) + pt2[1] * r)
        pts.append((x, y))

    if style == 'dotted':
        for p in pts:
            cv2.circle(img, p, thickness, color, -1)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not detected!")
    exit()

with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as hands:

    while True:

        success, image = cap.read()
        if not success:
            print("Frame not received from camera.")
            continue

        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        h, w, c = image.shape

        cv2.rectangle(image, (700, 100), (1100, 200), (255, 0, 255), cv2.FILLED)
        cv2.putText(image, "Join index & middle fingers to exit",
                    (720, 165), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                lmList = []
                for id, lm in enumerate(hand_landmarks.landmark):
                    lmList.append([id, int(lm.x * w), int(lm.y * h)])

                if len(lmList) < 21:
                    continue

                if lmList[4][1] is None or lmList[8][1] is None:
                    continue

                thumb = (lmList[4][1], lmList[4][2])
                index = (lmList[8][1], lmList[8][2])

                drawline(image, thumb, index, (0, 0, 255), thickness=1, gap=10)

                try:
                    distance = math.hypot(index[0] - thumb[0], index[1] - thumb[1])
                except:
                    distance = 0

                distance = max(10, min(200, distance))

                angle = np.interp(distance, [10, 200], [0, 180])

                print(f"Distance: {distance:.2f}, Angle: {angle:.2f}")

                move_servo(angle)

                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Hand Servo Control", image)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

print("Program ended safely.")
