import numpy as np
from matplotlib import pyplot as plt
import cmath as c
M=31
W=[]
p=np.pi
t=np.arange(0,M,1)
for n in range(0,M,1):
	k=0.5*np.cos((2*p*n)/(M-1))
	h=0.08*np.cos((4*p*n)/(M-1))
	s=0.42-k+h
	W=np.append(W,s)
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
plt.subplot(3,1,1)
plt.stem(t,W)
plt.title("blackman window")
plt.subplot(3,1,2)
plt.plot(w,np.abs(y))
plt.title("dtft of blackman window")
w=np.linspace(-3.14,3.14,N)
x1=np.abs(y)
x2=20*np.log(x1)
plt.subplot(3,1,3)
plt.plot(w,x2)
plt.title("DTFT OF BLACKMAN WINDOW IN dB's")
plt.show()



