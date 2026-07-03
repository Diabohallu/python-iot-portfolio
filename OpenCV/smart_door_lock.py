#smart door lock

import cv2
import time
from pyfirmata2 import Arduino


board = Arduino('COM3')   
time.sleep(2)

green_led = board.digital[6]
red_led = board.digital[7]
relay = board.digital[8]
buzzer = board.digital[9]

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0)
door_open = False

print("System started. Press ESC to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera error")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        if not door_open:
            relay.write(1)      
            green_led.write(1)
            red_led.write(0)
            buzzer.write(0)
            print("FACE DETECTED > DOOR OPEN")
            door_open = True

    else:
        if door_open:
            relay.write(0)       
            green_led.write(0)
            red_led.write(1)
            buzzer.write(1)
            print("NO FACE > DOOR CLOSED")
            door_open = False

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Face Controlled Lock System", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
relay.write(0)
green_led.write(0)
red_led.write(0)
buzzer.write(0)
board.exit()
print("System stopped.")