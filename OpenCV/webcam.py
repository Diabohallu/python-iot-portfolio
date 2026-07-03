
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.putText(frame, "It's a me, ", (75, 60), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0, 0, 255), 2)
    cv2.putText(frame, "Obaid", (370, 62), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 0, 0), 2)
    cv2.rectangle(frame, (85, 70), (450, 450), (0, 255, 0), -3)
    cv2.circle(frame, (200, 250), 50, (0, 0, 0), -3)
    cv2.circle(frame, (330, 250), 50, (0, 0, 0), -3)
    cv2.line(frame, (250, 250), (290, 250), (0, 0, 0), 10)
    cv2.ellipse(frame, (220, 355), (40, 30), 0, 0, 180, (0, 0, 0), 6)
    cv2.ellipse(frame, (300, 355), (40, 30), 0, 0, 180, (0, 0, 0), 6)

    if not ret:
        break
    cv2.imshow("My Camera", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
