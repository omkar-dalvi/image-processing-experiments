import numpy as np
import matplotlib.pyplot as plt
import math
xnnp=np.array([3+0*1j,4+0*1j,0+0*1j,6+0*1j])
nx=np.arange(4)
plt.stem(nx,xnnp)
plt.title("x(n)")
plt.xlabel("n")
plt.ylabel("x(n)")
plt.show()
ans=[]
r1=np.array([1+0*1j,1+0*1j,1+0*1j,1+0*1j])
a1=np.vdot(xnnp,r1)
ans.append(a1)
r2=np.array([1+0*1j,0+(-1)*1j,-1+0*1j,0+1j])
a2=np.vdot(xnnp,r2)
ans.append(a2)
r3=np.array([1+0*1j,-1+0*1j,1+0*1j,-1+0*1j])
a3=np.vdot(xnnp,r1)
ans.append(a3)
r4=np.array([1+0*1j,0+1*1j,-1+0*1j,0+(-1)*1j])
a4=np.vdot(xnnp,r2)
ans.append(a4)
real=[]
img=[]
for i in ans:
    real.append(i.real)
    img.append(i.imag)
magnitude=[]
angle=[]
for i in range(len(real)):
    magnitude.append(math.sqrt(pow(real[i],2)+pow(img[i],2)))
    angle.append(math.atan(img[i]/real[i]))
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

