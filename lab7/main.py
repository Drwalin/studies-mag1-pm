import numpy as np
import time
import pandas as pd
import random
import cv2
import matplotlib.pyplot as plt
import math
import datetime
import json;

vid = cv2.VideoCapture(0);

def DarkerGreen():
    return ( np.array([30,30,0]), np.array([100,200,150]));

def AnyYellow():
    return ( np.array([10,50,0]), np.array([70,255,255]));

def AnyBlueish():
    return ( np.array([100,0,0]), np.array([140,255,255]));

def AnySV(minH, maxH):
    return ( np.array([minH,0,0]), np.array([maxH,255,255]));

def nparr(a, b):
    return ( np.array([a]), np.array([b]));

while(1):
    _, frame = vid.read();
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV);
    
    minhsv, maxhsv = DarkerGreen();
#     minhsv, maxhsv = AnyYellow();
#     minhsv, maxhsv = AnyBlueish();
#     minhsv, maxhsv = AnySV(-20, 20);
    
    mask = cv2.inRange(hsv, minhsv, maxhsv);
    
#     mask = cv2.blur(mask, (30,30));
#     a, b = nparr(40,255);
#     mask = cv2.inRange(mask, a, b);
# 
#     mask = cv2.blur(mask, (30,30));
#     a, b = nparr(160,255);
#     mask = cv2.inRange(mask, a, b);
    
    res = cv2.bitwise_and(frame, frame, mask=mask);
    
    
    
#     res = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR);
#     res = hsv;
#     cv2.imshow('orig',frame);
#     res = frame;
    cv2.imshow('res',res);
    
    k = cv2.waitKey(5) & 0xFF;
    if k == 27:
        break;

cv2.destroyAllWindows();

