import numpy as np
import cv2
import os
img = np.zeros((3,3), dtype=np.uint8)

print(img)
img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

img =- np.zeros((5,3),dtype=np.uint8)
print(img.shape)
#img = cv2.imread('chapter02/MyPic.png')
img = cv2.imread('MyPic.png',cv2.IMREAD_REDUCED_GRAYSCALE_8)
cv2.imwrite('MyPic.jpg',img)

rng = np.random.default_rng()
randomByteArray = rng.integers(low=0, high=255, size=120000)
grayImage = randomByteArray.reshape(300,400)
cv2.imwrite('RandomGray.png',grayImage)

img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
cv2.imwrite('RandomColorImage.png',randomByteArray.reshape(100,400,3))
for row in np.arange(0,20):
    for col in np.arange(50,100):
        grayImage[row,col] = 255

cv2.imwrite('BackOut.jpg',img)