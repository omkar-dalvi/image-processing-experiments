# Importing libraries
import cv2
import numpy
# Reading image
img=cv2.imread("dsipl2img.jfif",0)
# Initialize empty bit array
bitArray=[]
# Appending bit values of each pixel to list

for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		bitArray.append(numpy.binary_repr(img[i][j],width=8))
# bitArray consists of string binary representation
# array takes two parameters
# 1.Array of bit planes
# 2.Type of the bit
# Reshape function converts 1-D array to 2-D array
eightBitImage=(numpy.array([int(i[0]) for i in bitArray],dtype=numpy.uint8)*128).reshape(img.shape[0],img.shape[1])
sevenBitImage=(numpy.array([int(i[1]) for i in bitArray],dtype=numpy.uint8)*64).reshape(img.shape[0],img.shape[1])
sixBitImage=(numpy.array([int(i[2]) for i in bitArray],dtype=numpy.uint8)*32).reshape(img.shape[0],img.shape[1])
fiveBitImage=(numpy.array([int(i[3]) for i in bitArray],dtype=numpy.uint8)*16).reshape(img.shape[0],img.shape[1])
fourBitImage=(numpy.array([int(i[4]) for i in bitArray],dtype=numpy.uint8)*8).reshape(img.shape[0],img.shape[1])
threeBitImage=(numpy.array([int(i[5]) for i in bitArray],dtype=numpy.uint8)*4).reshape(img.shape[0],img.shape[1])
twoBitImage=(numpy.array([int(i[6]) for i in bitArray],dtype=numpy.uint8)*2).reshape(img.shape[0],img.shape[1])
oneBitImage=(numpy.array([int(i[7]) for i in bitArray],dtype=numpy.uint8)*1).reshape(img.shape[0],img.shape[1])
cv2.imshow('Eigth Bit Plane Image',eightBitImage)
cv2.waitKey(0)
cv2.imshow('Seventh Bit Plane Image',sevenBitImage)
cv2.waitKey(0)
cv2.imshow('Sixth Bit Plane Image',sixBitImage)
cv2.waitKey(0)
cv2.imshow('Fifth Bit Plane Image',fiveBitImage)
cv2.waitKey(0)
cv2.imshow('Fourth Bit Plane Image',fourBitImage)
cv2.waitKey(0)
cv2.imshow('Third Bit Plane Image',threeBitImage)
cv2.waitKey(0)
cv2.imshow('Second Bit Plane Image',twoBitImage)
cv2.waitKey(0)
cv2.imshow('First Bit Plane Image',oneBitImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
