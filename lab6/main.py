import numpy as np
import time
import pandas as pd
import random
import cv2
import matplotlib.pyplot as plt
import math
import datetime
import json;




def LoadHistogram(img, fileName="hist.json"):
    def SaveToFile(fileName, self):
        s = json.dumps(self);
        f = open(fileName, "w");
        f.write(s);
        f.close();
    def ReadFromFile(fileName):
        try:
            f = open(fileName, "r");
            s = f.read();
            f.close();
            return json.loads(s);
        except:
            return [];
    inv_hist = ReadFromFile(fileName);
    if len(inv_hist) == 0:
        img2 = (img // 64);
        linear = img2.reshape(img2.shape[0]*img2.shape[1], 3);
        hist = {(i,j,k): 0 for i in range(0,4) for j in range(0,4) for k in range(0,4)};
        for i in range(0,linear.shape[0]):
            hist[ linear[i,0],linear[i,1],linear[i,2] ] = hist[linear[i,0],linear[i,1],linear[i,2]] + 1;

        inv_hist = [];
        for i in range(0,4):
            for j in range(0,4):
                for k in range(0,4):
                    obj = (hist[i,j,k], [i*64+32, j*64+32, k*64+32]);
                    inv_hist.append(obj);
                    
        inv_hist = sorted(inv_hist, key=lambda v:-v[0]);
        SaveToFile(fileName, inv_hist);
        print("saved histogram");
    else:
        print("loaded histogram");
    return inv_hist;





def dist2(a, b):
    c = a[0] - b[0];
    d = a[1] - b[1];
    e = a[2] - b[2];
    return c*c + d*d + e*e;

def closest_value(inv_hist, p):
    min_dist2 = dist2(inv_hist[0][1], p);
    min_id = 0;
    for i in range(1, len(inv_hist)):
        d = dist2(inv_hist[i][1], p);
        if d < min_dist2:
            min_dist2 = d;
            min_id = i;
    return inv_hist[min_id][1];

def filter(image, inv_hist):
    img = image.copy();
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            img[i,j] = closest_value(inv_hist, img[i,j]);
    return img;



def show(name, img):
    cv2.imshow(name, img);
    cv2.imwrite(name+".jpg", img);
    print(name);



img = cv2.imread("./butterfly.jpg");

inv_hist = LoadHistogram(img);
exit();

show("original", img);

img2 = (img // 64) * 64 + 32;
show("task_1", img2);


img_q2 = filter(img, inv_hist[0:2]);
show("colors2", img_q2);

img_q4 = filter(img, inv_hist[0:4]);
show("colors4", img_q4);

img_q8 = filter(img, inv_hist[0:8]);
show("colors8", img_q8);

img_q16 = filter(img, inv_hist[0:16]);
show("colors16", img_q16);

img_q32 = filter(img, inv_hist[0:32]);
show("colors32", img_q32);



# cv2.waitKey(0)
exit();


