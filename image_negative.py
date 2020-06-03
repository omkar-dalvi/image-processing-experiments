#Image Negative
from PIL import Image

img = Image.open('negation.jpg')
img.show()
pixels = img.load()

#negative image
for i in range(img.size[0]):
    for j in range(img.size[1]):
        x,y,z = pixels[i,j][0],pixels[i,j][1],pixels[i,j][2]
        x,y,z = abs(x-255), abs(y-255), abs(z-255)
        pixels[i,j] = (x,y,z)
img.show()
