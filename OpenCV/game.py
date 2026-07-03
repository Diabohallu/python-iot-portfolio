import cv2
import numpy as np

HEIGHT = 700
WIDTH = 850

b1_x = 100
b1_y = 300
b1_radius = 15

b2_x = 700
b2_y = 300
b2_radius = 15

speed = 20

score = 0
target_x = 400
target_y = 150
target_radius = 10

obs_x = 350
obs_y = 200
obs_width = 100
obs_height = 200

paused = False
counter = 0
seconds = 0

while True:

    frame = np.zeros((HEIGHT, WIDTH, 3), dtype="uint8")
    
    if paused == False:
        counter = counter + 1
  
        if counter >= 33: 
            seconds = seconds + 1
            counter = 0

    cv2.putText(frame, "Score: " + str(score), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, "Speed: " + str(speed), (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, "Time: " + str(seconds) + "s", (650, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    if paused == True:
        cv2.putText(frame, "PAUSED", (350, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.rectangle(frame, (obs_x, obs_y), (obs_x + obs_width, obs_y + obs_height), (128, 128, 128), -1)

    cv2.circle(frame, (target_x, target_y), target_radius, (0, 255, 255), -1)

    cv2.circle(frame, (b1_x, b1_y), b1_radius, (255, 0, 0), -1)

    cv2.circle(frame, (b2_x, b2_y), b2_radius, (0, 0, 255), -1)

    cv2.imshow("Ball Game", frame)
    
    key = cv2.waitKey(30) & 0xFF
    
    if key == ord('q'):
        break

    if key == ord("w"):
        b1_y = b1_y - speed
    if key == ord("s"):
        b1_y = b1_y + speed
    if key == ord("a"):
        b1_x = b1_x - speed
    if key == ord("d"):
        b1_x = b1_x + speed

    if key == ord("u"):    
        b2_y = b2_y - speed
    if key == ord("j"):    
        b2_y = b2_y + speed
    if key == ord("h"):   
        b2_x = b2_x - speed
    if key == ord("l"):   
        b2_x = b2_x + speed

    if key == ord('+'):
        speed = speed + 1
    if key == ord('-'):
        if speed > 1:
            speed = speed - 1

    if b1_x < b1_radius: 
        b1_x = b1_radius
    if b1_x > WIDTH - b1_radius: 
        b1_x = WIDTH - b1_radius
    if b1_y < b1_radius: 
        b1_y = b1_radius
    if b1_y > HEIGHT - b1_radius: 
        b1_y = HEIGHT - b1_radius

    if b2_x < b2_radius: 
        b2_x = b2_radius
    if b2_x > WIDTH - b2_radius: 
        b2_x = WIDTH - b2_radius
    if b2_y < b2_radius: 
        b2_y = b2_radius
    if b2_y > HEIGHT - b2_radius: 
        b2_y = HEIGHT - b2_radius

    dist_b1_target = ((b1_x - target_x)**2 + (b1_y - target_y)**2)**0.5

    dist_b2_target = ((b2_x - target_x)**2 + (b2_y - target_y)**2)**0.5

    if dist_b1_target < (b1_radius + target_radius) or dist_b2_target < (b2_radius + target_radius):
        score = score + 1
        
        if score == 1:
            target_x, target_y = 200, 100
        elif score == 2:
            target_x, target_y = 600, 500
        elif score == 3:
            target_x, target_y = 150, 450
        elif score == 4:
            target_x, target_y = 650, 150
        else:
            target_x, target_y = 400, 100
            score = 0 

cv2.destroyAllWindows()