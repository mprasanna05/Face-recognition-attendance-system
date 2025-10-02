import cv2

url = 'http://157.46.83.44:8080/video'
cap = cv2.VideoCapture(url)

while True:
    rtn, frame = cap.read()
    if not rtn:
        break
    cv2.imshow('Mobile Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
