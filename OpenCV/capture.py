import cv2, time

camera_port=0
video=cv2.VideoCapture(camera_port,cv2.CAP_DSHOW)

# Check if the webcam is opened correctly
if not video.isOpened():
    raise IOError("Cannot open webcam")

#return_value, image = video.read()
#print("We take a picture of you, check the folder")
#cv2.imwrite("image.png", image)
a=1
while True:
    a=a+1
    check, frame=video.read()

    print(check)
    print(frame)

    cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #time.sleep(3)
    cv2.imshow("Capturing",frame)
    key=cv2.waitKey(1)

    if key==ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()

