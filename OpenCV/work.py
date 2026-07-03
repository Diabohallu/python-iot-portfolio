import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands = 1)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)

    h, w, c = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:

            index_finger = hand.landmark[8]
            
            x = int(index_finger.x * w)
            y = int(index_finger.y * h)

            cv2.circle(frame, (x, y), 30, (255, 0, 0), -1)

        cv2.imshow("Circles", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()



