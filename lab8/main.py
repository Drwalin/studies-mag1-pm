import numpy as np
import time
import pandas as pd
import random
import cv2
import matplotlib.pyplot as plt
import math
import datetime
import json;
from scipy.spatial.distance import euclidean, cityblock

HIST_DIM = 4;

file_names = [];
for i in range(0,1000,25):
    for j in range(0,10,1):
        n = './image.orig/' + str(i+j) + '.jpg';
        file_names.append(n);

images = [];
for filename in file_names:
    v = cv2.imread(filename);
    images.append(v);

def GetSimplifiedHistogram(image):
    img = np.floor(image/(256/HIST_DIM)).astype('uint8');
    hist = [];
    for i in range(0,3):
        hist_ = cv2.calcHist([img], [i], None, [HIST_DIM], [0,HIST_DIM]);
        hist_ = hist_/(img.shape[0]*img.shape[1]);
        for i in range(0,HIST_DIM):
            if i<len(hist_):
                hist.append(hist_[i][0]);
            else:
                hist.append(0);
    return hist;

hists = {};
for img in images:
    hist = GetSimplifiedHistogram(img);
    hists[str(hist)] = (img, hist);

def FindClosest(img, maxCount, distMethod):
    hist = GetSimplifiedHistogram(img);
    ret = [[float('inf'), None] for i in range(0,maxCount)];
    for imp in hists.values():
        dist = distMethod(hist, imp[1]);
        for i in range(0, maxCount):
            if ret[i][0] >= dist:
                ret.insert(i, (dist, imp[0]));
                break;
    if len(ret) > maxCount:
        ret = ret[0:maxCount];
    return ret;


example_image_files = [
        './image.orig/17.jpg',
        './image.orig/117.jpg',
        './image.orig/217.jpg',
        './image.orig/317.jpg',
        './image.orig/417.jpg'];

example_images = [];
for filename in example_image_files:
    v = cv2.imread(filename);
    example_images.append(v);

for img in example_images:
    closest = FindClosest(img, 5, euclidean);
    cv2.imshow('test image', img);
    for i in range(0,5):
        cv2.imshow('closest '+str(i+1), closest[i][1]);
    cv2.waitKey();
    closest = FindClosest(img, 5, cityblock);
    for i in range(0,5):
        cv2.imshow('closest '+str(i+1), closest[i][1]);
    cv2.waitKey();




cv2.waitKey();
cv2.destroyAllWindows();

