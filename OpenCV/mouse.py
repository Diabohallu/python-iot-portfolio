import cv2
import numpy as np

click = []

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        click.append((x, y))
        print(f"Circle drawn at: x={x}, y={y}")

def smiley():
    image = np.zeros((500, 500, 3), dtype="uint8")
    cv2.circle(image, (250, 250), 200, (0, 215, 255), -1)
    cv2.circle(image, (250, 250), 200, (0, 0, 0), 4)
    cv2.circle(image, (175, 200), 15, (0, 0, 0), -1)
    cv2.circle(image, (325, 200), 15, (0, 0, 0), -1)
    cv2.ellipse(image, (250, 280), (100, 70), 0, 20, 160, (0, 0, 0), 5)
    return image

def house():
    image = np.zeros((600, 700, 3), dtype="uint8")
    image[:] = (0, 0, 0)

    cv2.circle(image, (600, 80), 60, (255, 255, 255), -1)
    cv2.circle(image, (600, 80), 60, (255, 255, 225), 3)

    cv2.rectangle(image, (150, 300), (550, 520), (60, 80, 180), -1)
    cv2.rectangle(image, (150, 300), (550, 520), (20, 20, 100), 3)

    cv2.rectangle(image, (310, 400), (390, 520), (30, 100, 139), -1)
    cv2.rectangle(image, (310, 400), (390, 520), (0, 60, 90), 2)

    cv2.rectangle(image, (185, 340), (270, 410), (210, 230, 140), -1)
    cv2.rectangle(image, (185, 340), (270, 410), (20, 20, 100), 2)

    cv2.rectangle(image, (430, 340), (515, 410), (210, 230, 140), -1)
    cv2.rectangle(image, (430, 340), (515, 410), (20, 20, 100), 2) 

    points = np.array([[150, 300], [350, 130], [550, 300]])
    cv2.fillPoly(image, [points], (30, 100, 139))
    cv2.polylines(image, [points], True, (0, 60, 90), 3)

    cv2.rectangle(image, (0, 520), (700, 600), (50, 150, 60), -1)

    return image  

webcam = cv2.VideoCapture(0)

cv2.namedWindow("Circles")
cv2.setMouseCallback("Circles", mouse_click)
cv2.namedWindow("Smiley Face")
cv2.namedWindow("House")

smiley_image = smiley()
house_image = house()         

print("Webcam opened!")
print("Click anywhere on the video to draw a circle.")
print("Press Q to quit and save your drawing.")

while True:
    ret, frame = webcam.read()
    if not ret:
        break

    for point in click:
        x, y = point
        cv2.circle(frame, (x, y), 30, (0, 0, 255), 3)

    cv2.putText(frame, "Click to draw circles", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    cv2.imshow("Circles", frame)
    cv2.imshow("Smiley Face", smiley_image) 
    cv2.imshow("House", house_image)         

    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.imwrite("circles.png", frame)
        break

webcam.release()
cv2.destroyAllWindows()



