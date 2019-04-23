import  numpy as np
from matplotlib import pyplot as plt
import cmath as c
x=np.array(input('enter seq1:'))
n1=len(x)
j=c.sqrt(-1)
p=np.pi
N=10000
y=[]
w=np.linspace(0,2*p,N)
for i in range(0,N):
	sum=0
	for n in range(0,n1,1):
		sum=sum+x[n]*(np.exp(-j*w[i]*n))
	y=np.append(y,sum)
plt.plot(w,np.angle(y))
plt.show()


