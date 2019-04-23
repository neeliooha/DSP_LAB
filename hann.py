import numpy as np 
import matplotlib.pyplot as plt
M=31
W=[]
p=np.pi
k=np.arange(0,31,1)
for n in range(0,M):
	t=((2*p*n)/(M-1))
	s=0.5-(0.5*np.cos(t))
	W=np.append(W,s)
plt.stem(k,W)
plt.show()
