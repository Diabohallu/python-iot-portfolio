
import cv2

image = cv2.imread("C:/Users/obaid/Downloads/wallhaven-k81776.jpg")
image_resized = cv2.resize(image, (900, 500))
gray = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)
cv2.rectangle(image_resized, (471, 345), (500, 390), (255, 255, 100), 2)
cv2.imshow("Image", image_resized)
cv2.imshow("Gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows
