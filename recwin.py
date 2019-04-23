import numpy as np 
import matplotlib.pyplot as plt
m=31
W=[]
t=np.arange(0,31,1)
for n in range(0,31,1):
	w=1
	W=np.append(W,w)
plt.stem(t,W)
plt.show()



