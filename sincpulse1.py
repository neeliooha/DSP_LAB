import numpy as np 
import matplotlib.pyplot as plt
n=np.arange(-100,100,1)
wc=np.pi/4
h=(np.sinc(wc*n))
h1=h*0.25
plt.stem(n,h1)
plt.title("sinc function")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()
