import numpy as np
from matplotlib import pyplot as plt
import cmath as c
M=31
W=[]
p=np.pi
t=np.arange(0,31,1)
for n in range(0,M,1):
	x=0.5*np.cos((2*p*n)/(M-1))
	S=0.5-x
	W=np.append(W,S)
n1=len(W)
j=c.sqrt(-1)
p=np.pi
N=10000
y=[]
w=np.linspace(-3.14,3.14,N)
for i in range(0,N):
	sum=0
	for n in range(0,n1,1):
		sum=sum+W[n]*(np.exp(-j*w[i]*n))
	y=np.append(y,sum)
w=np.linspace(-3.14,3.14,N)
plt.subplot(2,1,1)
plt.stem(t,W)
plt.title("hanning window")
plt.subplot(2,1,2)
plt.plot(w,np.abs(y))
plt.title("dtft of hanning window")
plt.show()


