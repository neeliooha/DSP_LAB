import numpy as np
from matplotlib import pyplot as plt
import cmath as c
M=31
t=np.arange(0,31,1)
W=[]
M=31
W=[]
t=np.arange(0,31,1)
for n in range(0,M,1):
	x=((M-1.0)/2.0)
	k=np.abs(n-x)
	p=float(((2.0*k)/(M-1.0)))
	s=1.0-(p)
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
plt.subplot(2,1,1)
plt.stem(t,W)
plt.title("triangular window")
plt.subplot(2,1,2)
plt.plot(w,np.abs(y))
plt.title("dtft of triangular window")
plt.show()

