import  numpy as np
from matplotlib import pyplot as plt
import cmath as c
def dtft(x):
	n1=len(x)
	j=c.sqrt(-1)
	p=np.pi
	X=[]
	for w in range(0,6,1):
		sum=0
		for  n in range(0,n1,1):
			sum=sum+x[n]*(np.exp(-j*w*n))
		y=np.append(sum)
	return y
y=np.array(input('enter seq1:'))
print(dtft(y))
print(np.abs(y))

