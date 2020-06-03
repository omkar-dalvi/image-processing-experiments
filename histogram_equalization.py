import cv2
from matplotlib import pyplot as plt 
img = cv2.imread('he.png',0)
# find frequency of pixels in range 0-255 
histr = cv2.calcHist([img],[0],None,[256],[0,256])
plt.title("Histogram -original image")
plt.xlabel("grey values")
plt.ylabel("frequency")
# show the plotting graph of an image
plt.plot(histr)
cv2.imshow('original',img)
cv2.waitKey(0)
plt.show()

#Equilization
equalized_img = cv2.equalizeHist(img)

histr = cv2.calcHist([equalized_img],[0],None,[256],[0,256])
plt.title("Histogram -equilized image")
plt.xlabel("grey values")
plt.ylabel("frequency")
# show the plotting graph of an image
plt.plot(histr)
cv2.imshow('Histogram Equilization',equalized_img)
cv2.waitKey(0)
plt.show()




