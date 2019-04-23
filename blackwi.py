import numpy as np 
import matplotlib.pyplot as plt
M=31
W=[]
p=np.pi
t=np.arange(0,31,1)
for n in range(0,M,1):
	k=0.5*np.cos((2*p*n)/(M-1))
	c=0.08*np.cos((4*p*n)/(M-1))
	s=0.42-k+c
	W=np.append(W,s)
plt.stem(t,W)
plt.show()



