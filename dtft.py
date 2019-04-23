import  numpy as np
from matplotlib import pyplot as plt
import cmath as c
def dtft(x):
	n1=len(x)
	j=c.sqrt(-1)
	p=np.pi
	y=[]
	for w in range(0,2*p,0.1):
		sum=0
		for  n in range(0,n1,1):
			sum=sum+x[n]*(np.exp(-j*w*n))
		y=np.append(y,sum)
	return y
x=np.array(input('enter seq1:'))
print(dtft(x))
print('dtft=',np.dt(x))

