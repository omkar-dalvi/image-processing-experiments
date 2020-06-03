import cv2
import numpy as np
image=cv2.imread('imageSeg.jpg')
cv2.imshow('input image',image)
cv2.waitKey(0)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray image',gray)
mean=0
for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        mean+=gray[i][j]
threshold=mean/(gray.shape[0]*gray.shape[1])
print(threshold)
segment1=gray.copy()
segment2=gray.copy()
for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        if segment1[i][j]>threshold:
            segment1[i][j]=255
        else:
            segment1[i][j]=0
cv2.imshow("Image segmentation with 2 segments",segment1)
for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        if segment2[i][j]>=180:
            segment2[i][j]=255
        elif segment2[i][j]<180 and segment2[i][j]>=70:
            segment2[i][j]=128
        else:
            segment2[i][j]=0
cv2.imshow("Image segmentation with 3 segments",segment2)
cv2.waitKey(0)
cv2.destroyAllWindows()

