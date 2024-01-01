import cv2
capture = cv2.VideoCapture(0)
from identify import detect_object_with_custom_height_width
if not capture.isOpened():
    print("Error: Camera is not open")
    exit()

while True:
    read, frame = capture.read()
    if read:
        cv2.imshow('Camera', frame)
        finger_detected = detect_object_with_custom_height_width(frame)
        cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()

cv2.destroyAllWindows()
