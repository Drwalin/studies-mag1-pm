import numpy as np
import time
import pandas as pd
import random
import cv2
import matplotlib.pyplot as plt
import math

def show(name, img):
    cv2.imshow(name, img);
    cv2.imwrite(name+".jpg", img);
    print(name);

t1 = time.time();

img = cv2.imread("./ali-tayyebi-unsplash-small.jpg")
show("original", img);
print(time.time()-t1);

img2 = np.ones(shape = (img.shape[0],img.shape[1]), dtype = np.uint8);
for i in range(0, img.shape[0], 1):
    for j in range(0, img.shape[1], 1):
        l = img[i,j];
        img2[i,j] = l[0]*0.299 + l[1]*0.587 + l[2]*0.114;
img = img2;
show("original_luminance", img);
print(time.time()-t1);

def iterate2d_kernel(img, kernel_size, func_kernel):
    ret = np.ones(shape = (img.shape[0],img.shape[1]), dtype = np.uint8);
    radius = kernel_size//2;
    for i in range(0, img.shape[0], 1):
        for j in range(0, img.shape[1], 1):
            dim = [i-radius, i+radius+1, j-radius,j+radius+1];
            for v in range(0,4):
                if dim[v] < 0: dim[v] = 0;
                if dim[v] > img.shape[1]: dim[v] = img.shape[1];
            rg = img[dim[0]:dim[1], dim[2]:dim[3]];
            ret[i,j] = func_kernel(rg);
    return ret;

def kernel_median(img):
    v = np.median(img);
    return v;

img2 = iterate2d_kernel(img, 3, kernel_median);
show("median3", img2);
print(time.time()-t1);

img2 = iterate2d_kernel(img, 11, kernel_median);
show("median11", img2);
print(time.time()-t1);

def kernel_average(img):
    v = np.average(img);
    return v;

img3 = iterate2d_kernel(img, 3, kernel_average);
show("average3", img3);
print(time.time()-t1);

img3 = iterate2d_kernel(img, 11, kernel_average);
show("average11", img3);
print(time.time()-t1);

cv2.waitKey(0)

