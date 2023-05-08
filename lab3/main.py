import numpy as np
import time
import pandas as pd
import random
import cv2
import matplotlib.pyplot as plt
import math

img = cv2.imread("./ali-tayyebi-unsplash-small.jpg")

cv2.imshow("original", img);

def Iterate2d(img, func):
    for i in range(0, img.shape[0], 1):
        for j in range(0, img.shape[1], 1):
            img[i,j] = func(img[i,j], i, j)
    
def func_linear(x):
    if x <= 30:
        return 3*x
    else:
        return math.ceil(0.73*x + 68)

func_y = [[x, func_linear(x)] for x in range(0, 256)]

def func_3(x3, i, j):
    return [func_linear(x) for x in x3]

Iterate2d(img, func_3);

cv2.imshow("modified", img);

plt.plot(func_y);
plt.show();

cv2.waitKey(0)

