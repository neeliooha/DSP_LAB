import numpy as np 
import matplotlib.pyplot as plt
M=31
W=[]
t=np.arange(0,31,1)
for n in range(0,M,1):
	s=((M-1.0)/2.0)
	k=np.abs(n-s)
	p=M-1.0
	r=float(1.0-(2.0*k/p))
	W=np.append(W,r)
plt.stem(t,W)
plt.show()

