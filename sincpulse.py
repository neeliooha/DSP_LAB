import numpy as np 
import matplotlib.pyplot as plt
n=np.arange(-100,100,1)
wc=np.pi/4
h=(np.sin(wc*n))/(np.pi*n)
h[100]=1.0/4.0
plt.stem(n,h)
plt.title("sinc function")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()
