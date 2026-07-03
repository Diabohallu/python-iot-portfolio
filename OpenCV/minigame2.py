import cv2 
import numpy as np

image = np.zeros((600, 600, 3), dtype="uint8")

ball_x = 300
ball_y = 50
ball_radius = 20
ball_speed = 7

paddle_x = 270
paddle_width = 60
paddle_height = 10

score = 0

while True:
    
    image[:] = 0

    cv2.circle(image, (ball_x, ball_y), ball_radius, (0, 255, 255), -1)
    cv2.rectangle(image, (paddle_x, 550), (paddle_x + paddle_width, 550 + paddle_height), (255, 0, 0), -1)
    cv2.putText(image, f"Score: {score}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    ball_y += ball_speed

    key = cv2.waitKey(30) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('a'): 
        paddle_x -= 50
    elif key == ord('d'): 
        paddle_x += 50

    if paddle_x < 0:
        paddle_x = 0
    if paddle_x > 540:
        paddle_x = 540

    if (ball_y + ball_radius >= 550) and (ball_y - ball_radius <= 560) and (paddle_x <= ball_x <= paddle_x + paddle_width):
        cv2.putText(image, "Game Over!", (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        cv2.imshow("Catch the Ball", image)
        cv2.waitKey(2000)
        break

    if ball_y > 600:
        score += 1
        ball_y = 50  
        ball_x = np.random.randint(50, 550)  

    cv2.imshow("Catch the Ball", image)

cv2.destroyAllWindows()