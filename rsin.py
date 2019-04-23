import numpy as np
import matplotlib.pyplot as plt
import cmath as c
t=np.arange(-15,15,0.1)
x1=(np.sinc(t/4))
h=0.25*x1
M=31
t1=np.arange(0,31,1)
W=[]
a=[]
for n in range(0,31,1):
	w=1
	W=np.append(W,w)
for k in range(0,31,1):
	s=h[k]*W[k]
	a=np.append(a,s)
n1=len(a)
j=c.sqrt(-1)
p=np.pi
N=10000
y=[]
w=np.linspace(-3.14,3.14,N)
for i in range(0,N):
	sum=0
	for n in range(0,n1,1):
		sum=sum+a[n]*(np.exp(-j*w[i]*n))
	y=np.append(y,sum)
w=np.linspace(-3.14,3.14,N)
plt.subplot(3,1,1)
plt.stem(t1,W)
plt.title("rectangular window")
plt.subplot(3,1,2)
plt.plot(w,np.abs(y))
plt.title("lpf using rectangular window")
w=np.linspace(-3.14,3.14,N)
x1=np.abs(y)
x2=20*np.log(x1)
plt.subplot(3,1,3)
plt.plot(w,x2)
plt.title("lpf using  rectangular window IN dB's")
plt.show()


#w=np.linspace(-3.14,3.14,N)
#plt.plot(w,np.abs(y))
#plt.title("LPF BY USING RECT")
#plt.show()


