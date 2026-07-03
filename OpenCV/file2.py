import cv2  # This is the OpenCV library for image and video processing.
from pyfirmata2 import Arduino   # PyFirmata lets us talk to the Arduino board from Python.
import time  # We will use time to create short delays between actions.
import mediapipe as mp  # Mediapipe is for detecting hands and gestures in videos.

# Step 1: Connect to the Arduino board
board = Arduino('COM3')  # 'COM3' is the computer port—this depends on your Arduino connection. You will need to adjust it if you use another port.


# Step 2: Set up the LED pin
led_pin = 2  # We will connect an LED to pin 2 on the Arduino.
board.digital[led_pin].mode = 1  # Set the pin as an output so we can turn the LED on or off.

# Step 3: Set up the Mediapipe hand tracker
mp_hands = mp.solutions.hands  # We load the hand tracking solution from Mediapipe.
hands = mp_hands.Hands(max_num_hands=1)  # We tell it to detect up to one hand with a decent confidence level.

# Step 4: Capture video from the webcam
cap = cv2.VideoCapture(0)  # 0 means use the first webcam on your computer.

# Step 5: Main loop to process each video frame
while True:
    ret, frame = cap.read()  # Capture a single frame from the webcam.
    if not ret:
        break  # If no frame is captured, exit the loop.

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert the frame to RGB (Mediapipe prefers RGB format).
    result = hands.process(rgb)  # Use Mediapipe to detect hand landmarks.

    if result.multi_hand_landmarks:  # If we see a hand in the frame
        board.digital[led_pin].write(1)  # Turn on the LED
    else:
        board.digital[led_pin].write(0)  # No hand detected, turn off the LED

    cv2.imshow('Frame', frame)  # Show the webcam video on the screen.
    
    if cv2.waitKey(1) & 0xFF == 27:  # If we press ESC key, exit the loop
        break

# Step 6: Cleanup
cap.release()  # Stop using the webcam.
cv2.destroyAllWindows()  # Close the window showing the video.
board.exit()  # Stop communication with the Arduino.