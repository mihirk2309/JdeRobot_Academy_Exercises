from GUI import GUI
from HAL import HAL
import numpy as np
import cv2

flag = 0
start = 0
stop = 0
err = 0
prev_error = 0
kp = 0.004
kd = 0.003

while True:
    
    raw = HAL.getImage()
    image = cv2.cvtColor(raw, cv2.COLOR_BGR2GRAY)
    
    ret, thresh1 = cv2.threshold(image,85,255,cv2.THRESH_BINARY)
    GUI.showImage(thresh1)
    
    median = cv2.medianBlur(thresh1, 5)
    GUI.showImage(median)
    
    for i in range(160,480):
        if (median[280][i] == 0):
            if flag == 1:
                stop = i
                flag = 0
        elif (median[280][i] == 255):
            if flag == 0:
                start = i
                flag = 1
            
    pos = (start+stop)/2
    mid = 320
    
    err = mid - pos
    console.print(err)
    w = kp*float(err) + kd*float(err-prev_error)
    
    HAL.motors.sendV(1.8)
    console.print("W = " + str(w))
    HAL.motors.sendW(w)
    prev_error = err