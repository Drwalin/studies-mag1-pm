import numpy as np
import time
import pandas as pd
import random
import cv2
import matplotlib.pyplot as plt

# %matplotlib inline


# Korzystając z poniższego przykładu wykonaj analogiczny patchwork,
# ale dla obrazu barwnego RGB. W takim przypadku piksele są wektorami.
# To jedyna zmiana w stosunku do przedstawionego przykładu.
# Barwy obrazów składowych wybierz dowolnie.

img1 = cv2.imread("./691.jpg")

# task 1:

for i in range(0, img1.shape[0], 1):
    for j in range(0, img1.shape[1], 1):
        if random.randrange(0,10000) < 5000:
            img1[i,j] = [255,255,255]

cv2.imshow("name", img1)
cv2.waitKey(0)





# task 2:
img1 = np.random.rand(3) * np.ones(shape = (50,50,3), dtype = np.uint8)
img2 = np.random.rand(3) *np.ones(shape = (50,50,3), dtype = np.uint8)
img3 = np.random.rand(3) * np.ones(shape = (50,50,3), dtype = np.uint8)
img4 = np.random.rand(3) * np.ones(shape = (50,50,3), dtype = np.uint8)

row1 = np.concatenate([img1,img2], axis = 1)
row2 = np.concatenate([img3,img4], axis = 1)
img = np.concatenate([row1, row2], axis = 0)
plt.imshow(img,cmap = 'gray')
plt.xticks([])
plt.yticks([])
plt.axis(False)
plt.show()




# task 3:

img5 = np.ones(shape = (32,32), dtype = np.uint8) * 255
cv2.line(img5, (3,1), (11,22), 0, 2);
cv2.imshow("Task 3", img5)
print(img5[:6,:6])
cv2.waitKey(0)



