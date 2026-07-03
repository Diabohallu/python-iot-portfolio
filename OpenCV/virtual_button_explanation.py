What this project does
Opens your webcam.
Detects your hand using MediaPipe.
Tracks your index finger tip.
Draws 3 virtual buttons on the screen.
When your finger touches a button:
The button changes state (ON/OFF).
The corresponding LED on Arduino turns ON/OFF.
Libraries Used
Python
import cv2
OpenCV → Used for webcam, drawing buttons, and displaying video.
Python
import mediapipe as mp
MediaPipe → Used for hand detection and finger tracking.
Python
from pyfirmata import Arduino
PyFirmata → Lets Python communicate with Arduino.
Python
import time
Used for timing and debounce.
Arduino Setup
Python
board = Arduino('COM6')
Connects Python to Arduino.
Example:
Python
COM3
COM4
COM6
The port depends on your computer.
Python
led_pins = [2, 3, 4]
LED connections:
LED
Arduino Pin
LED 1
2
LED 2
3
LED 3
4
MediaPipe Hand Setup
Python
mp_hands = mp.solutions.hands
Loads MediaPipe Hands module.
Python
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
Settings:
Detect only 1 hand
70% confidence required
Webcam Setup
Python
cap = cv2.VideoCapture(0)
Opens webcam.
0 = default camera.
Finger Tip Landmark
Python
INDEX_FINGER_TIP = 8
MediaPipe gives 21 landmarks.
Example:
Plain text
0  = Wrist
4  = Thumb Tip
8  = Index Tip
12 = Middle Tip
16 = Ring Tip
20 = Pinky Tip
We track landmark 8.
Virtual Buttons
Python
buttons = [
 ...
]
Creates 3 buttons.
Example:
Python
{
 "label":"Switch 1",
 "x":50,
 "y":50,
 "w":150,
 "h":60
}
Meaning:
Plain text
(50,50)
+------------------+
|    Switch 1      |
+------------------+

Width  = 150
Height = 60
Debounce
Python
TOUCH_DELAY = 0.5
Without this:
Plain text
Finger touches button
↓
ON
OFF
ON
OFF
ON
OFF
Very fast blinking.
Debounce means:
Plain text
Touch
↓
Wait 0.5 sec
↓
Allow next touch
Draw Button Function
Python
def draw_button(frame, button):
Draws each button.
Button Color
Python
color = (0,255,0)
Green = ON
Python
color = (0,0,255)
Red = OFF
Draw Rectangle
Python
cv2.rectangle(...)
Creates button shape.
Plain text
+-------------+
|  Switch 1   |
+-------------+
Put Text
Python
cv2.putText(...)
Writes:
Plain text
Switch 1
Switch 2
Switch 3
on buttons.
Main Loop
Python
while True:
Runs forever until ESC key is pressed.
Capture Frame
Python
ret, frame = cap.read()
Reads image from webcam.
Mirror Effect
Python
frame = cv2.flip(frame,1)
Without flip:
Plain text
Move Right
→ appears Left
With flip:
Plain text
Move Right
→ appears Right
Like a mirror.
Convert BGR to RGB
Python
rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
MediaPipe needs RGB images.
Detect Hand
Python
result = hands.process(rgb)
Finds hand landmarks.
Draw Hand Skeleton
Python
mp_drawing.draw_landmarks(...)
Draws:
Plain text
o---o---o
 \ /
  o
hand connections.
Get Finger Position
Python
index_tip = hand_landmarks.landmark[8]
Gets index finger tip.
Python
finger_x = int(index_tip.x * w)
finger_y = int(index_tip.y * h)
Converts normalized coordinates:
Plain text
0.0 → 1.0
to screen pixels.
Example:
Plain text
0.5 × 640 = 320
Button Touch Detection
Python
if button["x"] <= finger_x <= button["x"] + button["w"]
Checks if finger is inside button.
Example:
Plain text
Button:
x=50
width=150

Range:
50 → 200
If finger x=120:
Plain text
50 <= 120 <= 200
TRUE
Toggle Switch
Python
button["state"] = not button["state"]
Magic line!
If:
Python
True
becomes
Python
False
and vice versa.
Example:
Plain text
OFF → ON
ON → OFF