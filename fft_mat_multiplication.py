import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
import math
x = np.array([3,4,0,6])
ans = fftpack.fft(x)
nx=np.arange(4)
plt.stem(nx,x)
plt.title("x(n)")
plt.xlabel("n")
plt.ylabel("x(n)")
plt.show()
real=[]
img=[]
for i in ans:
    real.append(i.real)
    img.append(i.imag)
magnitude=[]
angle=[]
for i in range(len(real)):
    magnitude.append(math.sqrt(pow(real[i],2)+pow(img[i],2)))
    angle.append(abs(math.atan(img[i]/real[i])))
print(magnitude,angle)
mnp=np.copy(magnitude)
anp=np.copy(angle)
plt.stem(nx,mnp)
plt.title("|X(n)|")
plt.xlabel("n")
plt.ylabel("|X(n)|")
plt.show()
plt.stem(nx,anp)
plt.title("Angle(X(n))")
plt.xlabel("n")
plt.ylabel("Angle(|X(n)|)")
plt.show()





