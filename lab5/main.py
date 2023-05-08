import numpy as np
import time
import pandas as pd
import random
import cv2
import matplotlib.pyplot as plt
import math
import datetime

video = cv2.VideoCapture('moon.mov');
# video = cv2.VideoCapture(0);

frameId = 0;

while video.isOpened():
    frameId = frameId + 1;
    ret, frame = video.read();
    if not ret:
        break;
    
    m = frame.shape[0:2];
    m = (m[0]//2, m[1]//2);
    
    k = np.ones((3, 3), np.float32);
    k[0,0] = 0;
    k[0,1] = -1;
    k[0,2] = 0;
    k[1,0] = -1;
    k[1,1] = 5
    k[1,2] = -1;
    k[2,0] = 0;
    k[2,1] = -1;
    k[2,2] = 0;
    
    frame[m[0]:, 0:m[1], :] = cv2.blur(frame[m[0]:, 0:m[1], :], (30, 30));
    
    gray = cv2.cvtColor(frame[0:m[0], 0:m[1], :], cv2.COLOR_BGR2GRAY);
    frame[0:m[0], 0:m[1], 0] = gray;
    frame[0:m[0], 0:m[1], 1] = gray;
    frame[0:m[0], 0:m[1], 2] = gray;
    
    frame[0:m[0], m[1]:, :] = cv2.GaussianBlur(frame[0:m[0], m[1]:, :],
                                                (31, 31), cv2.BORDER_DEFAULT);
    
    frame[m[0]:, m[1]:, :] = cv2.filter2D(src=frame[m[0]:, m[1]:, :], ddepth=-1,
                                          kernel=k);
    
    cv2.putText(frame, text = str(datetime.datetime.now()), 
                org = (32,32), 
                fontFace = cv2.FONT_HERSHEY_SIMPLEX, 
                fontScale = 1.0, 
                color = (0,255,0), 
                thickness = 1);
    
    cv2.putText(frame, text = "Frame: " + str(frameId), 
                org = (32,64), 
                fontFace = cv2.FONT_HERSHEY_SIMPLEX, 
                fontScale = 1.0, 
                color = (0,255,0), 
                thickness = 1);
        
    cv2.imshow('video',frame);
    if cv2.waitKey(1) == 27:
        break;

video.release();
cv2.destroyAllWindows();

exit();


