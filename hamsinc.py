import numpy as np
import matplotlib.pyplot as plt
import cmath as c
t=np.arange(-15,15,0.1)
x1=(np.sinc(t/4))
h=0.25*x1
M=31
W=[]
p=np.pi
b=[]
t1=np.arange(0,31,1)
for n in range(0,M,1):
	x=0.46*np.cos((2*p*n)/(M-1))
	S=0.54-x
	W=np.append(W,S)
for k in range(0,M,1):
	r=h[k]*W[k]
	b=np.append(b,r)
n1=len(b)
j=c.sqrt(-1)
p=np.pi
N=10000
y=[]
w=np.linspace(-3.14,3.14,N)
for i in range(0,N):
	sum=0
	for n in range(0,n1,1):
		sum=sum+b[n]*(np.exp(-j*w[i]*n))
	y=np.append(y,sum)
w=np.linspace(-3.14,3.14,N)
plt.subplot(3,1,1)
plt.stem(t1,W)
plt.title("haming window")
plt.subplot(3,1,2)
plt.plot(w,np.abs(y))
plt.title("lpf using haming window")
w=np.linspace(-3.14,3.14,N)
x1=np.abs(y)
x2=20*np.log(x1)
plt.subplot(3,1,3)
plt.plot(w,x2)
plt.title("lpf using  HAMING WINDOW IN dB's")
plt.show()
#w=np.linspace(-3.14,3.14,N)
#plt.plot(w,np.abs(y))
#plt.title("LPF BY USING HAMMING WINDOW")
#plt.show()

