import cv2 
from matplotlib import pyplot as plt 

#calHist takes image and range of values for gray values
#images    : Source image represented as “[img]”.
#channels  : For grayscale image, its value is [0] 
#mask      : Mask image. 
#histSize  : BIN count
#ranges    : RANGE. 

img = cv2.imread('bright.jfif',0) 
histr = cv2.calcHist([img],[0],None,[256],[0,256])
cv2.imshow('image',img)
plt.title("Histogram of bright image")
plt.xlabel("Gray value")
plt.ylabel("Frequency")
plt.plot(histr) 
plt.show()
cv2.waitKey(0)

img = cv2.imread('dark.jpg',0) 
histr = cv2.calcHist([img],[0],None,[256],[0,256])
cv2.imshow('image',img)
plt.title("Histogram of dark image")
plt.xlabel("Gray value")
plt.ylabel("Frequency")
plt.plot(histr) 
plt.show()
cv2.waitKey(0)

img = cv2.imread('highcontrast.jpg',0) 
histr = cv2.calcHist([img],[0],None,[256],[0,256])
cv2.imshow('image',img)
plt.title("Histogram of High Contrast image")
plt.xlabel("Gray value")
plt.ylabel("Frequency")
plt.plot(histr) 
plt.show()
cv2.waitKey(0)
img = cv2.imread('lowcontrast.jpg',0) 
histr = cv2.calcHist([img],[0],None,[256],[0,256])
cv2.imshow('image',img)
plt.title("Histogram of Low Contrast image")
plt.xlabel("Gray value")
plt.ylabel("Frequency")
plt.plot(histr) 
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

