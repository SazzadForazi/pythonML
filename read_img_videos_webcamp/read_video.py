import cv2

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture("D:\\youtube video footage\\output.mp4")
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
