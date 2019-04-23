import numpy as np 
import matplotlib.pyplot as plt
M=31
W=[]
p=np.pi
t=np.arange(0,31,1)
for n in range(0,M,1):
	x=0.46*np.cos((2*p*n)/(M-1))
	S=0.54-x
	W=np.append(W,S)
plt.stem(t,W)
plt.show()


