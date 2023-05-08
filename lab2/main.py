import numpy as np
import time
import pandas as pd
import random
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("./butterfly.jpg")

def Iterate2d(img, func):
    for i in range(0, img.shape[0], 1):
        for j in range(0, img.shape[1], 1):
            img[i,j] = func(img[i,j], i, j)
    

print(type(img1))

# task 1:

# max = img1.max(

print("line ", 1)

maxRed = 0
for i in range(0, img1.shape[0], 1):
    for j in range(0, img1.shape[1], 1):
        if maxRed < img1[i,j,0]:
           maxRed = img1[i,j,0]
print("line ", 2)

def task1(color, i, j):
   if color[0] < 0.2*maxRed:
       v = sum(color)//3
       return [v,v,v]
   else:
       return color
print("line ", 3)
Iterate2d(img1, task1)
print("line ", 4)

cv2.imshow("name", img1)
# cv2.waitKey(0)



# task 2:
img1 = cv2.imread("./butterfly.jpg")

for i in range(0, img1.shape[0], 1):
    for j in range(0, img1.shape[1], 1):
        for k in range(0, img1.shape[2], 1):
            if random.randrange(0,10000) < 5000:
                v = img1[i,j,k]
                v += random.randrange(-255,255)
                if v<0:
                    v=0
                elif v>255:
                    v=255
                img1[i,j,k] = v

cv2.imshow("name2", img1)
cv2.waitKey(0)





