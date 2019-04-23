import numpy as np
from matplotlib import pyplot as plt
import cmath as c
t=np.arange(-15,15,0.1)
x1=(np.sinc(t/4))
h=0.25*x1
n1=len(h)
print n1
j=c.sqrt(-1)
p=np.pi
N=10000
y=[]
w=np.linspace(-3.14,3.14,N)
for i in range(0,N):
	sum=0
	for n in range(0,n1,1):
		sum=sum+h[n]*(np.exp(-j*w[i]*n))
	y=np.append(y,sum)
w=np.linspace(-3.14,3.14,N)
plt.subplot(2,1,1)
plt.stem(t,h)
plt.title("sinc")
plt.subplot(2,1,2)
plt.plot(w,np.abs(y))
plt.title("dtft of sinc")
plt.show()

