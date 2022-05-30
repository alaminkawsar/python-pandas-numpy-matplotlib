#https://appdividend.com/2022/03/19/python-cv2-videocapture/#:~:text=To%20capture%20a%20video%20in,for%20the%20second%20camera%2C%20etc.
#cv2.VideoCapture(0): Means first camera or webcam.
#cv2.VideoCapture(1):  Means second camera or webcam.
#cv2.VideoCapture("file name.mp4"): Means video file

#for downloading the image use
#cv2.VideoWriter(filename, fourcc, fps, frameSize)



import cv2

cap = cv2.VideoCapture(0)

#for video file open, use cap.isOpened() sytax inside the while loop
while(True):
    ret, frame = cap.read()
    #to change BGR to gray scale image
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()