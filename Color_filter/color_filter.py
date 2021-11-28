from GUI import GUI
from HAL import HAL
import cv2
import numpy as np

while(1) :
   # x = ser.read()
    frame = HAL.getImage()
    #print(video_capture.get(cv2.CAP_PROP_FPS))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #RED = cv2.inRange(hsv, (25, 104, 36), (52, 255, 129))
    low_red = np.array([0,120,70])
    high_red = np.array([10,255,255])
    red_mask = cv2.inRange(hsv, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    red_mask2 = cv2.inRange(hsv,lower_red,upper_red)
    
    red_mask = red_mask + red_mask2

    #GUI.showImage()
    
    _, contours, _ = cv2.findContours(red_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 2000):
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), 
                                       (x + w, y + h), 
                                       (0, 0, 255), 2)
              
            cv2.putText(frame, "Red Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))   
                        
    
    GUI.showImage(frame)
    #cv2.imshow('Video', frame)
     