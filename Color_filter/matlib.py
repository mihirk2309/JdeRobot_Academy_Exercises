""" import matplotlib.pyplot as plt
import numpy as np
import cv2
import pykinect2
x = np.arange(-4, 4, .1)
y = x * x
plt.plot(x, y, 'r-*')
plt.show()
video_capture = cv2.VideoCapture(0)
while(1) :
    ret, frame = video_capture.read()
    cv2.imshow('Video', frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')) :
        break
video_capture.release()
cv2.destroyAllWindows() """
import cv2
import numpy as np
import serial
import time
#import matplotlib.pyplot as plt
def nothing(x) :
    pass
cv2.namedWindow('Threshold')
hmax = 'hmax'
hmin = 'hmin'
smax = 'smax'
smin = 'smin'
vmax = 'vmax'
vmin = 'vmin'
cv2.createTrackbar("hmax", "Threshold", 0, 255, nothing)
cv2.createTrackbar("hmin", "Threshold", 0, 255, nothing)
cv2.createTrackbar("smax", "Threshold", 0, 255, nothing)
cv2.createTrackbar("smin", "Threshold", 0, 255, nothing)
cv2.createTrackbar("vmax", "Threshold", 0, 255, nothing)
cv2.createTrackbar("vmin", "Threshold", 0, 255, nothing)
video_capture = cv2.VideoCapture(0)
arrayx = []
arrayy = []
t = 0
#ser = serial.Serial(port = "/dev/ttyS0",baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 	0.0000001)
flag = 0
x = 'a'
while(1) :
   # x = ser.read()
    if (x == 's'):
        break
    hmax = cv2.getTrackbarPos("hmax", "Threshold")
    hmin = cv2.getTrackbarPos("hmin", "Threshold")
    smax = cv2.getTrackbarPos("smax", "Threshold")
    smin = cv2.getTrackbarPos("smin", "Threshold")
    vmax = cv2.getTrackbarPos("vmax", "Threshold")
    vmin = cv2.getTrackbarPos("vmin", "Threshold")
    ret, frame = video_capture.read()
    #print(video_capture.get(cv2.CAP_PROP_FPS))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #RED = cv2.inRange(hsv, (25, 104, 36), (52, 255, 129))
    RED = cv2.inRange(hsv, (hmin, smin, vmin), (hmax, smax, vmax))
    _,contours,_ = cv2.findContours(RED, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours :
        area = cv2.contourArea(cnt)
        if(area > 500) :
            #print(area)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
            cv2.circle(frame, (int(x+w/2),int(y+h/2)), 2, (255, 0, 0), thickness=5)
            print(int(x+w/2),480-int(y+h/2))
            arrayx.append(int(x+w/2))
            arrayy.append(480-int(y+h/2))
            if (arrayx[t] < 213  and arrayy[t] < 240 and flag != 1) :
                #ser.write('1')
                print("ZONE1")
                flag = 1 
            elif (arrayx[t] > 213  and arrayx[t] < 427 and arrayy[t] < 240 and flag != 2) :
                #ser.write('2')
                print("ZONE2")
                flag = 2
            elif (arrayx[t] > 427 and arrayy[t] < 240 and flag != 3) :
                #ser.write('3')
                print("ZONE3")
                flag = 3
            elif (arrayx[t] > 427 and arrayy[t] > 240 and flag != 4) :
                #ser.write('4')
                print("ZONE4")
                flag = 4
            elif (arrayx[t] > 213  and arrayx[t] < 427 and arrayy[t] > 240 and flag != 5) :
                #ser.write('5')
                print("ZONE5")
                flag = 5
            elif (arrayx[t] < 213 and arrayy[t] > 240 and flag != 6) :
                #ser.write('6')
                print("ZONE6")
                flag = 6
            #ser.write('a')
            #time.sleep(0.1)'''
            #time.sleep(0.1)'''
            #plt.plot(int(x+w/2),480-int(y+h/2), 'r-*')
            t += 1
    cv2.line(frame,(0,240),(640,240),(255,0,0),5)
    cv2.line(frame,(427,0),(427,480),(255,0,0),5)
    cv2.line(frame,(213,0),(213,480),(255,0,0),5)
    cv2.imshow('Video1', RED)
    cv2.imshow('Video', frame)
    
    if(cv2.waitKey(1) & 0xFF == ord('q')) :
        break
print(t)
'''for j in range(1, t) :
    plt.plot(arrayx[j-1], arrayy[j-1], arrayx[j], arrayy[j])
plt.show()'''
video_capture.release()
cv2.destroyAllWindows()

